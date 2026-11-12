"""Read-only local checks for DearSunday's static SEO bundle."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
from xml.etree import ElementTree
import json
import sys
import re
from html import unescape

ROOT = Path(__file__).resolve().parent
BASE = "https://dearsunday.moriclass.com/"
SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonicals = []
        self.meta = {}
        self.references = []
        self.jsonld = []
        self.images = []
        self.title_parts = []
        self.in_title = False
        self.h1_parts = []
        self.h1_count = 0
        self.in_h1 = False
        self.visible_parts = []
        self._script_depth = 0
        self._prose_depth = 0
        self._faq_depth = 0
        self._cta_depth = 0
        self.prose_parts = []
        self._jsonld = False
        self._script_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "article" and "prose" in attrs.get("class", "").split():
            self._prose_depth += 1
        if tag == "div" and "faq-block" in attrs.get("class", "").split():
            self._faq_depth += 1
        if tag == "div" and "cta-box" in attrs.get("class", "").split():
            self._cta_depth += 1
        if tag == "link" and attrs.get("rel", "").lower() == "canonical":
            self.canonicals.append(attrs.get("href", ""))
        if tag == "meta":
            key = attrs.get("property") or attrs.get("name")
            if key:
                self.meta[key.lower()] = attrs.get("content", "")
        if tag == "h1":
            self.h1_count += 1
            self.in_h1 = True
        if tag == "a" and attrs.get("href"):
            self.references.append(("link", attrs["href"]))
        if tag == "img" and attrs.get("src"):
            self.references.append(("image", attrs["src"]))
            self.images.append((attrs["src"], attrs.get("alt")))
        if tag == "script" and attrs.get("type", "").lower() == "application/ld+json":
            self._jsonld = True
            self._script_parts = []
        elif tag == "script" or tag == "style":
            self._script_depth += 1
        if tag == "title":
            self.in_title = True

    def handle_data(self, data):
        if self._jsonld:
            self._script_parts.append(data)
        elif self._script_depth == 0:
            self.visible_parts.append(data)
            if self._prose_depth and not self._faq_depth and not self._cta_depth:
                self.prose_parts.append(data)
        if self.in_title:
            self.title_parts.append(data)
        if self.in_h1:
            self.h1_parts.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._jsonld:
            self.jsonld.append("".join(self._script_parts))
            self._jsonld = False
        elif tag in ("script", "style") and self._script_depth:
            self._script_depth -= 1
        if tag == "title":
            self.in_title = False
        if tag == "h1":
            self.in_h1 = False
        if tag == "article" and self._prose_depth:
            self._prose_depth -= 1
        if tag == "div" and self._faq_depth:
            self._faq_depth -= 1
        if tag == "div" and self._cta_depth:
            self._cta_depth -= 1


def page_paths(root):
    return [root / "index.html", root / "about.html", root / "lich.html", *sorted((root / "blog").glob("*.html"))]


def page_url(path, root):
    rel = path.relative_to(root).as_posix()
    return BASE if rel == "index.html" else urljoin(BASE, rel)


def check_bundle(root, label):
    errors = []
    pages = page_paths(root)
    canonical_urls = []
    for path in pages:
        parser = PageParser()
        try:
            html = path.read_text(encoding="utf-8")
            parser.feed(html)
        except (OSError, UnicodeError) as exc:
            errors.append(f"{label}: cannot read {path.relative_to(root)}: {exc}")
            continue
        expected = page_url(path, root)
        title = unescape("".join(parser.title_parts)).strip()
        h1 = unescape("".join(parser.h1_parts)).strip()
        description = parser.meta.get("description", "").strip()
        if parser.canonicals != [expected]:
            errors.append(f"{label}: {path.relative_to(root)} canonical expected exactly {expected}; got {parser.canonicals}")
        if not title:
            errors.append(f"{label}: {path.relative_to(root)} is missing a title")
        if parser.h1_count != 1 or not h1:
            errors.append(f"{label}: {path.relative_to(root)} expected one non-empty H1; found {parser.h1_count}")
        if not description:
            errors.append(f"{label}: {path.relative_to(root)} is missing a meta description")
        for key, value in (("og:title", title), ("og:description", description), ("og:url", expected)):
            if parser.meta.get(key) != value:
                errors.append(f"{label}: {path.relative_to(root)} {key} does not match page metadata")
        canonical_urls.extend(parser.canonicals)
        for kind, ref in parser.references:
            parsed = urlparse(ref)
            if parsed.scheme or ref.startswith("//") or ref.startswith("#"):
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(f"{label}: {path.relative_to(root)} {kind} escapes site root: {ref}")
            elif not target.is_file():
                errors.append(f"{label}: {path.relative_to(root)} missing {kind}: {ref}")
        for src, alt in parser.images:
            if alt is None or not alt.strip():
                errors.append(f"{label}: {path.relative_to(root)} image {src} has no useful alt text")
        for index, raw in enumerate(parser.jsonld, 1):
            try:
                data = json.loads(raw)
                if data.get("@type") == "BlogPosting":
                    article_text = unescape(re.sub(r"\s+", " ", " ".join(parser.prose_parts))).strip()
                    article_words = len(article_text.split())
                    if data.get("wordCount") != article_words:
                        errors.append(f"{label}: {path.relative_to(root)} BlogPosting wordCount {data.get('wordCount')} does not match article prose ({article_words})")
                    if not data.get("dateModified"):
                        errors.append(f"{label}: {path.relative_to(root)} BlogPosting has no dateModified")
                    expected_image = urljoin(expected, next((src for src, _ in parser.images), ""))
                    if data.get("image") != [expected_image]:
                        errors.append(f"{label}: {path.relative_to(root)} BlogPosting image does not match its visible cover")
            except json.JSONDecodeError as exc:
                errors.append(f"{label}: {path.relative_to(root)} JSON-LD block {index} invalid: {exc}")

    xml_path = root / "sitemap.xml"
    txt_path = root / "sitemap.txt"
    try:
        xml_urls = [node.text or "" for node in ElementTree.parse(xml_path).findall("sm:url/sm:loc", SITEMAP_NS)]
    except (OSError, ElementTree.ParseError) as exc:
        xml_urls = []
        errors.append(f"{label}: sitemap.xml invalid: {exc}")
    try:
        txt_urls = [line.strip() for line in txt_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, UnicodeError) as exc:
        txt_urls = []
        errors.append(f"{label}: sitemap.txt cannot be read: {exc}")

    if len(canonical_urls) != len(set(canonical_urls)):
        errors.append(f"{label}: duplicate canonical URLs")
    if xml_urls != canonical_urls:
        errors.append(f"{label}: sitemap.xml URLs do not exactly match page canonicals/order")
    if txt_urls != canonical_urls:
        errors.append(f"{label}: sitemap.txt URLs do not exactly match page canonicals/order")
    if not pages:
        errors.append(f"{label}: no HTML pages found")
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return len(errors)
    print(f"PASS {label}: {len(pages)} HTML pages; canonical, XML/text sitemap, local links/images, and JSON-LD are consistent")
    return 0


def main():
    errors = check_bundle(ROOT, "source")
    dist = ROOT / "dist"
    if dist.is_dir():
        errors += check_bundle(dist, "dist")
    else:
        print("FAIL dist directory is missing; run prepare_publish.py after updating source")
        errors += 1
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())


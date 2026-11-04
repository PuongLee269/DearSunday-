"""Refresh public metadata after generating articles; keep the static bundle in sync."""
from pathlib import Path
from html import escape, unescape
from urllib.parse import urljoin
import json
import re
import shutil
from xml.etree.ElementTree import Element, SubElement, ElementTree, register_namespace, indent

ROOT = Path(__file__).resolve().parent
BASE = "https://puonglee269.github.io/DearSunday-/"
pages = [ROOT / "index.html", ROOT / "about.html", *sorted((ROOT / "blog").glob("*.html"))]
urls = []
page_images = {}
for path in pages:
    relative = path.relative_to(ROOT).as_posix()
    url = BASE if relative == "index.html" else urljoin(BASE, relative)
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<!-- public-meta -->.*?<!-- /public-meta -->", "", text, flags=re.S)
    title = unescape(re.search(r"<title>(.*?)</title>", text, re.S)[1])
    desc = unescape(re.search(r'<meta name="description" content="([^"]*)"', text)[1])
    image = re.search(r'<img[^>]+src="([^"]+)"', text)[1]
    image_url = urljoin(urljoin(BASE, relative), image)
    def update_schema(match):
        data = json.loads(match[1])
        if data.get("@type") != "BreadcrumbList":
            data["url"] = url
        if data.get("@type") == "BlogPosting":
            data["mainEntityOfPage"] = {"@type": "WebPage", "@id": url}
            data["image"] = [image_url]
        return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + '</script>'
    text = re.sub(r'<script type="application/ld\+json">(.*?)</script>', update_schema, text, flags=re.S)
    fields = {"og:type": "article" if relative.startswith("blog/") else "website", "og:locale": "vi_VN", "og:site_name": "DearSunday Journal", "og:title": title, "og:description": desc, "og:url": url, "og:image": image_url, "twitter:card": "summary_large_image"}
    meta = '<!-- public-meta --><link rel="canonical" href="' + escape(url, quote=True) + '">'
    for key, value in fields.items():
        attribute = "name" if key.startswith("twitter:") else "property"
        meta += f'<meta {attribute}="{key}" content="{escape(value, quote=True)}">'
    meta += '<!-- /public-meta -->'
    path.write_text(text.replace('</head>', meta + '</head>'), encoding="utf-8")
    urls.append(url)
    page_images[url] = sorted({urljoin(urljoin(BASE, relative), src) for src in re.findall(r'<img[^>]+src="([^"]+)"', text)})

SM = "http://www.sitemaps.org/schemas/sitemap/0.9"
IM = "http://www.google.com/schemas/sitemap-image/1.1"
register_namespace("", SM)
register_namespace("image", IM)
sitemap = Element(f"{{{SM}}}urlset")
for url in urls:
    entry = SubElement(sitemap, f"{{{SM}}}url")
    SubElement(entry, f"{{{SM}}}loc").text = url
    for image_url in page_images[url]:
        image_entry = SubElement(entry, f"{{{IM}}}image")
        SubElement(image_entry, f"{{{IM}}}loc").text = image_url
indent(sitemap, space="  ")
ElementTree(sitemap).write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
(ROOT / "sitemap.txt").write_text("\n".join(urls) + "\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")
for path in [*pages, ROOT / "sitemap.xml", ROOT / "sitemap.txt", ROOT / "robots.txt", ROOT / "styles.css", ROOT / "favicon.svg", ROOT / ".nojekyll"]:
    target = ROOT / "dist" / path.relative_to(ROOT)
    target.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".html":
        # GitHub Pages publishes the repository root, including this bundle.
        # Keep /dist/ available for other hosting but exclude its duplicate pages.
        target.write_text(path.read_text(encoding="utf-8").replace('content="index,follow,max-image-preview:large"', 'content="noindex,follow"'), encoding="utf-8")
    else:
        shutil.copy2(path, target)
print(f"Prepared {len(urls)} public URLs and synchronized dist")

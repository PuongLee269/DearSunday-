# DearSunday Journal

Static Vietnamese blog for DearSunday private homestay. The site is focused on helpful, original guides for couples, Thanh Xuân and Hà Nội; the exact accommodation address is not published.

## Files

- `index.html`: journal home and article index
- `about.html`: verified DearSunday overview and current service windows
- `blog/`: six search-focused guides with distinct optimized room images
- `images/`: original WebP room photographs, oriented from the source image metadata
- `images/responsive/`: checked-in WebP width variants referenced by page `srcset`; `prepare_publish.py` copies them into `dist/`
- `generate_articles.py`: regenerates the six article pages
- `dist/`: static deployment package for Codex Sites and GitHub Pages

## Publishing

- Public URL: https://dearsunday.moriclass.com/
- GitHub Pages publishes `main` from the repository root.
- `CNAME` binds the GitHub Pages project to `dearsunday.moriclass.com`; DNS must point that subdomain to `PuongLee269.github.io` before HTTPS can be issued.
- After editing articles, run `python -B generate_articles.py` and then `python -B prepare_publish.py`. The second command sets canonical, social and article image URLs, refreshes the sitemap, and synchronizes `dist/`.
- Before reviewing or merging a local change, run `python -B check_seo.py` to verify canonicals, sitemap URLs, metadata, JSON-LD, local resources, and the synchronized `dist/` bundle.
- If changing the public hostname, update `BASE` in `prepare_publish.py` before running it.
- When replacing a room image, regenerate its responsive WebP variants and update the matching `srcset` width descriptors in `index.html` or `generate_articles.py`; width descriptors must match each file's actual pixel width. The publication script copies existing variants but does not generate them.
- Recheck the service windows and activity details with the Page before each substantive update.
- Keep the precise address private; it is shared by DearSunday after booking.
- Keep OAI-SearchBot allowed in `robots.txt` if ChatGPT Search visibility is desired.
- Submit the final sitemap in Google Search Console after the site is public and verified.

Google indexing is separate from deployment. Verify the URL-prefix property `https://dearsunday.moriclass.com/` in Search Console and submit `sitemap.xml`; neither ranking nor inclusion is guaranteed.

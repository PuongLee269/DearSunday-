# DearSunday Journal

Static Vietnamese blog for DearSunday private homestay. The site is focused on helpful, original guides for couples, Thanh Xuân and Hà Nội; the exact accommodation address is not published.

## Files

- `index.html`: journal home and article index
- `about.html`: verified DearSunday overview and current service windows
- `blog/`: six search-focused guides with distinct optimized room images
- `images/`: WebP room photographs, oriented from the source image metadata
- `generate_articles.py`: regenerates the six article pages
- `dist/`: static deployment package for Codex Sites and GitHub Pages

## Publishing

- Public URL: https://puonglee269.github.io/DearSunday-/
- GitHub Pages publishes `main` from the repository root.
- After editing articles, run `python -B generate_articles.py` and then `python -B prepare_publish.py`. The second command sets canonical, social and article image URLs, refreshes the sitemap, and synchronizes `dist/`.
- Before reviewing or merging a local change, run `python -B check_seo.py` to verify page canonicals against both sitemaps, local links/images, JSON-LD, and the synchronized `dist/` bundle.
- If changing the public hostname, update `BASE` in `prepare_publish.py` before running it.
- Recheck the service windows and activity details with the Page before each substantive update.
- Keep the precise address private; it is shared by DearSunday after booking.
- Keep OAI-SearchBot allowed in `robots.txt` if ChatGPT Search visibility is desired.
- Submit the final sitemap in Google Search Console after the site is public and verified.

Google indexing is separate from deployment. Verify the URL-prefix property in Search Console and submit `sitemap.xml`; neither ranking nor inclusion is guaranteed. On a GitHub project site, crawler rules are controlled by the domain-root robots.txt; the project-local robots.txt is included for migration to a dedicated domain.

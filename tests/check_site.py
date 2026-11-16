#!/usr/bin/env python3
"""Dependency-free checks of a built Nortica site (no external requests)."""
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value and name in {"href", "src"}:
                self.links.append(value)


def check(site):
    site = site.resolve()
    errors = []
    pages = list(site.rglob("*.html"))
    if not pages:
        errors.append("No built HTML pages found")
    for page in pages:
        text = page.read_text()
        for legacy in ("foelkdavid/", "docs.debian.foelk.com", "debianzfs-live", "DebianZFS-Install"):
            if legacy.lower() in text.lower():
                errors.append(f"{page.relative_to(site)}: obsolete reference {legacy}")
        if "theme-preview" in text or "nortica-palette-preview" in text:
            errors.append(f"{page.relative_to(site)}: temporary palette selector must not be published")
        parser = Links()
        parser.feed(text)
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path:
                continue
            target = ((site / unquote(url.path).lstrip("/")) if url.path.startswith("/")
                      else (page.parent / unquote(url.path))).resolve()
            if not target.is_relative_to(site) or not target.exists():
                errors.append(f"{page.relative_to(site)}: missing local target {link}")
    for asset in ("media/nortica-horizontal.png", "media/nortica-symbol.png", "media/favicon-32.png"):
        if not (site / asset).is_file():
            errors.append(f"Missing brand asset: {asset}")
    home = (site / "index.html").read_text() if (site / "index.html").exists() else ""
    if "nortica-banner" in home or "media/nortica-horizontal.png" in home:
        errors.append("Home page must not include the large logo/banner")
    for expected in ("https://docs.nortica.org/", "media/nortica-symbol.png", "Nortica-Linux/nortica.org"):
        if expected not in home:
            errors.append(f"Home page missing {expected}")
    for asset in ("theme-preview.css", "theme-preview.js"):
        if (site / "assets" / asset).exists():
            errors.append(f"Temporary palette asset must not be published: {asset}")
    if list(site.rglob(".git")):
        errors.append("Git metadata must never be published")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(pages)} HTML pages: local links, branding, canonical URL and media OK")


if __name__ == "__main__":
    check(Path(sys.argv[1] if len(sys.argv) > 1 else "site"))

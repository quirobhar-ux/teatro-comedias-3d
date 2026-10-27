#!/usr/bin/env python3
"""Ensambla el HTML final a partir de las fuentes en src/."""
from pathlib import Path

root = Path(__file__).parent
src = root / "src"

parts = "".join(
    (src / name).read_text(encoding="utf-8")
    for name in ("body-1.html", "body-2.html", "body-3.html", "body-4.html", "body-5.html")
)
css = (src / "styles.css").read_text(encoding="utf-8")
js = (src / "app.js").read_text(encoding="utf-8")

html = parts.replace("/*__CSS__*/", css).replace("/*__JS__*/", js)
out = root / "teatro-barroco-unidades.html"
out.write_text(html, encoding="utf-8")
print(f"OK  {out.name}  {len(html):,} chars  ({len(html)/1024:.1f} KB)")

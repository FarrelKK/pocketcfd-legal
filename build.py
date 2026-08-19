#!/usr/bin/env python3
"""Turn the markdown legal documents into the static pages you publish.

  python3 build.py

Reads privacy-policy.md and terms-and-conditions.md from this folder, strips the
"BEFORE YOU PUBLISH" reminder box, and writes privacy.html / terms.html.
Any remaining [PLACEHOLDER] is highlighted in red so it cannot ship unnoticed.
"""
import re, sys, pathlib, markdown

HERE = pathlib.Path(__file__).parent
SRC  = HERE          # sources live in this folder

CSS = """
:root{color-scheme:light dark}
*{box-sizing:border-box}
body{margin:0;padding:32px 20px 72px;font:400 16px/1.65 -apple-system,BlinkMacSystemFont,
  "Segoe UI",Inter,Roboto,system-ui,sans-serif;background:#fbfbfd;color:#1c1f26}
main{max-width:720px;margin:0 auto}
h1{font-size:30px;line-height:1.2;letter-spacing:-.02em;margin:0 0 6px}
h2{font-size:19px;margin:34px 0 10px;letter-spacing:-.01em;padding-top:14px;
  border-top:1px solid #e6e8ee}
h2:first-of-type{border-top:0;padding-top:0}
h3{font-size:16px;margin:22px 0 8px}
p,li{color:#31363f}
a{color:#0b62d6}
code{background:#eef0f5;padding:1px 5px;border-radius:5px;font-size:14px}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:15px;display:block;overflow-x:auto}
th,td{border:1px solid #e2e5ec;padding:8px 10px;text-align:left;vertical-align:top}
th{background:#f2f4f8;font-weight:650}
blockquote{margin:16px 0;padding:12px 16px;border-left:3px solid #c9cedb;background:#f4f6fa;
  border-radius:0 8px 8px 0}
hr{border:0;border-top:1px solid #e6e8ee;margin:30px 0}
.ph{background:#ffe1e1;color:#a01414;padding:1px 5px;border-radius:5px;font-weight:600}
.nav{font-size:14px;margin-bottom:26px}
.nav a{margin-right:16px;text-decoration:none}
footer{margin-top:44px;padding-top:16px;border-top:1px solid #e6e8ee;font-size:13px;color:#6b7280}
@media (prefers-color-scheme:dark){
  body{background:#0f1218;color:#e6e9f0}
  p,li{color:#c7cdd8} h2{border-top-color:#242a36}
  code{background:#1b2130} th{background:#161c28} th,td{border-color:#242a36}
  blockquote{background:#151b26;border-left-color:#39425a}
  a{color:#6cb2ff} hr,footer{border-top-color:#242a36}
  .ph{background:#3a1414;color:#ff9a9a}
}
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{title}">
<style>{css}</style>
</head>
<body>
<main>
<div class="nav"><a href="./">Home</a><a href="./privacy.html">Privacy policy</a><a href="./terms.html">Terms</a></div>
{body}
<footer>{footer}</footer>
</main>
</body>
</html>
"""

def convert(md_path, title, out_name, footer):
    md = pathlib.Path(md_path).read_text(encoding="utf-8")
    # drop the "BEFORE YOU PUBLISH" reminder block (the leading > quote)
    md = re.sub(r"^> .*?(?:\n>.*)*\n\n", "", md, count=1, flags=re.M)
    html = markdown.markdown(md, extensions=["tables", "sane_lists"])
    # make unfilled placeholders impossible to miss
    html = re.sub(r"\[([A-Z][A-Z \./]{2,})\]", r'<span class="ph">[\1]</span>', html)
    out = PAGE.format(title=title, css=CSS, body=html, footer=footer)
    (HERE / out_name).write_text(out, encoding="utf-8")
    left = out.count('class="ph"')
    print(f"  {out_name:14} {len(out)//1024} KB" + (f"   ⚠ {left} placeholder(s) still to fill" if left else "   ✓ no placeholders"))

if __name__ == "__main__":
    print("building:")
    foot = 'Pocket CFD · <a href="mailto:you@example.com">you@example.com</a>'
    convert(SRC/"privacy-policy.md",       "Privacy Policy — Pocket CFD",       "privacy.html", foot)
    convert(SRC/"terms-and-conditions.md", "Terms and Conditions — Pocket CFD", "terms.html",   foot)
    print("done. Commit this folder and enable GitHub Pages.")

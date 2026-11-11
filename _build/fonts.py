"""Self-hosted web fonts. Run after editing Chinese text (no dependencies):

    python3 _build/pages.py && python3 _build/fonts.py

- Bricolage Grotesque (weight 400–800) and Hanken Grotesk (400–700): Google's Latin subset
- Noto Sans TC 400 and 700: only the Chinese characters used on the site (Google Fonts `text=` subsetting)
"""
import glob
import html
import json
import os
import re
import urllib.parse
import urllib.request

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
OUT = os.path.join(ROOT, "assets", "fonts")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
API = "https://fonts.googleapis.com/css2?"


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()


def latin_src(css):
    for comment, block in re.findall(r"/\* ([\w-]+) \*/\s*@font-face \{(.*?)\}", css, re.S):
        if comment == "latin":
            return re.search(r"url\((.*?)\)", block).group(1)
    raise SystemExit("latin block not found")


def save(name, data):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name + ".woff2"), "wb") as f:
        f.write(data)
    print(f"{name}.woff2  {len(data) // 1024} KB")


def site_cjk():
    chars = set()
    for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        text = html.unescape(open(f, encoding="utf-8").read())  # includes the JS strings in window.IQTI
        chars.update(ch for ch in text if ord(ch) > 0x2E7F)
    chars.update("，。：；！？（）「」、·…")
    return "".join(sorted(chars))


if __name__ == "__main__":
    save("bricolage", get(latin_src(get(API + "family=Bricolage+Grotesque:wght@400..800&display=swap").decode())))
    save("hanken", get(latin_src(get(API + "family=Hanken+Grotesk:wght@400..700&display=swap").decode())))
    text = site_cjk()
    for w in (400, 700):
        css = get(API + f"family=Noto+Sans+TC:wght@{w}&display=swap&text=" + urllib.parse.quote(text)).decode()
        save(f"noto-sans-tc-{w}", get(re.search(r"url\((.*?)\)", css).group(1)))
    print(len(text), "Chinese characters")

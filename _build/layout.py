"""Shared page shell, header, footer, contact details and UI strings for both languages."""
import hashlib
import json
import os
import re

LANGS = {
    "en": {"dir": "", "html": "en-GB", "label": "EN", "name": "English"},
    "zh": {"dir": "zh/", "html": "zh-Hant", "label": "中文", "name": "繁體中文"},
}

SITE = "https://www.iqtiaccountants.co.uk/"
PHONE_DISPLAY = "07305 084561"
PHONE_INTL = "+44 7305 084561"
PHONE_TEL = "+447305084561"
WHATSAPP = "https://wa.me/447305084561"
EMAIL = "info@iqtiaccountants.co.uk"
EMAIL_DISPLAY = "info@IQTiAccountants.co.uk"
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=128+City+Road+London+EC1V+2NX"


def L(en, zh):
    return {"en": en, "zh": zh}


def r(x, lang):
    return x[lang] if isinstance(x, dict) else x


NAV = [
    ("services.html", L("Services", "服務")),
    ("fees.html", L("Fees", "收費")),
    ("guides.html", L("Tax guides", "稅務指南")),
    ("about.html", L("About", "關於我們")),
    ("contact.html", L("Contact", "聯絡")),
]

ADDRESS = L(["128 City Road", "London EC1V 2NX", "United Kingdom"],
            ["128 City Road", "London EC1V 2NX", "英國倫敦"])

UI = {
    "skip": L("Skip to content", "跳至正文"),
    "menu": L("Menu", "選單"),
    "close": L("Close", "關閉"),
    "call": L("Call", "致電"),
    "whatsapp": L("WhatsApp", "WhatsApp"),
    "email": L("Email", "電郵"),
    "quote": L("Get a quote", "免費報價"),
    "office": L("Office", "辦事處"),
    "pages": L("Pages", "頁面"),
    "contact": L("Contact", "聯絡方式"),
    "language": L("Language", "語言"),
    "legal": L("Privacy &amp; accessibility", "私隱及無障礙聲明"),
    "meet": L("Meetings by appointment,<br>in person or online", "會面需預約，<br>可親身或網上進行"),
    "footer_q": L("Talk to an accountant<br>in your language.", "用您熟悉的語言<br>與會計師傾談。"),
    "footer_lead": L("A free, no-obligation chat — in English, Cantonese or Mandarin. We’ll send a fixed quote afterwards.",
                     "免費、無責任的初步諮詢，可用英語、粵語或普通話。之後我們會提供固定收費報價。"),
    "wechat": L("WhatsApp / WeChat", "WhatsApp / 微信"),
    "reg": L("IQTi Limited, trading as IQTi Accountants", "IQTi Limited（IQTi 會計師事務所）"),
    "top": L("Back to top", "返回頂部"),
    "concept": L("Concept", "概念"),
    "concept_long": L('Redesign concept. Not the <a href="https://www.iqtiaccountants.co.uk/" target="_blank" rel="noopener">official IQTi Accountants website</a>.',
                      '概念設計展示，並非 <a href="https://www.iqtiaccountants.co.uk/" target="_blank" rel="noopener">IQTi 會計師事務所官方網站</a>。'),
    "concept_by": L("Designed by ", "設計："),
    "concept_note": L("Unofficial redesign concept by", "非官方概念設計："),
}

# Strings main.js needs at runtime
JS_STRINGS = {
    "en": {
        "perMonth": "/ month", "perYear": "a year", "pickOne": "Tick a service to see an estimate",
        "approx": "Typical fixed fee", "services": "services",
        "mtd": {
            "empty": "Enter your income to check",
            "in26": ["You’re in MTD now", "Your qualifying income is over £50,000, so Making Tax Digital for Income Tax applies from 6 April 2026. Your first quarterly update was due by 7 August 2026."],
            "in27": ["You join on 6 April 2027", "Qualifying income over £30,000 means MTD for Income Tax from 6 April 2027, based on your 2025/26 tax return."],
            "in28": ["You join on 6 April 2028", "Qualifying income over £20,000 means MTD for Income Tax from 6 April 2028, based on your 2026/27 tax return."],
            "out": ["Not required yet", "Below £20,000 you are not yet required to join. Keep an eye on it if your income grows — we can set you up early on a voluntary basis."],
        },
        "sdlt": {"total": "Stamp Duty to pay", "eff": "Effective rate", "band": "Band", "rate": "Rate", "tax": "Tax",
                 "upTo": "Up to", "above": "Above", "ftbOver": "Over £500,000: first-time buyer relief doesn’t apply, so standard rates are used."},
        "form": {"subject": "Quote request", "name": "Name", "email": "Email", "phone": "Phone", "type": "Business type",
                 "turnover": "Annual turnover", "vat": "VAT returns", "payroll": "Payroll", "books": "Bookkeeping",
                 "msg": "Message", "lang": "Preferred language", "hello": "Hello IQTi, I’d like a quote.",
                 "missing": "Please fill in the highlighted fields."},
    },
    "zh": {
        "perMonth": "/ 月", "perYear": "每年", "pickOne": "請剔選服務以查看估算",
        "approx": "一般固定收費", "services": "項服務",
        "mtd": {
            "empty": "請輸入收入以查看",
            "in26": ["您已須遵行 MTD", "您的合資格收入超過 £50,000，自 2026 年 4 月 6 日起須遵行所得稅數碼報稅（MTD）。首份季度申報已於 2026 年 8 月 7 日到期。"],
            "in27": ["2027 年 4 月 6 日起適用", "合資格收入超過 £30,000，將根據 2025/26 年度報稅表，自 2027 年 4 月 6 日起須遵行 MTD。"],
            "in28": ["2028 年 4 月 6 日起適用", "合資格收入超過 £20,000，將根據 2026/27 年度報稅表，自 2028 年 4 月 6 日起須遵行 MTD。"],
            "out": ["暫時無須加入", "收入低於 £20,000 暫時無須加入。如收入增加請留意，我們亦可協助您提早自願加入。"],
        },
        "sdlt": {"total": "應繳印花稅", "eff": "實際稅率", "band": "稅階", "rate": "稅率", "tax": "稅款",
                 "upTo": "不超過", "above": "超過", "ftbOver": "樓價超過 £500,000，不適用首次置業寬減，按標準稅率計算。"},
        "form": {"subject": "報價查詢", "name": "姓名", "email": "電郵", "phone": "電話", "type": "業務類型",
                 "turnover": "年營業額", "vat": "增值稅申報", "payroll": "薪酬管理", "books": "記帳",
                 "msg": "訊息", "lang": "希望使用的語言", "hello": "您好 IQTi，我想查詢報價。",
                 "missing": "請填寫已標示的欄位。"},
    },
}

ICON = {
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19.5 5.3 16A8 8 0 1 1 8 18.7z"/><path d="M9 10.5h.01M12 10.5h.01M15 10.5h.01"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "arrow-ne": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
    "plus": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>',
}

# The IQTi mark, redrawn from the original logo: a "Q" ring holding a small bar chart, with a tail and a dot.
MARK_SVG = """<svg class="mark" viewBox="0 0 40 40" aria-hidden="true">
  <circle class="mark-ring" cx="18" cy="19" r="13.5"/>
  <path class="mark-bars" d="M12.5 24v-5M16.5 24v-9M20.5 24v-11M24.5 24v-7"/>
  <path class="mark-tail" d="m25.5 27.5 7 7"/>
  <circle class="mark-dot" cx="34" cy="6" r="2.2"/>
</svg>"""


def lang_switch(lang, page):
    prefix = "../" if LANGS[lang]["dir"] else ""
    items = []
    for code, meta in LANGS.items():
        href = prefix + meta["dir"] + (page if page != "index.html" else "")
        if not href:
            href = "./"
        cur = ' aria-current="true"' if code == lang else ""
        items.append(f'<a href="{href}" lang="{meta["html"]}" hreflang="{meta["html"]}"{cur}>{meta["label"]}</a>')
    return '<div class="lang" role="group" aria-label="Language / 語言">' + "".join(items) + "</div>"


_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ver(rel):
    with open(os.path.join(_ROOT, "assets", rel), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


def asset(lang):
    return ("../" if LANGS[lang]["dir"] else "") + "assets/"


def brand_block(lang):
    sub = "Accountants" if lang == "en" else "會計師事務所"
    label = "IQTi Accountants — home" if lang == "en" else "IQTi 會計師事務所 — 主頁"
    return f"""<a class="brand" href="./" aria-label="{label}">
      {MARK_SVG}
      <span class="brand-text"><span class="brand-name">IQT<i>i</i></span><span class="brand-sub">{sub}</span></span>
    </a>"""


def header(lang, page):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{href}"{cur if href == page else ""}>{r(label, lang)}</a>' for href, label in NAV)
    big = "".join(f'<li><a href="{href}"{cur if href == page else ""}>{r(label, lang)}</a></li>' for href, label in NAV)
    return f"""<a class="skip" href="#main">{r(UI['skip'], lang)}</a>
<div class="concept-bar" role="note">
  <div class="wrap concept-inner">
    <p><span class="concept-tag">{r(UI['concept'], lang)}</span><span class="concept-long">{r(UI['concept_long'], lang)}</span></p>
    <a href="https://ux-circles.com/web" target="_blank" rel="noopener"><span class="concept-by">{r(UI['concept_by'], lang)}</span><strong>UX CIRCLES</strong> {ICON['arrow-ne']}</a>
  </div>
</div>
<header class="site-header" data-header>
  <div class="wrap header-inner">
    {brand_block(lang)}
    <nav class="main-nav" aria-label="{'Main' if lang == 'en' else '主選單'}">{nav}</nav>
    {lang_switch(lang, page)}
    <a class="btn btn-blue header-cta" href="contact.html#quote">{r(UI['quote'], lang)}</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="menu-lines"><span></span><span></span></span><span class="sr">{r(UI['menu'], lang)}</span></button>
  </div>
</header>
<div class="menu" id="menu" hidden>
  <div class="wrap menu-inner">
    <ul class="menu-links">{big}</ul>
    <div class="menu-foot">
      <a class="btn btn-blue" href="contact.html#quote">{r(UI['quote'], lang)} {ICON['arrow']}</a>
      <a href="{WHATSAPP}" target="_blank" rel="noopener">{ICON['chat']} WhatsApp {PHONE_DISPLAY}</a>
      <a href="mailto:{EMAIL}">{ICON['mail']} {EMAIL_DISPLAY}</a>
      {lang_switch(lang, page)}
    </div>
  </div>
</div>"""


def footer(lang, page):
    nav = "".join(f'<li><a href="{h}">{r(lbl, lang)}</a></li>' for h, lbl in NAV)
    nav += f'<li><a href="legal.html">{r(UI["legal"], lang)}</a></li>'
    addr = "<br>".join(r(ADDRESS, lang))
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <h2 class="footer-q">{r(UI['footer_q'], lang)}</h2>
        <p class="footer-lead">{r(UI['footer_lead'], lang)}</p>
      </div>
      <div class="footer-actions">
        <a class="btn btn-white" href="contact.html#quote">{r(UI['quote'], lang)} {ICON['arrow']}</a>
        <a class="btn btn-line-light" href="{WHATSAPP}" target="_blank" rel="noopener">{ICON['chat']} WhatsApp</a>
      </div>
    </div>
    <div class="footer-grid">
      <div class="f-brand">{brand_block(lang)}<p>{r(UI['reg'], lang)}</p></div>
      <div><h3 class="f-h">{r(UI['contact'], lang)}</h3>
        <p>{r(UI['wechat'], lang)}<br><a class="u" href="{WHATSAPP}" target="_blank" rel="noopener">{PHONE_INTL}</a></p>
        <p>{r(UI['email'], lang)}<br><a class="u" href="mailto:{EMAIL}">{EMAIL_DISPLAY}</a></p></div>
      <div><h3 class="f-h">{r(UI['office'], lang)}</h3><p>{addr}</p><p class="muted">{r(UI['meet'], lang)}</p></div>
      <div><h3 class="f-h">{r(UI['pages'], lang)}</h3><ul class="f-links">{nav}</ul></div>
    </div>
  </div>
  <div class="wrap footer-base">
    <span>© <span data-year>2026</span> IQTi Limited · <span class="concept-note">{r(UI['concept_note'], lang)} <a class="u" href="https://ux-circles.com/web" target="_blank" rel="noopener">UX CIRCLES</a></span></span>
    <span class="footer-base-r">{lang_switch(lang, page)}<a href="#main" class="u">{r(UI['top'], lang)} ↑</a></span>
  </div>
</footer>
<nav class="action-bar" aria-label="{'Quick contact' if lang == 'en' else '快速聯絡'}">
  <a href="tel:{PHONE_TEL}">{ICON['phone']}<span>{r(UI['call'], lang)}</span></a>
  <a href="{WHATSAPP}" target="_blank" rel="noopener">{ICON['chat']}<span>WhatsApp</span></a>
  <a class="ab-quote" href="contact.html#quote">{ICON['arrow']}<span>{r(UI['quote'], lang)}</span></a>
</nav>"""


PRELOAD = {"en": ["bricolage", "hanken"], "zh": ["bricolage", "noto-sans-tc-700"]}


def no_stops(html):
    """Headings carry no closing full stop (. or 。)."""
    return re.sub(r"[.。](\s*</h[1-3]>)", r"\1", html)


def page(lang, name, title, description, body, body_class=""):
    a = asset(lang)
    meta = LANGS[lang]
    path = "" if name == "index.html" else name
    alts = "\n".join(f'<link rel="alternate" hreflang="{m["html"]}" href="{SITE}{m["dir"]}{path}">' for m in LANGS.values())
    js = json.dumps(JS_STRINGS[lang], ensure_ascii=False)
    preloads = "\n".join(f'<link rel="preload" href="{a}fonts/{f}.woff2" as="font" type="font/woff2" crossorigin>'
                         for f in PRELOAD[lang])
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "AccountingService",
        "name": "IQTi Accountants", "alternateName": ["IQTi 會計師事務所", "IQTi Limited"],
        "url": SITE, "telephone": PHONE_INTL, "email": EMAIL,
        "address": {"@type": "PostalAddress", "streetAddress": "128 City Road",
                    "addressLocality": "London", "postalCode": "EC1V 2NX", "addressCountry": "GB"},
        "areaServed": "United Kingdom", "knowsLanguage": ["en", "yue", "cmn"],
    }, ensure_ascii=False)
    return no_stops(f"""<!doctype html>
<html lang="{meta['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE}{meta['dir']}{path}">
{alts}
<link rel="alternate" hreflang="x-default" href="{SITE}{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'en_GB' if lang == 'en' else 'zh_HK'}">
<meta name="theme-color" content="#f5f4f0">
<link rel="icon" href="{a}img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{a}img/apple-touch-icon.png">
{preloads}
<link rel="stylesheet" href="{a}css/style.css?v={ver("css/style.css")}">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{schema}</script>
</head>
<body class="lang-{lang} {body_class}">
{header(lang, name)}
<main id="main">
{body}
</main>
{footer(lang, name)}
<script>window.IQTI = {js};</script>
<script src="{a}js/main.js?v={ver("js/main.js")}" defer></script>
</body>
</html>
""")

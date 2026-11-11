"""Builds every page in both languages. Run: python3 _build/pages.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import (L, r, LANGS, ICON, UI, page, asset, PHONE_DISPLAY, PHONE_INTL, PHONE_TEL, WHATSAPP, EMAIL,
                    EMAIL_DISPLAY, ADDRESS, MAPS_URL)
from content import VALUES, STATS, GROUPS, WHY, FEES, STEPS, TEAM, TESTIMONIALS, FAQ

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def write(lang, name, html):
    path = os.path.join(ROOT, LANGS[lang]["dir"], name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def page_head(lang, eyebrow, title, lead, extra=""):
    return f"""<section class="page-head">
  <div class="wrap">
    <p class="eyebrow reveal">{r(eyebrow, lang)}</p>
    <h1 class="h-xl reveal">{r(title, lang)}</h1>
    <p class="lead reveal">{r(lead, lang)}</p>
    {extra}
  </div>
</section>"""


def cta_pair(lang, light=False):
    second = "btn-line-light" if light else "btn-line"
    return f"""<div class="cta-row">
      <a class="btn btn-blue" href="contact.html#quote">{r(L('Get a fixed quote', '索取固定報價'), lang)} {ICON['arrow']}</a>
      <a class="btn {second}" href="{WHATSAPP}" target="_blank" rel="noopener">{ICON['chat']} {r(L('WhatsApp / WeChat', 'WhatsApp / 微信'), lang)}</a>
    </div>"""


def values_band(lang):
    cells = "".join(f"""<li class="val reveal">
        <span class="val-letter" aria-hidden="true">{letter}</span>
        <h3>{r(name, lang)}</h3>
        <p>{r(text, lang)}</p>
      </li>""" for letter, name, text in VALUES)
    return f"""<section class="values" aria-labelledby="values-h">
  <div class="wrap">
    <div class="values-head">
      <p class="eyebrow eyebrow-light">{r(L('What the name stands for', '名字的意義'), lang)}</p>
      <h2 id="values-h" class="h-lg">{r(L('Four letters we hold ourselves to.', '四個字母，四個承諾。'), lang)}</h2>
    </div>
    <ul class="val-grid">{cells}</ul>
  </div>
</section>"""


def stats(lang):
    return '<dl class="stats">' + "".join(
        f'<div class="stat reveal"><dt>{r(label, lang)}</dt><dd>{num}</dd></div>' for num, label in STATS) + "</dl>"


def team_cards(lang, long=False):
    a = asset(lang)
    out = []
    for key, name, cred, role, bio in TEAM:
        bio_html = f"<p>{r(bio, lang)}</p>" if long else ""
        out.append(f"""<article class="person reveal">
        <div class="person-img"><img src="{a}img/{key}.webp" alt="{name}, {r(role, lang)}" width="760" height="1000" loading="lazy"></div>
        <div class="person-body">
          <h3>{name} <span class="cred">{r(cred, lang)}</span></h3>
          {bio_html}
        </div>
      </article>""")
    return "".join(out)


def testimonials(lang):
    cards = "".join(f"""<figure class="quote reveal">
        <blockquote><p>{r(text, lang)}</p></blockquote>
        <figcaption>{r(name, lang)}</figcaption>
      </figure>""" for name, text in TESTIMONIALS)
    return f"""<section class="section section-tint" aria-labelledby="t-h">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{r(L('Client testimonials', '客戶評價'), lang)}</p>
      <h2 id="t-h" class="h-lg">{r(L('In our clients’ words.', '客戶怎樣說。'), lang)}</h2>
    </div>
    <div class="quotes">{cards}</div>
  </div>
</section>"""


def faq(lang):
    items = "".join(f"""<details class="faq-item">
        <summary><span>{r(q, lang)}</span>{ICON['plus']}</summary>
        <p>{r(a, lang)}</p>
      </details>""" for q, a in FAQ)
    return f"""<section class="section" aria-labelledby="faq-h">
  <div class="wrap split-2">
    <div class="sec-head">
      <p class="eyebrow">{r(L('Questions', '常見問題'), lang)}</p>
      <h2 id="faq-h" class="h-lg">{r(L('Good to know.', '您可能想知道。'), lang)}</h2>
    </div>
    <div class="faq">{items}</div>
  </div>
</section>"""


def steps(lang):
    items = "".join(f"""<li class="step reveal"><span class="step-n">0{i}</span><h3>{r(t, lang)}</h3><p>{r(d, lang)}</p></li>"""
                    for i, (t, d) in enumerate(STEPS, 1))
    return f"""<section class="section" aria-labelledby="steps-h">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{r(L('How it works', '合作流程'), lang)}</p>
      <h2 id="steps-h" class="h-lg">{r(L('From first chat to filed return.', '由初步諮詢到完成申報。'), lang)}</h2>
    </div>
    <ol class="steps">{items}</ol>
  </div>
</section>"""


# ---------------------------------------------------------------- home
def home(lang):
    a = asset(lang)
    h1 = L('Accounts and tax, explained in <em>your</em> language.', '會計與稅務，<em>用您的語言</em>說清楚。')
    lead = L('IQTi Accountants is a multilingual firm in London. We look after Self Assessment, landlords, property investors and small companies — in English, Cantonese or Mandarin, for a fixed fee agreed up front.',
             'IQTi 會計師事務所是一家位於倫敦的多語言會計師事務所，為個人報稅、房東、物業投資者及小型公司提供服務。可用英語、粵語或普通話溝通，收費事先議定、固定不變。')
    group_cards = "".join(f"""<a class="g-card reveal" href="services.html#{g['id']}">
        <span class="g-num">0{i}</span>
        <h3>{r(g['title'], lang)}</h3>
        <p>{r(g['lead'], lang)}</p>
        <ul>{''.join(f'<li>{r(t, lang)}</li>' for _, t, _ in g['items'])}</ul>
        <span class="g-more">{r(L('See services', '查看服務'), lang)} {ICON['arrow']}</span>
      </a>""" for i, g in enumerate(GROUPS, 1))
    why = "".join(f"""<li class="why-item reveal"><span class="tick">{ICON['check']}</span><div><h3>{r(t, lang)}</h3><p>{r(d, lang)}</p></div></li>""" for t, d in WHY)
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="pill reveal"><span class="dot"></span>{r(L('FCCA-led accountants · City Road, London', 'FCCA 會計師主理 · 倫敦 City Road'), lang)}</p>
      <h1 class="h-hero reveal">{r(h1, lang)}</h1>
      <p class="lead reveal">{r(lead, lang)}</p>
      <div class="reveal">{cta_pair(lang)}</div>
      <ul class="lang-chips reveal" aria-label="{r(L('Languages we speak', '我們使用的語言'), lang)}">
        <li lang="en-GB">English</li><li lang="yue-Hant">廣東話</li><li lang="cmn-Hant">普通話</li>
      </ul>
    </div>
    <div class="hero-visual reveal" aria-hidden="true">
      <div class="hv-photo"><img src="{a}img/esther.webp" alt="" width="760" height="1000" fetchpriority="high"></div>
      <div class="bubble b1"><span class="b-lang">EN</span>How can we help with your tax return?</div>
      <div class="bubble b2" lang="yue-Hant"><span class="b-lang">粵</span>有咩可以幫到你？</div>
      <div class="bubble b3" lang="cmn-Hant"><span class="b-lang">普</span>請問有什麼可以幫您？</div>
      <div class="hv-tag"><strong>Esther</strong><span>FCCA · MBA</span></div>
      <div class="hv-fee"><span>{r(L('Self Assessment', '個人報稅'), lang)}</span><strong>£20<small>{r(L('/ month avg.', '/ 月（平均）'), lang)}</small></strong><em>{r(L('Fixed fee', '固定收費'), lang)}</em></div>
    </div>
  </div>
  <div class="wrap">{stats(lang)}</div>
</section>

{values_band(lang)}

<section class="section" aria-labelledby="svc-h">
  <div class="wrap">
    <div class="sec-head sec-head-row">
      <div>
        <p class="eyebrow">{r(L('Our services', '我們的服務'), lang)}</p>
        <h2 id="svc-h" class="h-lg">{r(L('Eleven services, one team that knows your file.', '十一項服務，同一團隊熟悉您的帳目。'), lang)}</h2>
      </div>
      <a class="link-arrow" href="services.html">{r(L('All services', '全部服務'), lang)} {ICON['arrow']}</a>
    </div>
    <div class="g-grid">{group_cards}</div>
  </div>
</section>

<section class="mtd-band" aria-labelledby="mtd-h">
  <div class="wrap mtd-inner reveal">
    <div>
      <p class="eyebrow">{r(L('Making Tax Digital for Income Tax', '所得稅數碼報稅（MTD）'), lang)}</p>
      <h2 id="mtd-h" class="h-md">{r(L('Quarterly updates started on 6 April 2026. Are you in?', '季度申報已於 2026 年 4 月 6 日開始。您需要加入嗎？'), lang)}</h2>
      <p>{r(L('Sole traders and landlords with income over £50,000 now report every quarter. The threshold drops to £30,000 in 2027 and £20,000 in 2028.', '收入超過 £50,000 的自僱人士及房東現須每季申報。門檻將於 2027 年降至 £30,000，2028 年降至 £20,000。'), lang)}</p>
    </div>
    <a class="btn btn-ink" href="guides.html#mtd">{r(L('Check in 10 seconds', '10 秒檢查'), lang)} {ICON['arrow']}</a>
  </div>
</section>

<section class="section" aria-labelledby="why-h">
  <div class="wrap split-2">
    <div class="sec-head sticky">
      <p class="eyebrow">{r(L('Why IQTi', '為什麼選擇 IQTi'), lang)}</p>
      <h2 id="why-h" class="h-lg">{r(L('An accountant you can actually talk to.', '一位真正能溝通的會計師。'), lang)}</h2>
      <div class="soft">
        <p>{r(L('We work in', '我們使用'), lang)}</p>
        <ul class="soft-list"><li>Xero</li><li>FreeAgent</li><li>Hammock</li></ul>
      </div>
    </div>
    <ul class="why">{why}</ul>
  </div>
</section>

<section class="section section-tint" aria-labelledby="team-h">
  <div class="wrap split-2 team-split">
    <div class="sec-head">
      <p class="eyebrow">{r(L('Meet the team', '認識我們的團隊'), lang)}</p>
      <h2 id="team-h" class="h-lg">{r(L('Small on purpose.', '小團隊，用心服務。'), lang)}</h2>
      <p class="lead-sm">{r(L('IQTi is a UK-based multilingual accounting firm. With a focus on accuracy, integrity and professionalism, we help clients reach their financial goals.', 'IQTi 是一家英國多語言會計師事務所，注重準確、誠信及專業，致力幫助客戶實現財務目標。'), lang)}</p>
      <a class="link-arrow" href="about.html">{r(L('About us', '關於我們'), lang)} {ICON['arrow']}</a>
    </div>
    <div class="team">{team_cards(lang)}</div>
  </div>
</section>

{testimonials(lang)}
{steps(lang)}
"""
    title = L("IQTi Accountants | Chinese-speaking accountants in London · 會計師", "IQTi 會計師事務所 | 倫敦中英雙語會計師")
    desc = L("Multilingual accountants in London. Self Assessment, landlord tax, company accounts, VAT, payroll and bookkeeping in English, Cantonese and Mandarin, for fixed fees.",
             "倫敦多語言會計師事務所，以英語、粵語及普通話提供個人報稅、房東稅務、公司帳目、增值稅、薪酬及理帳服務，收費固定。")
    write(lang, "index.html", page(lang, "index.html", r(title, lang), r(desc, lang), body, "home"))


# ---------------------------------------------------------------- services
def services(lang):
    blocks = []
    for i, g in enumerate(GROUPS, 1):
        items = "".join(f"""<li class="svc reveal" id="{sid}"><h3>{r(t, lang)}</h3><p>{r(d, lang)}</p></li>""" for sid, t, d in g["items"])
        blocks.append(f"""<section class="svc-group" id="{g['id']}" aria-labelledby="{g['id']}-h">
    <div class="svc-side">
      <span class="g-num">0{i}</span>
      <h2 id="{g['id']}-h" class="h-md">{r(g['title'], lang)}</h2>
      <p>{r(g['lead'], lang)}</p>
    </div>
    <ul class="svc-list">{items}</ul>
  </section>""")
    jump = "".join(f'<a href="#{g["id"]}">{r(g["title"], lang)}</a>' for g in GROUPS)
    body = page_head(lang, L("Services", "服務"),
                     L("Everything HMRC and Companies House expect, handled.", "稅局及 Companies House 的要求，一手包辦。"),
                     L("For sole traders, landlords, property investors and small limited companies. Pick one service or hand us the lot.",
                       "服務自僱人士、房東、物業投資者及小型有限公司。可選擇單項服務，或全部交給我們。"),
                     f'<nav class="jump reveal" aria-label="{r(L("On this page", "本頁內容"), lang)}">{jump}</nav>') + f"""
<div class="wrap svc-wrap">{''.join(blocks)}</div>
{steps(lang)}
<section class="section section-tint">
  <div class="wrap callout reveal">
    <div>
      <h2 class="h-md">{r(L('Fees are fixed and agreed before we start.', '收費固定，開始前議定。'), lang)}</h2>
      <p>{r(L('See typical prices and build an estimate for the services you need.', '查看一般收費，並為所需服務估算費用。'), lang)}</p>
    </div>
    <a class="btn btn-blue" href="fees.html">{r(L('See fees', '查看收費'), lang)} {ICON['arrow']}</a>
  </div>
</section>
{faq(lang)}
"""
    title = L("Services | IQTi Accountants", "服務 | IQTi 會計師事務所")
    desc = L("Self Assessment, landlord and non-resident landlord tax, Capital Gains Tax, company accounts, Corporation Tax, VAT, PAYE payroll, bookkeeping and company formation.",
             "個人報稅、房東及非居民房東稅務、資本利得稅、公司帳目、公司稅、增值稅、PAYE 薪酬、理帳及成立公司。")
    write(lang, "services.html", page(lang, "services.html", r(title, lang), r(desc, lang), body))


# ---------------------------------------------------------------- fees
def fees(lang):
    cards = "".join(f"""<li class="fee reveal">
        <h3>{r(name, lang)}</h3>
        <p class="fee-for">{r(who, lang)}</p>
        <p class="fee-price"><span class="cur">£</span>{price}<span class="per">{r(L('/ month avg.', '/ 月（平均）'), lang)}</span></p>
      </li>""" for key, price, name, who in FEES)
    opts = "".join(f"""<label class="est-opt">
          <input type="checkbox" name="svc" value="{price}" data-key="{key}">
          <span class="est-box">{ICON['check']}</span>
          <span class="est-name">{r(name, lang)}</span>
          <span class="est-price">£{price}</span>
        </label>""" for key, price, name, who in FEES)
    body = page_head(lang, L("Fees", "收費"),
                     L("Fixed fees. No surprises.", "固定收費，沒有意外。"),
                     L("Our fees depend on what your business needs and its turnover, and are always agreed in writing before we start. These are our average monthly fees.",
                       "收費視乎業務需要及營業額而定，並一定會在開始前以書面議定。以下為平均每月收費。")) + f"""
<section class="section section-flush">
  <div class="wrap">
    <ul class="fees">{cards}</ul>
  </div>
</section>

<section class="section section-tint" aria-labelledby="est-h">
  <div class="wrap estimator reveal" data-estimator>
    <div class="est-left">
      <p class="eyebrow">{r(L('Fee estimator', '收費估算'), lang)}</p>
      <h2 id="est-h" class="h-md">{r(L('What would my fee be?', '我的收費大約多少？'), lang)}</h2>
      <p>{r(L('Tick what you need for a rough monthly figure, based on our average fees.', '剔選所需服務，按平均收費估算每月費用。'), lang)}</p>
      <fieldset class="est-opts"><legend class="sr">{r(L('Services', '服務'), lang)}</legend>{opts}</fieldset>
    </div>
    <div class="est-result" aria-live="polite">
      <p class="est-label" data-est-label>{r(L('Tick a service to see an estimate', '請剔選服務以查看估算'), lang)}</p>
      <p class="est-total"><span class="cur">£</span><span data-est-total>0</span><span class="per">{r(L('/ month', '/ 月'), lang)}</span></p>
      <p class="est-year" data-est-year>&nbsp;</p>
      <p class="est-note">{r(L('An estimate only. Your actual fee is fixed after a free chat about your records and turnover.', '僅供參考。實際收費會在免費諮詢、了解您的帳目及營業額後確定。'), lang)}</p>
      <a class="btn btn-white" href="contact.html#quote" data-est-link>{r(L('Get my fixed quote', '索取固定報價'), lang)} {ICON['arrow']}</a>
    </div>
  </div>
</section>
{faq(lang)}
"""
    title = L("Fees | IQTi Accountants", "收費 | IQTi 會計師事務所")
    desc = L("Fixed accounting fees, agreed before we start. Self Assessment from £20 a month on average, company accounts and tax from £120.",
             "固定會計收費，事先議定。個人報稅平均每月 £20 起，公司帳目及稅表平均每月 £120。")
    write(lang, "fees.html", page(lang, "fees.html", r(title, lang), r(desc, lang), body))


# ---------------------------------------------------------------- guides
def guides(lang):
    sdlt_bands = [
        ("£0 – £125,000", "0%"), ("£125,001 – £250,000", "2%"), ("£250,001 – £925,000", "5%"),
        ("£925,001 – £1.5m", "10%"), (r(L("Over £1.5m", "超過 £1.5m"), lang), "12%"),
    ]
    band_rows = "".join(f"<tr><td>{b}</td><td>{p}</td></tr>" for b, p in sdlt_bands)
    body = page_head(lang, L("Tax guides", "稅務指南"),
                     L("Two changes worth knowing about.", "兩項值得留意的稅務變動。"),
                     L("Plain-language notes on recent UK tax changes, with quick calculators. General guidance only — talk to us about your own situation.",
                       "以淺白文字解釋近期英國稅務變動，並附簡易計算工具。內容僅供一般參考，個別情況請與我們商討。"),
                     f'<nav class="jump reveal" aria-label="{r(L("On this page", "本頁內容"), lang)}"><a href="#mtd">{r(L("Making Tax Digital", "數碼報稅 MTD"), lang)}</a><a href="#sdlt">{r(L("Stamp Duty", "印花稅"), lang)}</a></nav>') + f"""
<article class="section guide" id="mtd" aria-labelledby="mtd-title">
  <div class="wrap guide-grid">
    <div class="guide-body">
      <p class="eyebrow">{r(L('Updated August 2025', '2025 年 8 月更新'), lang)}</p>
      <h2 id="mtd-title" class="h-lg">{r(L('Making Tax Digital for Income Tax', '所得稅數碼報稅（MTD）'), lang)}</h2>
      <p>{r(L('Making Tax Digital (MTD) for Income Tax changes how sole traders and landlords report to HMRC. Instead of one tax return a year, you keep digital records in compatible software and send a short update every quarter, then a final declaration after the year ends.', '所得稅數碼報稅（MTD）改變了自僱人士及房東向稅局申報的方式。您須以兼容軟件保存數碼記錄，每季遞交簡短更新，並在年度結束後作最終申報，而非每年只交一次報稅表。'), lang)}</p>
      <h3>{r(L('Who has to join, and when', '誰需要加入？何時開始？'), lang)}</h3>
      <p>{r(L('It depends on your qualifying income: your total gross income from self-employment and property, before expenses.', '取決於您的「合資格收入」，即自僱及物業的總收入（未扣除開支）。'), lang)}</p>
      <table class="tbl">
        <thead><tr><th>{r(L('Qualifying income', '合資格收入'), lang)}</th><th>{r(L('MTD from', '開始日期'), lang)}</th></tr></thead>
        <tbody>
          <tr><td>{r(L('Over £50,000', '超過 £50,000'), lang)}</td><td>{r(L('6 April 2026', '2026 年 4 月 6 日'), lang)}</td></tr>
          <tr><td>{r(L('Over £30,000', '超過 £30,000'), lang)}</td><td>{r(L('6 April 2027', '2027 年 4 月 6 日'), lang)}</td></tr>
          <tr><td>{r(L('Over £20,000', '超過 £20,000'), lang)}</td><td>{r(L('6 April 2028', '2028 年 4 月 6 日'), lang)}</td></tr>
        </tbody>
      </table>
      <h3>{r(L('Quarterly deadlines', '季度申報限期'), lang)}</h3>
      <p>{r(L('Updates cover the quarters to 30 June, 30 September, 31 December and 31 March, and are due by 7 August, 7 November, 7 February and 7 May. The final declaration is due by 31 January, as now.', '季度截至 6 月 30 日、9 月 30 日、12 月 31 日及 3 月 31 日，須分別於 8 月 7 日、11 月 7 日、2 月 7 日及 5 月 7 日前遞交。最終申報限期與現時一樣，為 1 月 31 日。'), lang)}</p>
      <h3>{r(L('How we help', '我們如何協助'), lang)}</h3>
      <p>{r(L('We set you up in MTD-compatible software, keep the records with you, and file each quarterly update and the final declaration for you.', '我們為您設定兼容 MTD 的軟件，與您一起保存記錄，並代為遞交每季更新及最終申報。'), lang)}</p>
    </div>
    <aside class="tool reveal" data-mtd aria-labelledby="mtd-tool-h">
      <h3 id="mtd-tool-h">{r(L('Do I need to join?', '我需要加入嗎？'), lang)}</h3>
      <label for="mtd-income">{r(L('Gross income from self-employment and property, per year', '每年自僱及物業總收入'), lang)}</label>
      <div class="money"><span>£</span><input id="mtd-income" type="text" inputmode="numeric" autocomplete="off" placeholder="45,000"></div>
      <div class="tool-out" aria-live="polite">
        <p class="tool-big" data-mtd-title>{r(L('Enter your income to check', '請輸入收入以查看'), lang)}</p>
        <p data-mtd-text></p>
      </div>
    </aside>
  </div>
</article>

<article class="section section-tint guide" id="sdlt" aria-labelledby="sdlt-title">
  <div class="wrap guide-grid">
    <div class="guide-body">
      <p class="eyebrow">{r(L('Updated April 2025', '2025 年 4 月更新'), lang)}</p>
      <h2 id="sdlt-title" class="h-lg">{r(L('Stamp Duty Land Tax from 1 April 2025', '2025 年 4 月 1 日起的印花稅'), lang)}</h2>
      <p>{r(L('Temporary Stamp Duty reliefs ended on 31 March 2025. For residential purchases in England and Northern Ireland, the nil-rate band went back down from £250,000 to £125,000.', '臨時印花稅寬減已於 2025 年 3 月 31 日結束。在英格蘭及北愛爾蘭購買住宅物業，零稅率門檻由 £250,000 回落至 £125,000。'), lang)}</p>
      <table class="tbl">
        <thead><tr><th>{r(L('Portion of the price', '樓價部分'), lang)}</th><th>{r(L('Rate', '稅率'), lang)}</th></tr></thead>
        <tbody>{band_rows}</tbody>
      </table>
      <ul class="bullets">
        <li>{r(L('<strong>First-time buyers</strong> pay nothing up to £300,000 and 5% on £300,001–£500,000. Above £500,000 the relief doesn’t apply.', '<strong>首次置業人士</strong>：£300,000 以下免稅，£300,001 至 £500,000 的部分徵 5%。樓價超過 £500,000 則不適用寬減。'), lang)}</li>
        <li>{r(L('<strong>Additional properties</strong> (buy-to-let, second homes) pay a further 5% on every band.', '<strong>額外物業</strong>（出租物業、第二住所）每個稅階另加 5%。'), lang)}</li>
        <li>{r(L('<strong>Non-UK residents</strong> pay a further 2% on every band.', '<strong>非英國居民</strong>每個稅階另加 2%。'), lang)}</li>
      </ul>
    </div>
    <aside class="tool reveal" data-sdlt aria-labelledby="sdlt-tool-h">
      <h3 id="sdlt-tool-h">{r(L('Stamp Duty calculator', '印花稅計算機'), lang)}</h3>
      <label for="sdlt-price">{r(L('Purchase price', '樓價'), lang)}</label>
      <div class="money"><span>£</span><input id="sdlt-price" type="text" inputmode="numeric" autocomplete="off" placeholder="450,000"></div>
      <fieldset class="seg">
        <legend>{r(L('Buyer', '買家類別'), lang)}</legend>
        <label><input type="radio" name="buyer" value="std" checked><span>{r(L('Home mover', '換樓'), lang)}</span></label>
        <label><input type="radio" name="buyer" value="ftb"><span>{r(L('First-time buyer', '首次置業'), lang)}</span></label>
        <label><input type="radio" name="buyer" value="add"><span>{r(L('Additional property', '額外物業'), lang)}</span></label>
      </fieldset>
      <label class="check"><input type="checkbox" name="nonres"><span class="est-box">{ICON['check']}</span>{r(L('I’m not a UK resident', '我不是英國居民'), lang)}</label>
      <div class="tool-out" aria-live="polite">
        <p class="tool-label">{r(L('Stamp Duty to pay', '應繳印花稅'), lang)}</p>
        <p class="tool-big" data-sdlt-total>£0</p>
        <p class="tool-sub" data-sdlt-eff></p>
        <table class="tbl tbl-sm" data-sdlt-table hidden></table>
        <p class="tool-note" data-sdlt-note></p>
      </div>
      <p class="tool-fine">{r(L('Residential property in England and Northern Ireland. An estimate, not tax advice.', '適用於英格蘭及北愛爾蘭住宅物業。僅供估算，並非稅務意見。'), lang)}</p>
    </aside>
  </div>
</article>
"""
    title = L("Tax guides: MTD for Income Tax and Stamp Duty | IQTi Accountants", "稅務指南：所得稅數碼報稅及印花稅 | IQTi 會計師事務所")
    desc = L("Check if Making Tax Digital for Income Tax applies to you and calculate Stamp Duty Land Tax under the rates from 1 April 2025.",
             "查看您是否須遵行所得稅數碼報稅（MTD），並按 2025 年 4 月 1 日起的稅率計算印花稅。")
    write(lang, "guides.html", page(lang, "guides.html", r(title, lang), r(desc, lang), body))


# ---------------------------------------------------------------- about
def about(lang):
    a = asset(lang)
    langs = [
        ("English", L("For HMRC, Companies House and your bank.", "與稅局、Companies House 及銀行溝通。")),
        ("廣東話", L("Cantonese, for clients from Hong Kong, Guangdong and beyond.", "服務來自香港、廣東及各地的客戶。")),
        ("普通話", L("Mandarin, for clients from mainland China, Taiwan and Singapore.", "服務來自中國內地、台灣及新加坡的客戶。")),
    ]
    lang_cards = "".join(f'<li class="lc reveal"><span class="lc-name">{n}</span><p>{r(d, lang)}</p></li>' for n, d in langs)
    body = page_head(lang, L("About us", "關於我們"),
                     L("A London firm that speaks three languages.", "一家說三種語言的倫敦會計師事務所。"),
                     L("IQTi Accountants is a UK-based multilingual accounting firm. We provide accounting and bookkeeping for sole traders, property investors and small businesses — with a focus on accuracy, integrity and professionalism.",
                       "IQTi 會計師事務所是一家英國多語言會計師事務所，為自僱人士、物業投資者及小型企業提供會計及理帳服務，注重準確、誠信及專業。")) + f"""
<section class="section section-flush">
  <div class="wrap about-photo reveal">
    <img src="{a}img/building.webp" alt="" width="1400" height="731" loading="lazy">
    <div class="about-photo-card">
      {stats(lang)}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="lang-h">
  <div class="wrap split-2">
    <div class="sec-head">
      <p class="eyebrow">{r(L('Multilingual expertise', '多語言專業'), lang)}</p>
      <h2 id="lang-h" class="h-lg">{r(L('Tax is hard enough in one language.', '稅務本已複雜，何況語言不通。'), lang)}</h2>
      <p class="lead-sm">{r(L('Our accountants speak English and Chinese, with strong multicultural experience. Many of our clients run businesses or own property in the UK while family, income or investments sit elsewhere — we understand both sides.', '我們的會計師能說英語及中文，並擁有豐富的多元文化經驗。不少客戶在英國經營業務或擁有物業，而家人、收入或投資則在其他地方——我們明白兩邊的情況。'), lang)}</p>
    </div>
    <ul class="lang-cards">{lang_cards}</ul>
  </div>
</section>

{values_band(lang)}

<section class="section" aria-labelledby="team-h">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{r(L('Our team', '我們的團隊'), lang)}</p>
      <h2 id="team-h" class="h-lg">{r(L('The people on your file.', '負責您帳目的團隊。'), lang)}</h2>
    </div>
    <div class="team team-long">{team_cards(lang, long=True)}</div>
  </div>
</section>

{testimonials(lang)}
"""
    title = L("About | IQTi Accountants", "關於我們 | IQTi 會計師事務所")
    desc = L("IQTi Accountants is a multilingual accounting firm in London, led by an FCCA accountant, working in English, Cantonese and Mandarin.",
             "IQTi 會計師事務所是一家倫敦多語言會計師事務所，由 FCCA 會計師主理，以英語、粵語及普通話服務客戶。")
    write(lang, "about.html", page(lang, "about.html", r(title, lang), r(desc, lang), body))


# ---------------------------------------------------------------- contact
def contact(lang):
    def yn(name, label, required=True):
        req = " required" if required else ""
        star = ' <span class="req" aria-hidden="true">*</span>' if required else ""
        return f"""<fieldset class="field yn"{' data-required' if required else ''}>
          <legend>{r(label, lang)}{star}</legend>
          <div class="seg seg-sm">
            <label><input type="radio" name="{name}" value="yes"{req}><span>{r(L('Yes', '是'), lang)}</span></label>
            <label><input type="radio" name="{name}" value="no"><span>{r(L('No', '否'), lang)}</span></label>
          </div>
        </fieldset>"""

    star = ' <span class="req" aria-hidden="true">*</span>'
    types = [L("Sole trader", "個體經營者"), L("Limited company", "有限公司"), L("Partnership / LLP", "合夥 / 有限責任合夥"),
             L("Landlord", "房東"), L("Not sure yet", "未確定")]
    type_opts = "".join(f'<option>{r(t, lang)}</option>' for t in types)
    pref = [("English", "English"), ("廣東話", "廣東話"), ("普通話", "普通話")]
    pref_opts = "".join(f'<label><input type="radio" name="pref" value="{v}"{" checked" if i == (0 if lang == "en" else 1) else ""}><span>{t}</span></label>' for i, (v, t) in enumerate(pref))
    addr = "<br>".join(r(ADDRESS, lang))
    body = page_head(lang, L("Contact", "聯絡我們"),
                     L("Reach out. Get a fixed quote.", "立即查詢，索取固定報價。"),
                     L("Start with a free, no-obligation 15-minute chat, or send us the details below and we’ll come back with a quote.",
                       "可先預約 15 分鐘免費、無責任諮詢，或填寫以下資料，我們會回覆報價。")) + f"""
<section class="section section-flush">
  <div class="wrap contact-grid">
    <aside class="contact-cards">
      <a class="c-card c-card-wa reveal" href="{WHATSAPP}" target="_blank" rel="noopener">
        <span class="c-ic">{ICON['chat']}</span>
        <span class="c-t">{r(L('WhatsApp / WeChat', 'WhatsApp / 微信'), lang)}</span>
        <span class="c-v">{PHONE_INTL}</span>
        <span class="c-s">{r(L('Book your free 15-minute chat', '預約 15 分鐘免費諮詢'), lang)} {ICON['arrow']}</span>
      </a>
      <a class="c-card reveal" href="tel:{PHONE_TEL}">
        <span class="c-ic">{ICON['phone']}</span>
        <span class="c-t">{r(L('Phone', '電話'), lang)}</span>
        <span class="c-v">{PHONE_DISPLAY}</span>
      </a>
      <a class="c-card reveal" href="mailto:{EMAIL}">
        <span class="c-ic">{ICON['mail']}</span>
        <span class="c-t">{r(L('Email', '電郵'), lang)}</span>
        <span class="c-v">{EMAIL_DISPLAY}</span>
      </a>
      <a class="c-card reveal" href="{MAPS_URL}" target="_blank" rel="noopener">
        <span class="c-ic">{ICON['pin']}</span>
        <span class="c-t">{r(L('Office', '辦事處'), lang)}</span>
        <span class="c-v c-v-sm">{addr}</span>
        <span class="c-s">{r(L('Meetings by appointment, in person or online', '會面需預約，可親身或網上進行'), lang)}</span>
      </a>
    </aside>

    <form class="quote-form reveal" id="quote" data-quote novalidate>
      <h2 class="h-md">{r(L('Request a quote', '索取報價'), lang)}</h2>
      <p class="form-intro">{r(L('Takes about a minute. Choose how to send it at the end — WhatsApp or email.', '大約一分鐘即可完成，最後可選擇以 WhatsApp 或電郵發送。'), lang)}</p>
      <div class="row-2">
        <div class="field"><label for="f-first">{r(L('First name', '名字'), lang)}{star}</label><input id="f-first" name="first" autocomplete="given-name" required></div>
        <div class="field"><label for="f-last">{r(L('Last name', '姓氏'), lang)}{star}</label><input id="f-last" name="last" autocomplete="family-name" required></div>
      </div>
      <div class="row-2">
        <div class="field"><label for="f-email">{r(L('Email', '電郵'), lang)}{star}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-phone">{r(L('Phone', '電話'), lang)}{star}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
      </div>
      <div class="row-2">
        <div class="field"><label for="f-type">{r(L('Business type', '業務類型'), lang)}{star}</label>
          <select id="f-type" name="type" required><option value="">{r(L('Select…', '請選擇…'), lang)}</option>{type_opts}</select></div>
        <div class="field"><label for="f-turnover">{r(L('Annual turnover (£)', '年營業額（英鎊）'), lang)}{star}</label>
          <div class="money"><span>£</span><input id="f-turnover" name="turnover" inputmode="numeric" required></div></div>
      </div>
      <div class="row-3">
        {yn('vat', L('Need VAT returns?', '需要增值稅申報嗎？'))}
        {yn('payroll', L('Need payroll?', '需要薪酬管理嗎？'))}
        {yn('books', L('Need bookkeeping?', '需要我們記帳嗎？'), required=False)}
      </div>
      <fieldset class="field"><legend>{r(L('Preferred language', '希望使用的語言'), lang)}</legend><div class="seg seg-sm">{pref_opts}</div></fieldset>
      <div class="field"><label for="f-msg">{r(L('Anything else?', '其他查詢'), lang)}</label><textarea id="f-msg" name="msg" rows="4"></textarea></div>
      <p class="form-error" data-form-error role="alert" hidden></p>
      <div class="form-send">
        <button class="btn btn-blue" type="submit" value="wa">{ICON['chat']} {r(L('Send via WhatsApp', '經 WhatsApp 發送'), lang)}</button>
        <button class="btn btn-line" type="submit" value="mail">{ICON['mail']} {r(L('Send by email', '經電郵發送'), lang)}</button>
      </div>
      <p class="form-fine">{r(L('Nothing is stored on this website: your message opens in WhatsApp or your email app for you to send. See our <a class="u" href="legal.html">privacy notice</a>.', '本網站不會儲存任何資料：訊息會在 WhatsApp 或您的電郵程式中開啟，由您自行發送。請參閱我們的<a class="u" href="legal.html">私隱聲明</a>。'), lang)}</p>
    </form>
  </div>
</section>
{faq(lang)}
"""
    title = L("Contact & quote | IQTi Accountants", "聯絡及報價 | IQTi 會計師事務所")
    desc = L("Get a fixed accounting quote or book a free 15-minute chat by WhatsApp, WeChat, phone or email.",
             "透過 WhatsApp、微信、電話或電郵索取固定會計報價，或預約 15 分鐘免費諮詢。")
    write(lang, "contact.html", page(lang, "contact.html", r(title, lang), r(desc, lang), body))


# ---------------------------------------------------------------- legal
def legal(lang):
    sections = [
        (L("Privacy notice", "私隱聲明"), [
            L("IQTi Limited, trading as IQTi Accountants, of 128 City Road, London EC1V 2NX, is responsible for personal information you give us.",
              "IQTi Limited（IQTi 會計師事務所），地址為 128 City Road, London EC1V 2NX，負責處理您提供給我們的個人資料。"),
            L("<strong>This website.</strong> The site does not use cookies, analytics or a contact database. The quote form runs in your browser and opens a message in WhatsApp or your email app; nothing is sent until you send it yourself.",
              "<strong>本網站</strong>不使用 cookies、分析工具或聯絡資料庫。報價表格在您的瀏覽器中運作，並在 WhatsApp 或電郵程式中開啟訊息；在您自行發送前，不會傳送任何資料。"),
            L("<strong>What we use and why.</strong> When you contact us we use your name, contact details and the information you share to reply and prepare a quote. As clients, we hold the records we need to provide accounting and tax services and to meet our legal duties, including anti-money-laundering checks.",
              "<strong>我們使用的資料及原因。</strong>當您聯絡我們時，我們會使用您的姓名、聯絡資料及您提供的資訊來回覆及準備報價。成為客戶後，我們會保存提供會計及稅務服務、以及履行法律責任（包括反洗錢審查）所需的記錄。"),
            L("<strong>Sharing.</strong> We share information only with HMRC, Companies House and others where your instructions or the law require it, and with the software providers we use to do the work. We never sell personal data.",
              "<strong>資料分享。</strong>我們只會在您的指示或法律要求下，與稅局、Companies House 等機構分享資料，以及與我們工作所用的軟件供應商分享。我們絕不出售個人資料。"),
            L("<strong>Keeping records.</strong> Client records are kept for as long as the law requires — normally six years after our work ends.",
              "<strong>記錄保存。</strong>客戶記錄按法律要求保存，一般為服務結束後六年。"),
            L(f"<strong>Your rights.</strong> You can ask to see, correct or delete your information, or object to how we use it, by emailing <a class=\"u\" href=\"mailto:{EMAIL}\">{EMAIL_DISPLAY}</a>. You can also complain to the Information Commissioner’s Office at ico.org.uk.",
              f"<strong>您的權利。</strong>您可以電郵至 <a class=\"u\" href=\"mailto:{EMAIL}\">{EMAIL_DISPLAY}</a>，要求查閱、更正或刪除您的資料，或反對我們使用資料的方式。您亦可向資訊專員辦公室（ico.org.uk）投訴。"),
        ]),
        (L("Accessibility statement", "無障礙聲明"), [
            L("We want everyone to be able to use this website. It is built to meet WCAG 2.2 level AA: it works with a keyboard and screen readers, text can be resized to 200%, colours meet contrast guidelines, and animation is switched off if your device asks for reduced motion.",
              "我們希望每個人都能使用本網站。網站按 WCAG 2.2 AA 級標準建立：支援鍵盤及螢幕閱讀器操作、文字可放大至 200%、顏色符合對比度指引，如裝置設定減少動態效果，動畫會自動關閉。"),
            L(f"Every page is available in English and Traditional Chinese. If something doesn’t work for you, email <a class=\"u\" href=\"mailto:{EMAIL}\">{EMAIL_DISPLAY}</a> or message us on WhatsApp and we’ll help — and fix it.",
              f"每一頁都有英文及繁體中文版本。如遇到任何使用問題，請電郵至 <a class=\"u\" href=\"mailto:{EMAIL}\">{EMAIL_DISPLAY}</a> 或透過 WhatsApp 聯絡我們，我們會協助並作出修正。"),
        ]),
        (L("Tax guides and calculators", "稅務指南及計算工具"), [
            L("The guides and calculators on this site are general information, not advice for your situation. Rates and thresholds were correct when published and can change.",
              "本網站的指南及計算工具僅屬一般資訊，並非針對個人情況的意見。稅率及門檻以發佈時為準，日後可能改變。"),
        ]),
    ]
    out = "".join(f"""<section class="legal-sec" aria-labelledby="l{i}"><h2 id="l{i}" class="h-md">{r(h, lang)}</h2>{''.join(f'<p>{r(p, lang)}</p>' for p in ps)}</section>"""
                  for i, (h, ps) in enumerate(sections))
    body = page_head(lang, L("Legal", "法律聲明"), L("Privacy &amp; accessibility", "私隱及無障礙聲明"),
                     L("How we handle your information, and how we make this site usable for everyone.", "我們如何處理您的資料，以及如何讓每個人都能使用本網站。")) + f"""
<div class="wrap legal">{out}</div>"""
    title = L("Privacy & accessibility | IQTi Accountants", "私隱及無障礙聲明 | IQTi 會計師事務所")
    desc = L("Privacy notice and accessibility statement for IQTi Accountants.", "IQTi 會計師事務所的私隱聲明及無障礙聲明。")
    write(lang, "legal.html", page(lang, "legal.html", r(title, lang), r(desc, lang), body))


if __name__ == "__main__":
    for lang in LANGS:
        for fn in (home, services, fees, guides, about, contact, legal):
            fn(lang)
    print("built", 7 * len(LANGS), "pages")

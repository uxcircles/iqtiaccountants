# IQTi Accountants (IQTi 會計師事務所): website redesign

A concept redesign of [iqtiaccountants.co.uk](https://www.iqtiaccountants.co.uk/), the London accounting firm working in English, Cantonese and Mandarin. Plain HTML, CSS and JavaScript: the repository root can be hosted on any static host (GitHub Pages, Netlify, Cloudflare Pages, Vercel).

## Languages

| Path   | Language                       |
|--------|--------------------------------|
| `/`    | English                        |
| `/zh/` | 繁體中文 (Traditional Chinese) |

**Pages:** Home · Services · Fees · Tax guides · About · Contact · Privacy & accessibility

## What's new compared with the current site

- **Fee estimator** (`fees.html`): tick services to see a typical monthly fixed fee, then carry the selection into the quote form.
- **Making Tax Digital checker** (`guides.html#mtd`): enter qualifying income to see whether MTD for Income Tax applies from April 2026, 2027 or 2028.
- **Stamp Duty calculator** (`guides.html#sdlt`): England & NI residential rates from 1 April 2025, with first-time buyer relief, the 5% additional-property surcharge and the 2% non-resident surcharge.
- **Quote form** with the same questions as the original, sent via WhatsApp or email (no backend; nothing is stored).
- Mobile quick-action bar (Call · WhatsApp · Get a quote), and a real privacy notice and accessibility statement in place of the Wix placeholder text.

## Run locally

```bash
python3 -m http.server 5210
```

## Editing

The HTML is generated so the header, footer and contact details stay identical across all 14 pages:

- Contact details, header, footer, JS strings: `_build/layout.py`
- Services, values, fees, team, testimonials, FAQ (English and Chinese side by side via `L(english, 中文)`): `_build/content.py`
- Page layouts: `_build/pages.py`

```bash
python3 _build/pages.py      # rebuild pages
python3 _build/fonts.py      # re-subset fonts after changing Chinese text
```

Fonts are self-hosted in `assets/fonts/`: Bricolage Grotesque (headings), Hanken Grotesk (body) and Noto Sans TC (Chinese, subset to the characters used).

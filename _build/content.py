"""Site content in both languages, side by side: L(english, 中文)."""
from layout import L

# I · Q · T · i — the four letters of the name, as on the original site
VALUES = [
    ("I", L("Integrity", "Integrity 誠信"), L("High ethical standards, with honesty in everything we file and say.", "誠實、正直，具有高度的道德標準。")),
    ("Q", L("Quality", "Quality 品質"), L("Competent, diligent work, checked before it reaches HMRC.", "以能力和勤勉提供優質服務。")),
    ("T", L("Trustworthy", "Trustworthy 可靠"), L("Reliable and confidential. Your figures stay between us.", "可靠且保密，您的資料絕不外洩。")),
    ("i", L("international", "international 國際"), L("Chinese expertise, locally grounded in UK tax.", "中英專業知識，紮根於英國稅務。")),
]

STATS = [
    ("50+", L("satisfied clients", "滿意的客戶")),
    ("£10M+", L("in assets managed", "管理資產")),
    ("20+", L("years of experience", "年經驗")),
]

GROUPS = [
    {
        "id": "personal",
        "title": L("You &amp; your property", "個人及物業"),
        "lead": L("Sole traders, landlords, investors and anyone HMRC has asked for a tax return.",
                  "適合自僱人士、房東、投資者，以及任何需要向稅局報稅的人士。"),
        "items": [
            ("self-assessment", L("Self Assessment tax returns", "個人報稅"),
             L("We prepare and file your return, work out what you owe and your payments on account, and remind you well before 31 January.",
               "我們為您準備及遞交個人報稅表，計算應繳稅款及預繳稅款，並在 1 月 31 日截止前提醒您。")),
            ("landlord", L("Landlord &amp; non-resident landlord tax", "房東及非英國居民房東稅務"),
             L("Rental profit, allowable expenses and mortgage-interest relief, plus registration and returns under HMRC’s Non-Resident Landlord Scheme.",
               "計算租金利潤、可扣除開支及按揭利息寬減，並處理稅局「非居民房東計劃」的登記及申報。")),
            ("cgt", L("Capital Gains Tax", "資本利得稅"),
             L("Selling a property or shares. UK residential property sales must be reported and the tax paid within 60 days of completion. We calculate the gain, apply reliefs and file on time.",
               "出售物業或股票。出售英國住宅物業須於完成交易後 60 天內申報及繳稅。我們計算收益、申請寬減並準時申報。")),
        ],
    },
    {
        "id": "company",
        "title": L("Your limited company", "有限公司"),
        "lead": L("From the day you incorporate to every year-end after.",
                  "由成立公司開始，到之後每一個財政年度。"),
        "items": [
            ("accounts", L("Company annual accounts", "公司年度財務報表"),
             L("Statutory accounts prepared and filed at Companies House, due nine months after your year end.",
               "編製法定帳目並遞交 Companies House，限期為年結後九個月。")),
            ("ct", L("Corporation Tax returns", "公司所得稅申報"),
             L("Your CT600 return, with the tax worked out and planned for: payment is normally due nine months and one day after year end.",
               "準備 CT600 公司稅申報表並作稅務規劃；稅款一般須於年結後九個月零一天內繳交。")),
            ("confirmation", L("Confirmation statement", "公司確認聲明"),
             L("Filed every year so the details Companies House holds on your company stay correct.",
               "每年遞交，確保 Companies House 的公司資料準確無誤。")),
            ("formation", L("Company formation", "成立公司"),
             L("We set up your limited company and register it for Corporation Tax, and for PAYE and VAT when you need them.",
               "為您成立有限公司，登記公司稅，並在需要時登記 PAYE 及增值稅。")),
        ],
    },
    {
        "id": "monthly",
        "title": L("Month to month", "日常營運"),
        "lead": L("The regular work that keeps a business ready for its deadlines.",
                  "讓業務隨時準備好應付各項截止日期的日常工作。"),
        "items": [
            ("bookkeeping", L("Bookkeeping", "理帳服務"),
             L("Bank reconciliations, receipts and invoices kept up to date in Xero, FreeAgent or Hammock — monthly or quarterly.",
               "在 Xero、FreeAgent 或 Hammock 中處理銀行對帳、收據及發票，每月或每季更新。")),
            ("vat", L("VAT returns", "VAT 增值稅申報"),
             L("Registration once your turnover passes £90,000, and Making Tax Digital-compatible returns every quarter.",
               "營業額超過 £90,000 時協助登記，並每季遞交符合數碼報稅（MTD）要求的增值稅申報。")),
            ("payroll", L("PAYE payroll", "PAYE 薪酬服務"),
             L("Payslips, Real Time Information submissions to HMRC, workplace pensions and year-end P60s.",
               "處理糧單、向稅局實時申報（RTI）、職場退休金及年終 P60。")),
            ("reporting", L("Financial reporting", "財務報告"),
             L("Management accounts and clear figures for you, your bank or your mortgage lender.",
               "提供管理帳目，以及給您、銀行或按揭機構的清晰財務數字。")),
        ],
    },
]

WHY = [
    (L("A personal approach", "個人化服務"),
     L("Accounting solutions tailored to your situation, not a one-size package, from a small team that gets to know your file.",
       "按您的實際情況度身制定會計方案，而非一式一樣的套餐；小團隊熟悉您的帳目。")),
    (L("English, Cantonese, Mandarin", "英語、粵語、普通話"),
     L("Explain your situation in the language you think in. We translate HMRC letters into plain words.",
       "用您最習慣的語言說明情況，我們會把稅局信件解釋得清清楚楚。")),
    (L("Cloud software", "雲端會計軟件"),
     L("We work in Xero, FreeAgent and Hammock, so your records are always up to date and nothing gets lost in email.",
       "我們使用 Xero、FreeAgent 和 Hammock，帳目隨時更新，文件不會在電郵中遺失。")),
    (L("Fixed fees, agreed first", "固定收費，事先議定"),
     L("Every fee is set before we start. No hidden charges, no surprise invoices.",
       "所有費用在開始前議定，沒有隱藏收費，也沒有意外帳單。")),
]

FEES = [
    ("sa", 20, L("Self Assessment tax return", "個人報稅"), L("Sole traders, directors, rental or foreign income", "自僱人士、董事、租金或海外收入")),
    ("landlord", 20, L("Landlord tax services", "房東稅務服務"), L("UK and non-resident landlords", "英國及非居民房東")),
    ("company", 120, L("Company accounts &amp; tax return", "公司年度帳目及稅表"), L("Annual accounts, CT600 and confirmation statement", "年度帳目、CT600 及確認聲明")),
    ("books", 80, L("Bookkeeping", "理帳服務"), L("Monthly or quarterly, in cloud software", "每月或每季，使用雲端軟件")),
    ("vat", 50, L("VAT returns", "增值稅申報"), L("Quarterly, MTD-compatible", "每季，符合 MTD 要求")),
    ("paye", 50, L("PAYE payroll", "PAYE 薪酬"), L("Payslips, RTI and pensions", "糧單、RTI 及退休金")),
]

STEPS = [
    (L("Free 15-minute chat", "15 分鐘免費諮詢"),
     L("Tell us what you need by phone, WhatsApp, WeChat or video — in the language you prefer.",
       "透過電話、WhatsApp、微信或視像，用您喜歡的語言告訴我們您的需要。")),
    (L("A fixed quote", "固定收費報價"),
     L("We confirm the work and the fee in writing before anything starts.",
       "開始工作前，我們以書面確認工作範圍及費用。")),
    (L("Easy set-up", "輕鬆開始"),
     L("We become your agent with HMRC, contact your previous accountant and connect your cloud software.",
       "我們登記成為您在稅局的代理，聯絡您之前的會計師，並連接雲端會計軟件。")),
    (L("We file. You get reminders.", "我們申報，準時提醒"),
     L("Deadlines are tracked for you, and you’ll know what you owe well before it’s due.",
       "我們為您跟進所有截止日期，讓您在到期前早早知道應繳金額。")),
]

TEAM = [
    ("esther", "Esther", L("FCCA, MBA", "FCCA、MBA"), L("Accountant", "會計師"),
     L("Esther is a Fellow of the Association of Chartered Certified Accountants (FCCA) and holds an MBA. She works with clients in English, Cantonese and Mandarin.",
       "Esther 是英國特許公認會計師公會資深會員（FCCA），並持有工商管理碩士學位，以英語、粵語及普通話服務客戶。")),
    ("lee", "Lee", L("Associate", "助理"), L("Associate", "助理"),
     L("Lee is an Associate at IQTi, supporting client work throughout the year.",
       "Lee 是 IQTi 的助理，全年支援客戶工作。")),
]

TESTIMONIALS = [
    (L("Anna Leung", "梁安娜"),
     L("IQTi Accountants has been instrumental in streamlining our financial processes and providing valuable insights. Their expertise is unmatched.",
       "IQTi 會計師事務所在簡化我們的財務流程和提供寶貴見解方面發揮了重要作用。他們的專業知識無與倫比。")),
    (L("Michael Lee", "李麥可"),
     L("I highly recommend IQTi Accountants for their exceptional accounting services and commitment to client satisfaction.",
       "我強烈推薦 IQTi 會計師事務所，因為他們提供卓越的會計服務並致力於讓客戶滿意。")),
    (L("Emily Chow", "周慧敏"),
     L("IQTi Accountants has played a crucial role in optimising our financial strategies and ensuring compliance. Their dedication is truly commendable.",
       "IQTi 會計師事務所在優化我們的財務策略和確保合規方面發揮了至關重要的作用。他們的奉獻精神確實值得稱讚。")),
]

FAQ = [
    (L("Is the fee really fixed?", "收費真的固定嗎？"),
     L("Yes. We agree the fee in writing before we start, based on what you need and your turnover. If your circumstances change — say you register for VAT — we’ll agree any change with you first.",
       "是的。我們會按您的需要及營業額，在開始前以書面議定費用。如情況有變（例如登記增值稅），我們會先與您協商。")),
    (L("Do I need to come to the office?", "需要親身到辦事處嗎？"),
     L("No. Meetings are by appointment, in person or online, and documents can be shared by email or through your cloud accounting software.",
       "不需要。會面需預約，可親身或網上進行；文件可透過電郵或雲端會計軟件傳送。")),
    (L("Can I switch to you from my current accountant?", "可以從現有會計師轉到你們嗎？"),
     L("Yes, at any point in the year. With your permission we contact your previous accountant for the records we need, so you don’t have to.",
       "可以，一年中任何時候都可以。經您同意後，我們會直接聯絡您之前的會計師索取所需資料。")),
    (L("I live outside the UK but rent out a UK property. Can you help?", "我住在英國境外，但在英國有出租物業，可以協助嗎？"),
     L("Yes. We handle the Non-Resident Landlord Scheme and the UK tax return that usually goes with it.",
       "可以。我們處理「非居民房東計劃」及相關的英國報稅。")),
]

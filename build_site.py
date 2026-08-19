import os

ROOT = os.path.join(os.path.dirname(__file__), "site")

SLUG_PATH = {
    "home": "",
    "about": "about",
    "partners": "partners",
    "risk": "risk-management",
    "regulatory": "regulatory-documents",
    "contacts": "contacts",
}

NAV_ORDER = ["home", "about", "partners", "risk", "regulatory", "contacts"]

NAV_LABEL = {
    "uk": {"home": "Головна", "about": "Про нас", "partners": "Партнерам", "risk": "Ризик-менеджмент",
           "regulatory": "Нормативні акти", "contacts": "Контакти"},
    "en": {"home": "Home", "about": "About us", "partners": "For partners", "risk": "Risk management",
           "regulatory": "Regulatory docs", "contacts": "Contacts"},
}

META = {
    "home": {
        "uk": ("AMOS 2012 — торгівля електричною енергією", "AMOS 2012 — професійна торгівля електричною енергією на ринку України: аналітика, фінансова дисципліна, довгострокове партнерство."),
        "en": ("AMOS 2012 — Electricity Trading", "AMOS 2012 — professional electricity trading in the Ukrainian market: analytics, financial discipline, long-term partnership."),
    },
    "about": {
        "uk": ("Про нас — AMOS 2012", "Компетенції та підхід AMOS 2012 до торгівлі електричною енергією."),
        "en": ("About us — AMOS 2012", "AMOS 2012's competencies and approach to electricity trading."),
    },
    "partners": {
        "uk": ("Партнерам — AMOS 2012", "Умови співпраці з AMOS 2012 та коло потенційних партнерів."),
        "en": ("For partners — AMOS 2012", "Cooperation terms with AMOS 2012 and who we work with."),
    },
    "risk": {
        "uk": ("Ризик-менеджмент — AMOS 2012", "Як AMOS 2012 управляє ціновими, кредитними та регуляторними ризиками."),
        "en": ("Risk management — AMOS 2012", "How AMOS 2012 manages price, credit, and regulatory risk."),
    },
    "regulatory": {
        "uk": ("Нормативно-правові акти — AMOS 2012", "Перелік нормативно-правових актів, що регулюють діяльність AMOS 2012."),
        "en": ("Regulatory documents — AMOS 2012", "Regulations and legal acts governing AMOS 2012's activity."),
    },
    "contacts": {
        "uk": ("Контакти — AMOS 2012", "Зв'яжіться з AMOS 2012."),
        "en": ("Contacts — AMOS 2012", "Get in touch with AMOS 2012."),
    },
}

ICONS = {
    "shield": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>',
    "link": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><circle cx="8" cy="12" r="4"/><circle cx="16" cy="12" r="4"/></svg>',
    "star": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M12 3l2.6 5.6L21 9.3l-4.5 4.2L17.6 20 12 16.8 6.4 20l1.1-6.5L3 9.3l6.4-.7L12 3z"/></svg>',
    "eye": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M2 12s3.5-6.5 10-6.5S22 12 22 12s-3.5 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="2.5"/></svg>',
    "chart": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></svg>',
    "rings": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><circle cx="8" cy="12" r="4"/><circle cx="16" cy="12" r="4"/></svg>',
    "axis": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M12 2v20M2 12h20"/></svg>',
    "badge": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z"/></svg>',
    "bars": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M4 19V9M12 19V5M20 19v-7"/></svg>',
    "check": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg>',
    "grid": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><rect x="4" y="4" width="16" height="16" rx="1"/><path d="M9 9h6v6H9z"/></svg>',
    "monitor": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M2 12s3.5-6.5 10-6.5S22 12 22 12s-3.5 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="2.5"/></svg>',
    "doc": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#8b9089" stroke-width="1.8"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><path d="M15 3h6v6M10 14L21 3"/></svg>',
}

LOGO_MARK = '''<svg width="28" height="28" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M32 3L58 17.5V46.5L32 61L6 46.5V17.5L32 3Z" stroke="#163837" stroke-width="3"/>
  <path d="M32 18L46 46H37.5L32 34L26.5 46H18L32 18Z" fill="#163837"/>
  <rect x="29.5" y="18" width="5" height="5" fill="#c9873f"/>
</svg>'''

FOOTER_MARK = '''<svg width="17" height="17" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M32 3L58 17.5V46.5L32 61L6 46.5V17.5L32 3Z" stroke="#565c58" stroke-width="3"/><path d="M32 18L46 46H37.5L32 34L26.5 46H18L32 18Z" fill="#8b9089"/><rect x="29.5" y="18" width="5" height="5" fill="#c9873f"/></svg>'''

HAMBURGER = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1c2120" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>'


def href(slug, lang):
    seg = SLUG_PATH[slug]
    base = "/en/" if lang == "en" else "/"
    return base + (seg + "/" if seg else "")


def value_card(icon, title, desc):
    return f'<div class="value-card"><div class="value-icon">{ICONS[icon]}</div><h3>{title}</h3><p>{desc}</p></div>'


def mini_card(icon, label):
    return f'<div class="mini-card"><div class="value-icon">{ICONS[icon]}</div><span>{label}</span></div>'


def bullet_list(items):
    lis = "".join(f'<li><span class="bullet-dot"></span><span>{i}</span></li>' for i in items)
    return f'<ul class="bullet-list">{lis}</ul>'


def chip_grid(items):
    spans = "".join(f'<span class="chip">{i}</span>' for i in items)
    return f'<div class="chip-grid">{spans}</div>'


def doc_row(text, pending=False, badge=None):
    if pending:
        return (f'<div class="doc-row pending">{ICONS["badge"]}<span>{text}</span>'
                f'<span class="pending-badge">{badge}</span></div>')
    return f'<div class="doc-row">{ICONS["doc"]}<span>{text}</span></div>'


def home_body(lang):
    t = {
        "uk": dict(h1="Стабільність у кожній енергетичній угоді",
                   sub="AMOS 2012 торгує електричною енергією на ринку України, поєднуючи аналітику, фінансову дисципліну та довіру партнерів.",
                   cta1="Зв'язатися з нами", cta2="Про нас",
                   about_kicker="Про компанію", about_h2="Хто ми",
                   about_p="AMOS 2012 працює на ринку електричної енергії України, поєднуючи аналітику, фінансову дисципліну та глибоке розуміння регуляторного середовища. Наша мета — надійні й економічно обґрунтовані рішення для кожного партнера.",
                   values_kicker="Принципи роботи", values_h2="Наші цінності",
                   values=[("shield", "Надійність", "Виконуємо зобов'язання та тримаємо слово в кожній енергетичній угоді."),
                           ("link", "Партнерство", "Будуємо довгострокові відносини на основі довіри."),
                           ("star", "Досвід", "Глибоке розуміння енергетичного ринку та професійний підхід."),
                           ("eye", "Прозорість", "Відкрита комунікація на кожному етапі співпраці.")],
                   ct_h2="Зв'яжіться з нами", ct_p="Готові обговорити умови співпраці — залиште заявку, і ми зв'яжемося з вами.", ct_btn="Перейти до контактів"),
        "en": dict(h1="Stability in every energy deal",
                   sub="AMOS 2012 trades electricity on the Ukrainian market, combining analytics, financial discipline, and the trust of our partners.",
                   cta1="Get in touch", cta2="About us",
                   about_kicker="About the company", about_h2="Who we are",
                   about_p="AMOS 2012 operates in Ukraine's electricity market, combining analytics, financial discipline, and a deep understanding of the regulatory environment. Our goal is dependable, economically sound solutions for every partner.",
                   values_kicker="How we work", values_h2="Our values",
                   values=[("shield", "Reliability", "We honor our commitments and keep our word in every energy deal."),
                           ("link", "Partnership", "We build long-term relationships based on trust."),
                           ("star", "Expertise", "Deep understanding of the energy market and a professional approach."),
                           ("eye", "Transparency", "Open communication at every stage of cooperation.")],
                   ct_h2="Get in touch", ct_p="Ready to discuss cooperation terms — leave a request and we'll get back to you.", ct_btn="Go to contacts"),
    }[lang]

    values_html = "".join(value_card(*v) for v in t["values"])

    return f'''<section class="site-hero">
  <svg class="site-hero-rings" width="480" height="480" viewBox="0 0 480 480" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="240" cy="240" r="239" stroke="rgba(247,244,238,0.08)"/>
    <circle cx="240" cy="240" r="178" stroke="rgba(247,244,238,0.1)"/>
    <circle cx="240" cy="240" r="116" stroke="#c9873f" stroke-opacity="0.35"/>
  </svg>
  <div class="site-hero-inner">
    <div class="site-eyebrow"><span class="rule"></span><span>AMOS 2012</span></div>
    <h1>{t["h1"]}</h1>
    <p class="site-hero-sub">{t["sub"]}</p>
    <div class="site-cta-row">
      <a class="btn-primary" href="{href('contacts', lang)}">{t["cta1"]}</a>
      <a class="btn-ghost" href="{href('about', lang)}">{t["cta2"]}</a>
    </div>
  </div>
</section>

<section class="site-about">
  <div>
    <span class="site-kicker">{t["about_kicker"]}</span>
    <h2>{t["about_h2"]}</h2>
    <p>{t["about_p"]}</p>
  </div>
  <div class="about-mark">
    <svg width="220" height="220" viewBox="0 0 300 300" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M150 20L272 80V220L150 280L28 220V80L150 20Z" stroke="#163837" stroke-width="1.5" opacity="0.5"/>
      <path d="M150 70L212 210H182L150 150L118 210H88L150 70Z" fill="#163837" opacity="0.92"/>
      <rect x="140" y="70" width="20" height="20" fill="#c9873f"/>
    </svg>
  </div>
</section>

<section class="site-values">
  <div class="site-values-inner">
    <span class="site-kicker">{t["values_kicker"]}</span>
    <h2>{t["values_h2"]}</h2>
    <div class="values-grid">{values_html}</div>
  </div>
</section>

<section class="contact-teaser">
  <div class="contact-teaser-inner">
    <div>
      <h2>{t["ct_h2"]}</h2>
      <p>{t["ct_p"]}</p>
    </div>
    <a class="btn-primary" href="{href('contacts', lang)}">{t["ct_btn"]}</a>
  </div>
</section>'''


def about_body(lang):
    t = {
        "uk": dict(
            kicker="Компанія", h1="Про нас",
            lead="AMOS 2012 поєднує глибоку експертизу на ринку електричної енергії з фінансовою дисципліною та системним підходом до ризиків.",
            h2a="Наші компетенції",
            l1h="Що ми робимо",
            l1=["Формування контрактних портфелів на короткостроковий і середньостроковий горизонт",
                "Оптимізація структури угод для покращення маржинальності",
                "Контроль цінових ризиків і зниження впливу ринкової волатильності",
                "Фінансове моделювання та планування грошових потоків"],
            l2h="На чому базуються рішення",
            l2=["Аналіз ринкової кон'юнктури", "Макроекономічні тенденції", "Зміни регуляторного середовища", "Сценарне моделювання"],
            h2b="Наш підхід",
            l3h="У фундаменті нашого бізнесу",
            l3=["Довгострокові партнерські відносини", "Неухильне дотримання регуляторних норм",
                "Фінансова дисципліна на кожному етапі", "Контроль операційних і кредитних ризиків"],
            l4h="Стратегія розвитку",
            l4=["Розширення обсягів торгівлі", "Поступова інтеграція в європейський енергоринок", "Вихід у суміжні напрямки енергетичного бізнесу"],
        ),
        "en": dict(
            kicker="Company", h1="About us",
            lead="AMOS 2012 combines deep expertise in the electricity market with financial discipline and a systematic approach to risk.",
            h2a="Our competencies",
            l1h="What we do",
            l1=["Structuring contract portfolios across short- and medium-term horizons",
                "Optimizing deal structures to improve margins",
                "Managing price risk and reducing the impact of market volatility",
                "Financial modeling and cash-flow planning"],
            l2h="What our decisions are based on",
            l2=["Market-conditions analysis", "Macroeconomic trends", "Regulatory developments", "Scenario modeling"],
            h2b="Our approach",
            l3h="What our business is built on",
            l3=["Long-term partnerships", "Strict regulatory compliance", "Financial discipline at every stage", "Control of operational and credit risk"],
            l4h="Growth strategy",
            l4=["Scaling trading volumes", "Gradual integration into the European energy market", "Expansion into adjacent energy-business areas"],
        ),
    }[lang]

    return f'''<div class="page-head"><div class="page-head-inner">
  <span class="site-kicker">{t["kicker"]}</span>
  <h1>{t["h1"]}</h1>
  <p>{t["lead"]}</p>
</div></div>
<section class="page-section"><div class="page-section-inner">
  <h2>{t["h2a"]}</h2>
  <div class="split-lists">
    <div class="list-block"><h3>{t["l1h"]}</h3>{bullet_list(t["l1"])}</div>
    <div class="list-block"><h3>{t["l2h"]}</h3>{bullet_list(t["l2"])}</div>
  </div>
</div></section>
<section class="page-section"><div class="page-section-inner">
  <h2>{t["h2b"]}</h2>
  <div class="split-lists">
    <div class="list-block"><h3>{t["l3h"]}</h3>{bullet_list(t["l3"])}</div>
    <div class="list-block"><h3>{t["l4h"]}</h3>{bullet_list(t["l4"])}</div>
  </div>
</div></section>'''


def partners_body(lang):
    t = {
        "uk": dict(
            kicker="Співпраця", h1="Партнерам",
            lead="AMOS 2012 орієнтована на тривалу співпрацю і пропонує гнучкі умови взаємодії, адаптовані під потреби кожного партнера.",
            h2a="Принципи співпраці",
            principles=["Прозорі умови співпраці", "Точне виконання договірних зобов'язань", "Гнучкі комерційні схеми",
                        "Системний підхід до ризиків", "Оперативність у прийнятті рішень", "Структуровані торгові пропозиції",
                        "Оптимізація портфеля угод", "Постійна аналітична підтримка", "Безперервний моніторинг ринку"],
            h2b="Географія",
            geo="AMOS 2012 працює на ринку України з орієнтацією на розвиток співпраці з європейськими енергетичними ринками.",
            h2c="Відкриті до співпраці з",
            partners=["Торгові компанії", "Постачальники електроенергії", "Виробники електроенергії", "Імпортери та експортери",
                      "Учасники закордонних енергоринків", "Фінансові установи", "Інвестори"],
            ct_h2="Готові обговорити співпрацю?", ct_btn="Обговорити співпрацю",
        ),
        "en": dict(
            kicker="Cooperation", h1="For partners",
            lead="AMOS 2012 is built for long-term cooperation and offers flexible terms tailored to each partner's needs.",
            h2a="Principles of cooperation",
            principles=["Transparent terms", "Precise contract fulfillment", "Flexible commercial models",
                        "Systematic risk management", "Fast decision-making", "Structured trade proposals",
                        "Deal-portfolio optimization", "Ongoing analytical support", "Continuous market monitoring"],
            h2b="Geography",
            geo="AMOS 2012 operates in the Ukrainian market with a focus on expanding cooperation with European energy markets.",
            h2c="Open to cooperation with",
            partners=["Trading companies", "Electricity suppliers", "Electricity producers", "Import/export businesses",
                      "Foreign market participants", "Financial institutions", "Investors"],
            ct_h2="Ready to discuss cooperation?", ct_btn="Discuss cooperation",
        ),
    }[lang]

    return f'''<div class="page-head"><div class="page-head-inner">
  <span class="site-kicker">{t["kicker"]}</span>
  <h1>{t["h1"]}</h1>
  <p>{t["lead"]}</p>
</div></div>
<section class="page-section"><div class="page-section-inner">
  <h2>{t["h2a"]}</h2>
  {chip_grid(t["principles"])}
</div></section>
<section class="page-section"><div class="page-section-inner">
  <h2>{t["h2b"]}</h2>
  <p style="font-size:14.5px; line-height:1.7; color:var(--brand-ink-soft); max-width:60ch;">{t["geo"]}</p>
</div></section>
<section class="page-section"><div class="page-section-inner">
  <h2>{t["h2c"]}</h2>
  {chip_grid(t["partners"])}
</div></section>
<section class="contact-teaser"><div class="contact-teaser-inner">
  <div><h2>{t["ct_h2"]}</h2></div>
  <a class="btn-primary" href="{href('contacts', lang)}">{t["ct_btn"]}</a>
</div></section>'''


def risk_body(lang):
    t = {
        "uk": dict(
            kicker="Управління ризиками", h1="Ризик-менеджмент",
            lead="Управління ризиками — невід'ємна частина щоденної роботи AMOS 2012.",
            h_risks="Ризики, якими ми управляємо",
            risks=[("chart", "Цінові ризики"), ("rings", "Кредитні ризики контрагентів"),
                   ("axis", "Ризики ліквідності"), ("badge", "Регуляторні ризики")],
            h_tools="Інструменти",
            tools=[("bars", "Сценарний аналіз"), ("check", "Фінансове планування"),
                   ("grid", "Ліміти на контрагентів"), ("monitor", "Постійний моніторинг ринку")],
        ),
        "en": dict(
            kicker="Risk management", h1="Risk management",
            lead="Risk management is an integral part of AMOS 2012's daily operations.",
            h_risks="Risks we manage",
            risks=[("chart", "Price risk"), ("rings", "Counterparty credit risk"),
                   ("axis", "Liquidity risk"), ("badge", "Regulatory risk")],
            h_tools="Tools we use",
            tools=[("bars", "Scenario analysis"), ("check", "Financial planning"),
                   ("grid", "Counterparty limits"), ("monitor", "Continuous market monitoring")],
        ),
    }[lang]

    risks_html = "".join(mini_card(*r) for r in t["risks"])
    tools_html = "".join(mini_card(*r) for r in t["tools"])

    return f'''<div class="page-head"><div class="page-head-inner">
  <span class="site-kicker">{t["kicker"]}</span>
  <h1>{t["h1"]}</h1>
  <p>{t["lead"]}</p>
</div></div>
<section class="page-section"><div class="page-section-inner">
  <div class="list-block"><h3>{t["h_risks"]}</h3><div class="mini-grid">{risks_html}</div></div>
  <div class="list-block"><h3>{t["h_tools"]}</h3><div class="mini-grid">{tools_html}</div></div>
</div></section>'''


def regulatory_body(lang):
    t = {
        "uk": dict(
            kicker="Документи", h1="Нормативно-правові акти",
            lead="Перелік ключових нормативно-правових актів, що регулюють діяльність AMOS 2012 на ринку електричної енергії України.",
            docs=["Кабінет Міністрів України — офіційний вебпортал",
                  "Закон України «Про ринок електричної енергії» № 2019-VIII",
                  "Закон України «Про ліцензування видів господарської діяльності»",
                  "Закон України «Про звернення громадян»",
                  "Закон України «Про доступ до публічної інформації»",
                  "Закон України «Про захист персональних даних»",
                  "Закон України «Про захист прав споживачів»",
                  "Постанова НКРЕКП про Правила ринку електричної енергії",
                  "Постанова НКРЕКП про Кодекс системи передачі",
                  "Постанова НКРЕКП про Кодекс системи розподілу",
                  "Постанова НКРЕКП про Правила ринку «на добу наперед» та внутрішньодобового ринку",
                  "Постанова НКРЕКП про Ліцензійні умови постачання електричної енергії",
                  "Постанова НКРЕКП про Кодекс комерційного обліку електричної енергії",
                  "НКРЕКП — офіційний вебпортал"],
            pending="Ліцензія на право провадження діяльності з постачання електричної енергії — AMOS 2012",
            badge="Очікується",
        ),
        "en": dict(
            kicker="Documents", h1="Regulatory documents",
            lead="Key regulations and legal acts governing AMOS 2012's activity on Ukraine's electricity market.",
            docs=["Cabinet of Ministers of Ukraine — official portal",
                  'Law of Ukraine "On the Electricity Market" No. 2019-VIII',
                  'Law "On Licensing of Business Activities"',
                  'Law "On Citizens\' Appeals"',
                  'Law "On Access to Public Information"',
                  'Law "On Personal Data Protection"',
                  'Law "On Consumer Rights Protection"',
                  "NKREKP Resolution on the Electricity Market Rules",
                  "NKREKP Resolution on the Transmission System Code",
                  "NKREKP Resolution on the Distribution System Code",
                  "NKREKP Resolution on Day-Ahead and Intraday Market Rules",
                  "NKREKP Resolution on Electricity Supply Licensing Conditions",
                  "NKREKP Resolution on the Commercial Metering Code",
                  "NKREKP — official portal"],
            pending="License for the supply of electricity — AMOS 2012",
            badge="Pending",
        ),
    }[lang]

    rows = "".join(doc_row(d) for d in t["docs"])
    rows += doc_row(t["pending"], pending=True, badge=t["badge"])

    return f'''<div class="page-head"><div class="page-head-inner">
  <span class="site-kicker">{t["kicker"]}</span>
  <h1>{t["h1"]}</h1>
  <p>{t["lead"]}</p>
</div></div>
<section class="page-section"><div class="page-section-inner">
  <div class="doc-list">{rows}</div>
</div></section>'''


def contacts_body(lang):
    t = {
        "uk": dict(kicker="Контакти", h1="Зв'яжіться з нами", lead="Залиште повідомлення, і ми відповімо найближчим часом.",
                   addr_l="Адреса", addr_v="[адреса]", phone_l="Телефон", phone_v="[телефон]", email_v="[email]",
                   name_l="Ім'я", msg_l="Повідомлення", send="Надіслати",
                   note="Форма використовує сервіс Web3Forms — потрібно додати власний access key."),
        "en": dict(kicker="Contacts", h1="Get in touch", lead="Leave a message and we'll respond shortly.",
                   addr_l="Address", addr_v="[address]", phone_l="Phone", phone_v="[phone]", email_v="[email]",
                   name_l="Name", msg_l="Message", send="Send",
                   note="This form uses Web3Forms — add your own access key before launch."),
    }[lang]

    return f'''<div class="page-head"><div class="page-head-inner">
  <span class="site-kicker">{t["kicker"]}</span>
  <h1>{t["h1"]}</h1>
  <p>{t["lead"]}</p>
</div></div>
<section class="site-contact"><div class="site-contact-inner">
  <div class="contact-info">
    <div class="contact-fields">
      <div>{t["addr_l"]}: {t["addr_v"]}</div>
      <div>{t["phone_l"]}: {t["phone_v"]}</div>
      <div>Email: {t["email_v"]}</div>
    </div>
  </div>
  <div class="contact-form-wrap">
    <form class="contact-form" action="https://api.web3forms.com/submit" method="POST">
      <input type="hidden" name="access_key" value="REPLACE_WITH_WEB3FORMS_ACCESS_KEY">
      <input type="checkbox" name="botcheck" class="form-honeypot" tabindex="-1" autocomplete="off">
      <div class="field-group">
        <span class="field-label">{t["name_l"]}</span>
        <input class="field-input" type="text" name="name" required>
      </div>
      <div class="field-group">
        <span class="field-label">Email</span>
        <input class="field-input" type="email" name="email" required>
      </div>
      <div class="field-group">
        <span class="field-label">{t["msg_l"]}</span>
        <textarea class="field-input" name="message" rows="4" required></textarea>
      </div>
      <button class="btn-primary" type="submit">{t["send"]}</button>
      <span class="form-note">{t["note"]}</span>
    </form>
  </div>
</div></section>'''


BODY_FN = {
    "home": home_body,
    "about": about_body,
    "partners": partners_body,
    "risk": risk_body,
    "regulatory": regulatory_body,
    "contacts": contacts_body,
}


def render_page(slug, lang):
    title, desc = META[slug][lang]
    other_lang = "en" if lang == "uk" else "uk"

    nav_items = "".join(
        f'<a href="{href(s, lang)}"{" aria-current=\"page\"" if s == slug else ""}>{NAV_LABEL[lang][s]}</a>'
        for s in NAV_ORDER
    )

    uk_link_href = href(slug, "uk")
    en_link_href = href(slug, "en")
    lang_switch = (
        '<div class="lang-switch" role="group" aria-label="Language">'
        f'<a class="lang-link{" active" if lang == "uk" else ""}" href="{uk_link_href}">UA</a>'
        '<span class="lang-sep">/</span>'
        f'<a class="lang-link{" active" if lang == "en" else ""}" href="{en_link_href}">EN</a>'
        '</div>'
    )

    body = BODY_FN[slug](lang)
    html_lang = "en" if lang == "en" else "uk"

    return f'''<!doctype html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="uk" href="https://amos2012.com{uk_link_href}">
<link rel="alternate" hreflang="en" href="https://amos2012.com{en_link_href}">
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@500;600;700;900&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<div class="site-shell">
<header class="site-header">
  <a class="site-logo" href="{href('home', lang)}">
    {LOGO_MARK}
    <div class="site-logo-text"><span class="top">AMOS</span><span class="bottom">2012</span></div>
  </a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">{HAMBURGER}</button>
  <nav class="site-nav" id="site-nav">
    {nav_items}
    {lang_switch}
  </nav>
</header>

<main>
{body}
</main>

<footer class="site-footer">
  <div class="site-footer-brand">{FOOTER_MARK}<span>AMOS 2012</span></div>
  <div class="site-footer-legal">{"© 2026 AMOS 2012. Всі права захищені." if lang == "uk" else "© 2026 AMOS 2012. All rights reserved."}</div>
</footer>
</div>
<script src="/assets/js/main.js"></script>
</body>
</html>
'''


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


for slug in NAV_ORDER:
    for lang in ("uk", "en"):
        seg = SLUG_PATH[slug]
        prefix = "en/" if lang == "en" else ""
        out_path = f"{prefix}{seg + '/' if seg else ''}index.html"
        write(out_path, render_page(slug, lang))

write("robots.txt", "User-agent: *\nAllow: /\n")

print("Site generated at", ROOT)

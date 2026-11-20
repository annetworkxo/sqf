#!/usr/bin/env python3
"""Write the static HTML pages for the GitHub Pages package."""
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent

AREAS = [
    "Quality, automotive & specialist systems",
    "Environment, safety & sustainability",
    "Information security & business resilience",
    "Food safety & food-sector assurance",
    "Social accountability & responsible business",
    "Product compliance & approval readiness",
]
SERVICES = [
    ("ISO 9001", "Quality management systems", "Management system planning, process documentation, implementation and internal audit support.", 0),
    ("IATF 16949", "Automotive quality management", "Automotive system requirements and quality improvement, with guidance on the core quality tools.", 0),
    ("ISO 13485", "Medical device quality management", "Consultancy for quality management systems for medical devices.", 0),
    ("ISO 15378", "Medicinal product packaging", "Management system requirements for primary packaging materials for medicinal products.", 0),
    ("ISO 21001", "Educational organizations", "Management system consultancy for educational organizations.", 0),
    ("GMP", "Good Manufacturing Practices", "Readiness support for Good Manufacturing Practices in pharmaceutical industries.", 0),
    ("ISO 14001", "Environmental management", "Environmental aspects and impacts, compliance planning and management system implementation.", 1),
    ("ISO 45001", "Occupational health & safety", "Workplace hazard assessment, risk awareness and health and safety management systems.", 1),
    ("ISO 50001", "Energy management", "Consultancy on energy management system requirements and improvement frameworks.", 1),
    ("CBAM", "Carbon Border Adjustment Mechanism", "Guidance on understanding applicable CBAM requirements and readiness for your business.", 1),
    ("ISO 27001", "Information security management", "Consultancy on information security management system requirements.", 2),
    ("TISAX", "Trusted Information Security Assessment Exchange", "Readiness support for information security assessment requirements.", 2),
    ("ISO 22301", "Business continuity management", "Consultancy on business continuity management system requirements.", 2),
    ("CTPAT", "Customs Trade Partnership Against Terrorism", "Readiness consultancy for supply-chain security requirements under CTPAT.", 2),
    ("ISO 22000", "Food safety management", "Food safety management system requirements and implementation support.", 3),
    ("FSSC 22000", "Food safety certification scheme", "Consultancy and readiness support for FSSC 22000 requirements.", 3),
    ("HACCP", "Hazard Analysis and Critical Control Points", "Guidance on the Codex Alimentarius HACCP system, implementation and general principles of food hygiene.", 3),
    ("BRCGS Food", "Global Standard for Food Safety", "Consultancy and preparation for the BRCGS Global Standard for Food Safety.", 3),
    ("ISO 26000", "Social responsibility guidance", "Guidance on social responsibility. ISO 26000 is a guidance standard, rather than a certifiable management system.", 4),
    ("SA8000", "Social accountability", "Support in understanding and implementing social accountability requirements.", 4),
    ("BSCI", "Business Social Compliance Initiative", "Readiness support for business social compliance requirements.", 4),
    ("WRAP", "Worldwide Responsible Accredited Production", "Consultancy on responsible production requirements and assessment readiness.", 4),
    ("SMETA", "Sedex Members Ethical Trade Audit", "Preparation and readiness support for SMETA ethical trade audit requirements.", 4),
    ("EcoVadis", "Sustainability assessment readiness", "Support with readiness for sustainability assessment requirements.", 4),
    ("CE Marking", "European product conformity", "Consultancy on applicable CE marking requirements and preparation for the relevant conformity route.", 5),
    ("UL Approval", "Product approval requirements", "Guidance and preparation for applicable UL approval requirements.", 5),
    ("BIS Approval", "Bureau of Indian Standards", "Consultancy and readiness support for applicable BIS requirements.", 5),
    ("ATEX", "Explosive atmospheres", "Guidance on applicable ATEX requirements for products intended for explosive atmospheres.", 5),
]
EXTRAS = [
    "Free consultation",
    "Training / Internal Audits",
    "Training — Management systems",
    "Training — Social accountability",
    "Training — Automotive quality",
    "Second-party audits",
    "Verification / validation / inspection",
    "Other enquiry",
]
CLIENTS = [
    ("FOX", "fox.png"),
    ("Godrej Agrovet", "godrej-agrovet.png"),
    ("Jindal Stainless", "jindal-stainless.png"),
    ("Caparo", "caparo.png"),
    ("Tata Projects", "tata-projects.png"),
    ("MSS Products", "mss-us.png"),
    ("Pik", "pik.png"),
    ("S D Fine-Chem", "sdfine.png"),
    ("Adam Fabriwerk", "adam-fabriwerk.png"),
    ("Tufropes", "tufropes.png"),
    ("Omea Solar", "omea.png"),
    ("Pelicans Group", "pelicans.png"),
    ("VFE", "vfe.png"),
    ("Polysil", "polysil.png"),
    ("Harish Textile Engineers", "harish-textile.png"),
]
NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("training.html", "Training"),
    ("audits.html", "Audits"),
    ("clients.html", "Clients"),
    ("contact.html", "Contact"),
]
WA = "https://wa.me/917875556748?text=" + html.escape("Hello SQF, I would like to connect.", quote=True)
WA_DISCUSS = "https://wa.me/917875556748?text=" + html.escape("Hello SQF, I would like to discuss consultancy or training.", quote=True)
MAP = "https://www.google.com/maps/search/?api=1&query=Harivishwa+Apartment+Pathardi+Phata+Nashik+422010"
ADDRESS = "Flat No. 1105, Wing B, Harivishwa Apartment, Khanderao Nagar, Behind Express In Hotel, Pathardi Phata, Nashik – 422010, Maharashtra"
DISCLAIMER = "Figures are as presented in the SQF company profile. Consultancy and training do not themselves confer certification or approval — that still depends on the scheme and the certification body."

ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'
PHONE = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.6a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.5-1.1a2 2 0 0 1 2.1-.5c.8.3 1.7.5 2.6.6a2 2 0 0 1 1.7 2z"/></svg>'
MAIL = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 4h16v16H4z"/><path d="m22 6-10 7L2 6"/></svg>'
PIN = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>'
SEARCH = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'


def e(text):
    return html.escape(text)


def contact(service=""):
    href = "contact.html"
    if service:
        href += "?service=" + html.escape(service, quote=True).replace(" ", "%20")
    return href


def shell(active, title, description, body):
    links = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active else ""
        links.append(f'<a href="{href}"{current}>{label}</a>')
    nav = "".join(links)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#10182b">
  <link rel="icon" href="assets/images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <a class="sr-only" href="#main">Skip to content</a>
  <div class="top">
    <div class="offer">
      <div class="wrap">
        <p>Free consultation open until 10 Dec 2026</p>
        <a href="{contact("Free consultation")}">Book {ARROW}</a>
      </div>
    </div>
    <header class="bar wrap">
      <a class="brand" href="index.html">
        <img src="assets/images/sqf-logo-mark.png" alt="" width="44" height="44">
        <span><strong>Shubhkiran</strong><small>Quality Forum · Nashik</small></span>
      </a>
      <nav class="nav" aria-label="Primary">{nav}</nav>
      <div class="actions">
        <a class="btn talk" href="contact.html">Talk to SQF</a>
        <button class="menu-btn" type="button" data-menu aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
        </button>
      </div>
    </header>
    <nav id="mobile-nav" class="menu wrap" data-menu-panel aria-label="Mobile">{nav}</nav>
  </div>
  <main id="main">
{body}
  </main>
  <footer class="site-footer">
    <div class="wrap foot">
      <div>
        <div class="brand">
          <img src="assets/images/sqf-logo-mark.png" alt="" width="48" height="48">
          <h2>Shubhkiran Quality Forum</h2>
        </div>
        <p>Consultancy, training and audit readiness. Nashik, since 1999.</p>
        <p>{e(ADDRESS)}</p>
      </div>
      <div>
        <p class="label">VISIT</p>
        <ul>{"".join(f"<li><a href='{href}'>{label}</a></li>" for href, label in NAV)}
          <li><a href="assets/documents/sqf-company-profile.pdf">Company profile (PDF)</a></li>
        </ul>
      </div>
      <div>
        <p class="label">TALK</p>
        <ul>
          <li><a href="tel:+919370317764">+91 93703 17764 · Vilas Shinde</a></li>
          <li><a href="tel:+917875556741">+91 78755 56741 · Mobile</a></li>
          <li><a href="tel:+912532380070">0253 2380070 · Office</a></li>
          <li><a href="{WA}">WhatsApp · +91 78755 56748</a></li>
          <li><a href="mailto:shubhkiranquality@gmail.com">shubhkiranquality@gmail.com</a></li>
          <li><a href="mailto:vishwaqc@gmail.com">vishwaqc@gmail.com</a></li>
        </ul>
      </div>
    </div>
    <div class="wrap legal">
      <p>© <span data-year>2026</span> Shubhkiran Quality Forum. All rights reserved.</p>
      <p>{e(DISCLAIMER)}</p>
    </div>
  </footer>
  <script src="js/site.js"></script>
</body>
</html>
"""


def close():
    return f"""
    <section class="wrap">
      <div class="close">
        <div>
          <p class="kicker">Next step</p>
          <h2>Tell us the standard.<span style="display:block">We’ll talk through the scope.</span></h2>
        </div>
        <div class="row" style="margin-top:0">
          <a class="btn" href="contact.html">Talk to SQF {ARROW}</a>
          <a class="btn ghost" href="{WA}">WhatsApp</a>
        </div>
      </div>
    </section>"""


def intro(kicker, title, lede, actions=""):
    return f"""
    <header class="wrap" style="padding-top:3.2rem">
      <p class="kicker">{e(kicker)}</p>
      <h1>{title}</h1>
      <p class="lede">{e(lede)}</p>
      {actions}
    </header>"""


pages = {}

pages["index.html"] = shell(
    "index.html",
    "ISO Consultancy & Training in Nashik | Shubhkiran Quality Forum",
    "SQF helps organizations build practical management systems, prepare for audits, and train their people. Nashik, since 1999.",
    f"""
    <section class="wrap hero">
      <div>
        <p class="kicker">Nashik, Maharashtra · Est. 1999</p>
        <h1><span>Better systems.</span><span>Stronger teams.</span><span class="accent">Lasting quality.</span></h1>
        <p class="lede">Quality goes beyond a certificate. We help you build practical management systems, prepare for audits, and give your people the skills to keep improving.</p>
        <form class="finder" action="services.html" method="get">
          {SEARCH}
          <label class="sr-only" for="home-search">Search standards and services</label>
          <input id="home-search" name="q" placeholder="Find a standard — ISO 9001, IATF, HACCP…">
          <button class="btn ink" type="submit">Search</button>
        </form>
        <div class="row">
          <a class="btn" href="contact.html">Discuss your requirements {ARROW}</a>
          <a class="btn ghost" href="services.html">Explore expertise</a>
        </div>
        <p class="proof">Consultancy. Training. Audit readiness. <strong>A practical partner, from assessment to improvement.</strong></p>
      </div>
      <figure class="figure">
        <img class="cover" src="assets/images/training-participants.webp" alt="Training participants gathered for a group photograph with the SQF trainer" width="1280" height="960">
        <figcaption class="caption">
          <div>
            <p class="kicker">People at the heart of quality</p>
            <p>Building capability. Creating lasting relationships.</p>
          </div>
          <img class="logo-round" src="assets/images/sqf-logo-mark.png" alt="" width="48" height="48">
        </figcaption>
      </figure>
    </section>
    <section class="strip">
      <div class="wrap">
        <p class="kicker">Systems we support</p>
        <a href="{contact("ISO 9001")}"><b>ISO 9001</b> <span class="muted">· Quality</span></a>
        <a href="{contact("IATF 16949")}"><b>IATF 16949</b> <span class="muted">· Automotive</span></a>
        <a href="{contact("ISO 14001")}"><b>ISO 14001</b> <span class="muted">· Environment</span></a>
        <a href="{contact("ISO 45001")}"><b>ISO 45001</b> <span class="muted">· Health & safety</span></a>
        <a href="{contact("ISO 22000")}"><b>ISO 22000</b> <span class="muted">· Food safety</span></a>
      </div>
    </section>
    <section class="wrap section split">
      <div>
        <p class="kicker">Your quality partner / since 1999</p>
        <h2>Practical experience. Lasting relationships.</h2>
      </div>
      <div>
        <p class="lede" style="margin-top:0">Based in Nashik and led by mechanical engineer and lead auditor Mr. Vilas Shinde, SQF helps organizations strengthen systems, build capability, and prepare for third-party assessment.</p>
        <p><a href="about.html"><strong>Meet Shubhkiran Quality Forum {ARROW}</strong></a></p>
      </div>
    </section>
    <section class="band">
      <div class="wrap section">
        <div class="split">
          <h2>A complete management solution, since 1999.</h2>
          <p>SQF is a Nashik practice of auditors and engineers. The work is hands-on: management systems, the people who run them, and readiness for assessment — for organizations across India and those that operate further afield.</p>
        </div>
        <dl class="metrics" style="margin-top:2rem">
          <div class="metric"><strong>20+</strong><span>Technical experts</span></div>
          <div class="metric"><strong>~30</strong><span>Years in safety, security and sustainability</span></div>
          <div class="metric"><strong>1,500+</strong><span>Management system implementations</span></div>
          <div class="metric"><strong>5,000+</strong><span>Personnel certifications</span></div>
          <div class="metric"><strong>100%</strong><span>Independent and impartial</span></div>
        </dl>
        <p class="fine">Figures as presented in the SQF company profile. A certificate still depends on the scheme and the certification body.</p>
      </div>
    </section>
    <section class="wrap section">
      <p class="kicker">How the work moves</p>
      <h2>From the requirement to a system that holds.</h2>
      <p class="lede">Plant teams, quality heads, and suppliers usually need the same four things. SQF stays with the work, then leaves the knowledge with the people who will use it.</p>
      <ol class="cards-4" style="margin-top:1.5rem;padding:0;list-style:none">
        <li class="card"><p class="index">01</p><h3>See the gap</h3><p>Start from the standard, the site, and what a customer or assessor will actually look for.</p></li>
        <li class="card"><p class="index">02</p><h3>Build the system</h3><p>Put the management system into the way the organization already works, not into a file that sits on a shelf.</p></li>
        <li class="card"><p class="index">03</p><h3>Train the people</h3><p>Awareness, internal auditors, and the tools the team keeps using after the workshop.</p></li>
        <li class="card"><p class="index">04</p><h3>Stand ready</h3><p>Second-party audits and assessment preparation, so the findings are clear before a third party arrives.</p></li>
      </ol>
    </section>
    <section class="wrap" style="padding-bottom:4rem">
      <div class="headrow">
        <div>
          <p class="kicker">Explore SQF</p>
          <h2>Expertise for the next stage of growth.</h2>
        </div>
        <a class="btn ghost" href="services.html">Full catalogue</a>
      </div>
      <div class="cards" style="margin-top:1.5rem">
        <a class="card" href="services.html"><p class="num">01</p><h3>Management systems</h3><p>Quality, safety, environment, information security, food safety and responsible business.</p></a>
        <a class="card" href="audits.html"><p class="num">02</p><h3>Audits & verification</h3><p>Agreed criteria, practical gap identification and a clear view of supply-chain performance.</p></a>
        <a class="card" href="training.html"><p class="num">03</p><h3>Training & development</h3><p>Management system awareness, internal auditing, social accountability and automotive quality tools.</p></a>
        <a class="card" href="services.html#products"><p class="num">04</p><h3>Product compliance</h3><p>Guidance on product requirements, certification readiness, testing and inspection needs.</p></a>
      </div>
    </section>
    <section class="wrap split" style="padding-bottom:4rem">
      <div class="photos">
        <img src="assets/images/training-session.webp" alt="SQF trainer presenting to participants at a workshop">
        <img src="assets/images/learning-workshop.webp" alt="Workshop participants facing a trainer and presentation screen">
      </div>
      <div>
        <p class="kicker">People at the heart of quality</p>
        <h2>Learn together. Improve together.</h2>
        <p class="lede">Explore SQF’s training programmes, see moments from our workshops, and meet the organizations featured in the company profile.</p>
        <div class="row">
          <a class="btn ghost" href="training.html">Explore training</a>
          <a class="btn ghost" href="clients.html">Clients & gallery</a>
        </div>
      </div>
    </section>
    <section class="strip">
      <div class="wrap section">
        <div class="headrow">
          <div>
            <p class="kicker">Key clients — consulted services</p>
            <h2>Beside operations that take quality seriously.</h2>
          </div>
          <a href="clients.html"><strong>See the full list</strong></a>
        </div>
        <ul class="logos" style="margin-top:1.5rem">
          {"".join(f'<li class="logo"><img src="assets/images/clients/{file}" alt="{e(name)} logo"><span>{e(name)}</span></li>' for name, file in CLIENTS[:10])}
        </ul>
        <p class="fine">Logos identify organizations named in the company profile. The relationship is consultancy and training, not a certification claim.</p>
      </div>
    </section>
    {close()}
    """,
)

pages["about.html"] = shell(
    "about.html",
    "About SQF — Company Profile & Expertise | Shubhkiran Quality Forum",
    "Shubhkiran Quality Forum is a Nashik consultancy and training practice of auditors and engineers, established in 1999.",
    intro(
        "About us",
        "Experience that turns requirements into progress.",
        "We help organizations manage risk, strengthen management systems, and build the capability to keep improving.",
        f'<div class="row"><a class="btn ghost" href="assets/documents/sqf-company-profile.pdf">Download company profile</a><a class="btn ink" href="contact.html">Talk to SQF {ARROW}</a></div>',
    )
    + f"""
    <section class="wrap split" style="padding:2rem 0 4rem">
      <img class="cover" style="border-radius:1.25rem" src="assets/images/training-session.webp" alt="SQF workshop with a trainer and participants">
      <div>
        <p class="accent" style="font-weight:700">Since 1999</p>
        <h2>A practical partner for your organization.</h2>
        <p class="lede">Shubhkiran Quality Forum is a consultancy and training organization of experienced auditors and engineers. The work spans management systems, audit readiness, professional development, and technical and sustainability requirements.</p>
        <p class="muted">Led by <strong style="color:var(--ink)">Mr. Vilas Shinde</strong>, a mechanical engineer and lead auditor, SQF focuses on customized solutions, hands-on implementation, and knowledge transfer. An extensive network helps the practice assist organizations across India and support needs wherever they operate.</p>
        <blockquote class="quote"><p>“We believe in cultivating long-term relationships with our customers.”</p><footer class="muted">Shubhkiran Quality Forum</footer></blockquote>
      </div>
    </section>
    <section class="strip"><div class="wrap section">
      <p class="kicker">At a glance</p>
      <h2>Expertise with a wider perspective.</h2>
      <dl class="metrics" style="margin-top:1.5rem">
        <div class="metric"><strong>20+</strong><span>Technical experts</span></div>
        <div class="metric"><strong>~30</strong><span>Years in safety, security and sustainability</span></div>
        <div class="metric"><strong>2+</strong><span>Locations across India</span></div>
        <div class="metric"><strong>~15+</strong><span>SQF employees</span></div>
        <div class="metric"><strong>100%</strong><span>Independent and impartial</span></div>
      </dl>
      <p class="fine">Figures and the independence statement are as presented in the SQF company profile.</p>
    </div></section>
    <section class="wrap section">
      <p class="kicker">Achievements</p>
      <h2>A track record of supporting progress.</h2>
      <div class="cards-3" style="margin-top:1.5rem">
        <article class="card" style="background:var(--ink);color:var(--on-ink)"><p class="stat">1,500+</p><h3 style="margin-top:.8rem">Management system implementations</h3></article>
        <article class="card" style="background:var(--ink);color:var(--on-ink)"><p class="stat">100+</p><h3 style="margin-top:.8rem">Product certifications</h3></article>
        <article class="card" style="background:var(--ink);color:var(--on-ink)"><p class="stat">5,000+</p><h3 style="margin-top:.8rem">Personnel certifications</h3></article>
      </div>
      <p class="fine">Company-reported figures. Certification and approval arrangements depend on the applicable scheme.</p>
    </section>
    <section class="wrap split" style="padding-bottom:2rem">
      <div class="panel">
        <p class="kicker">Sustainability</p>
        <h2>Supporting the needs of tomorrow.</h2>
        <p class="muted">SQF’s company profile sets out its alignment with the United Nations Sustainable Development Goals and support for the Paris Climate Agreement through consultancy and training in sustainable management systems.</p>
        <p class="muted">The focus is on helping organizations understand risks and develop management systems that support safety, sustainability, and responsible business.</p>
        <a class="btn ghost" href="services.html#sustainability">Explore sustainability services</a>
      </div>
      <div>
        <p class="kicker">Why SQF</p>
        <h2>Clear advice. Practical value.</h2>
        <ul class="list">
          <li><h3>One-stop support</h3><p class="muted">Management system consultancy, product compliance readiness, testing and inspection support, and training.</p></li>
          <li><h3>A wider network</h3><p class="muted">A business network that supports local operations and requirements wherever organizations operate.</p></li>
          <li><h3>Added business value</h3><p class="muted">Vulnerabilities identified, with specific and clear recommendations for action.</p></li>
          <li><h3>Quality experts</h3><p class="muted">Experienced professionals with qualifications and a hands-on understanding of implementation.</p></li>
        </ul>
      </div>
    </section>
    {close()}
    """,
)

service_cards = []
for code, title, summary, area_i in SERVICES:
    blob = e(f"{code} {title} {summary} {AREAS[area_i]}".lower())
    service_cards.append(
        f'<article class="card" data-service data-area="{e(AREAS[area_i])}" data-text="{blob}">'
        f'<p class="num">{e(AREAS[area_i])}</p><h3>{e(code)}</h3><p><strong>{e(title)}</strong></p>'
        f'<p>{e(summary)}</p><p><a href="{contact(code)}"><strong>Enquire {ARROW}</strong></a></p></article>'
    )
chips = '<button class="chip" type="button" data-area-filter="all" aria-selected="true">All</button>' + "".join(
    f'<button class="chip" type="button" data-area-filter="{e(area)}">{e(area)}</button>' for area in AREAS
)
options = "".join(f'<option value="{e(code)}">{e(code)}</option>' for code, *_ in SERVICES) + "".join(
    f'<option value="{e(item)}">{e(item)}</option>' for item in EXTRAS
)
cycle = [
    ("Management systems & certification readiness", "System development, implementation support and preparation for external assessment."),
    ("Testing & product certification support", "Help understanding product requirements and the relevant testing or certification route."),
    ("Inspection support", "Discuss inspection needs within your product, process or supplier requirements."),
    ("Advisory & training", "Practical guidance and professional development to build internal capability."),
    ("Verification & validation", "Review the applicable requirements, scope and evidence needed for verification or validation."),
]
sectors = ["Chemical & Process", "Consumer Products & Retail", "Energy", "Healthcare & Medical Devices", "Infrastructure & Rail", "Manufacturing", "Mobility & Automotive", "Real Estate"]

pages["services.html"] = shell(
    "services.html",
    "Services — ISO, Sustainability & Product Compliance | Shubhkiran Quality Forum",
    "Explore SQF consultancy for management systems, sustainability, food safety, security, and product compliance readiness.",
    intro("Services", "The right expertise for your requirements.", "Management system consultancy, sustainability and social accountability, food safety, security, and product compliance readiness.")
    + f"""
    <section class="wrap" style="padding-bottom:2rem">
      <p class="kicker">Across the business cycle</p>
      <h2>Connected support, from requirements to readiness.</h2>
      <ol class="cards-5" style="margin-top:1.2rem;padding:0;list-style:none">
        {"".join(f'<li class="card"><p class="index">0{i+1}</p><h3 style="font-size:1rem;margin-top:.6rem">{e(t)}</h3><p>{e(b)}</p></li>' for i, (t, b) in enumerate(cycle))}
      </ol>
    </section>
    <section id="products" class="wrap" style="padding-bottom:2rem">
      <p class="kicker">Service catalogue</p>
      <h2>Find your standard. Plan your next step.</h2>
      <p class="lede">Search by a standard, scheme, industry or topic. Ask SQF to confirm the scope that applies to your organization.</p>
      <div class="panel" style="margin-top:1.2rem">
        <label for="catalogue-search"><strong>Search the catalogue</strong></label>
        <div class="search">{SEARCH}<input id="catalogue-search" placeholder="ISO 9001, IATF, food safety, BIS…"></div>
        <div class="filters" role="tablist" aria-label="Service area">{chips}</div>
      </div>
      <p class="note" data-count></p>
      <div class="empty" data-empty>
        <h3 class="display" style="font-size:1.6rem">Nothing matches that yet.</h3>
        <p class="muted">Try another term, or ask SQF to confirm the scope for your organization.</p>
        <p><a href="contact.html"><strong>Ask about this requirement {ARROW}</strong></a></p>
      </div>
      <div class="catalogue">{"".join(service_cards)}</div>
      <p class="note">SQF provides consultancy, training, and readiness support. Certification, product approvals, testing, inspection, verification, and validation vary by scheme. Consultancy does not itself confer certification or approval.</p>
    </section>
    <section id="sustainability" class="wrap">
      <p class="kicker">Sectors we serve</p>
      <h2>Different industries. The same commitment to quality.</h2>
      <ul class="pills">{"".join(f"<li>{e(s)}</li>" for s in sectors)}</ul>
      <p class="note">The practice also describes experience in electrical and electronics, pharmaceuticals, textiles, logistics, education, food, and other services.</p>
    </section>
    {close()}
    """,
)

tracks = [
    ("Management systems", "ISO 9001 · ISO 14001 · ISO 45001", "Training — Management systems", "assets/images/learning-workshop.webp", "Participants attending an SQF professional workshop", [
        "Internal auditor training on ISO 9001, ISO 14001 and ISO 45001",
        "Awareness of management systems and employee responsibilities",
        "Product life cycle awareness",
        "Environmental aspects and their impacts",
        "Hazard identification and risk assessment awareness (HIRAO)",
    ]),
    ("Social accountability", "SA8000 · WRAP · BSCI · ISO 26000 · SMETA", "Training — Social accountability", "assets/images/professional-training-group.webp", "SQF professional training group in a conference room", [
        "Internal auditor training covering social accountability standards and frameworks",
        "Awareness of corporate social responsibility policies",
        "Understanding applicable social and ethical accountability requirements",
    ]),
    ("Automotive quality", "IATF 16949 · Core tools · VDA", "Training — Automotive quality", "assets/images/training-session.webp", "Trainer presenting to participants at workshop tables", [
        "Internal auditor training on IATF 16949",
        "Awareness of the five core quality tools: APQP, PPAP, FMEA, MSA and SPC",
        "Awareness of VDA requirements",
    ]),
]
track_html = []
for title, codes, service, image, alt, points in tracks:
    lis = "".join(f"<li>{e(point)}</li>" for point in points)
    track_html.append(
        f'<article class="track"><img src="{image}" alt="{e(alt)}"><div class="copy"><p class="num">{e(codes)}</p>'
        f'<h3 class="display" style="font-size:1.8rem;margin-top:.4rem">{e(title)}</h3><ul class="checks">{lis}</ul>'
        f'<p><a href="{contact(service)}"><strong>Enquire about this track</strong></a></p></div></article>'
    )

pages["training.html"] = shell(
    "training.html",
    "Training & Personnel Development — ISO, Social & Automotive | Shubhkiran Quality Forum",
    "SQF training in management systems, social accountability and automotive quality tools, including internal auditor programmes.",
    intro(
        "Training",
        "Knowledge that works. People who improve.",
        "Build awareness, develop internal auditors, and strengthen practical quality skills with SQF’s professional training programmes.",
        f'<div class="row"><a class="btn" href="{contact("Training / Internal Audits")}">Discuss a programme {ARROW}</a></div>',
    )
    + f"""
    <section class="wrap">
      <p class="kicker">Programmes</p>
      <h2>Choose a learning path.</h2>
      <p class="lede">Share your team’s needs and SQF will discuss the topics and programme scope. Dates, delivery, duration and fees are confirmed with the team.</p>
      <div style="display:grid;gap:1rem;margin-top:1.5rem">{"".join(track_html)}</div>
    </section>
    <section class="wrap" style="padding:2rem 0">
      <div class="panel ink">
        <p class="kicker on-dark">Personnel certification</p>
        <h2>Build capability. Understand the pathway.</h2>
        <p>Training and personnel certification are part of the SQF portfolio. Discuss the programme, assessment, eligibility and certificate arrangements before booking.</p>
        <p><a href="clients.html#training-gallery"><strong>See the training community</strong></a></p>
      </div>
    </section>
    {close()}
    """,
)

pages["audits.html"] = shell(
    "audits.html",
    "Second-Party Audits, Verification & Inspection Support | Shubhkiran Quality Forum",
    "Second-party audit support against agreed quality, safety and environmental criteria, plus verification and inspection readiness.",
    intro(
        "Audits & verification",
        "A clear view. A stronger supply chain.",
        "Second-party audit support built around mutually agreed quality, safety, and environmental criteria.",
        f'<div class="row"><a class="btn" href="{contact("Second-party audits")}">Discuss an audit {ARROW}</a></div>',
    )
    + f"""
    <section class="wrap split" style="padding-bottom:2rem">
      <div>
        <p class="kicker">Second-party audits</p>
        <h2>Agreed criteria. Actionable findings.</h2>
        <p class="lede">Assess sites against a checklist that reflects your requirements. Use the findings to identify gaps, review performance, and plan follow-up.</p>
        <ul class="list">
          <li>Quality, safety and environmental aspects</li>
          <li>Suppliers, manufacturers and warehouses</li>
          <li>Checklists updated when requirements change</li>
          <li>Annual evaluation of each site’s performance</li>
        </ul>
      </div>
      <aside class="panel ink">
        <p class="kicker on-dark">Assessment frequency</p>
        <h3 class="display" style="font-size:1.6rem;margin-top:.6rem">A schedule shaped by audit results.</h3>
        <p>Frequency and scope are agreed for the engagement, based on site requirements and outcomes.</p>
        <ul class="pills"><li style="background:var(--on-ink);color:var(--ink)">Quarterly</li><li style="background:var(--on-ink);color:var(--ink)">Half-yearly</li><li style="background:var(--on-ink);color:var(--ink)">Yearly</li></ul>
      </aside>
    </section>
    <section class="wrap" style="padding-bottom:2rem">
      <p class="kicker">How it works</p>
      <h2>A practical audit cycle.</h2>
      <ol class="cards-4" style="margin-top:1.2rem;padding:0;list-style:none">
        <li class="card"><p class="index">01</p><h3>Agree the checklist</h3><p>Define the quality, safety and environmental criteria to be assessed.</p></li>
        <li class="card"><p class="index">02</p><h3>Assess the site</h3><p>Evaluate the site against the agreed scope and identify gaps.</p></li>
        <li class="card"><p class="index">03</p><h3>Review performance</h3><p>Use results to guide periodic assessments and annual site evaluation.</p></li>
        <li class="card"><p class="index">04</p><h3>Update and follow up</h3><p>Amend criteria when requirements change and track improvement needs.</p></li>
      </ol>
    </section>
    <section class="wrap">
      <p class="kicker">What you get</p>
      <h2>Confidence across the supply chain.</h2>
      <div class="cards" style="margin-top:1.2rem">
        <article class="card"><h3>Understand gaps</h3><p>Assess site quality and environmental, occupational health and safety aspects against identified needs.</p></article>
        <article class="card"><h3>External perspective</h3><p>Obtain an independent review against the criteria agreed for the audit engagement.</p></article>
        <article class="card"><h3>Adapt to change</h3><p>Update the checklist when requirements, processes or expectations change.</p></article>
        <article class="card"><h3>Consistent expectations</h3><p>Work towards agreed criteria across suppliers, manufacturers and warehouses.</p></article>
      </div>
      <div class="panel" style="margin-top:1rem;border-style:dashed">
        <h3 class="display" style="font-size:1.6rem">Verification, validation and inspection.</h3>
        <p class="muted">The profile also includes verification, validation, inspection, testing, and certification-related support across the business cycle. Contact SQF to discuss the relevant scope, methods, and delivery arrangements.</p>
        <a class="btn ink" href="{contact("Verification / validation / inspection")}">Discuss your scope {ARROW}</a>
      </div>
    </section>
    {close()}
    """,
)

gallery = [
    ("assets/images/training-participants.webp", "Training participants and the trainer gathered for a group photograph", "The people behind the progress", True),
    ("assets/images/recognition-ceremony.webp", "Bouquet presentation during a professional recognition gathering", "A moment of recognition", False),
    ("assets/images/professional-training-group.webp", "A professional training group posing together in a conference room", "Shared learning", False),
    ("assets/images/training-session.webp", "Participants listening to a trainer during a classroom session", "Knowledge into practice", False),
    ("assets/images/learning-workshop.webp", "A workshop with participants seated at tables facing the presentation screen", "Building capability", False),
]
shots = "".join(
    f'<li class="{"wide" if wide else ""}"><button class="shot" type="button" data-shot data-full="{src}" data-alt="{e(alt)}" data-caption="{e(cap)}"><img src="{src}" alt="{e(alt)}"><span>{e(cap)}</span></button></li>'
    for src, alt, cap, wide in gallery
)

pages["clients.html"] = shell(
    "clients.html",
    "Clients & Training Gallery | Shubhkiran Quality Forum",
    "Organizations featured in the SQF company profile, and photographs from the training community.",
    intro(
        "Clients",
        "Shared experience. Lasting relationships.",
        "Client references from the SQF company profile, and moments from the training community.",
        f'<div class="row"><a class="btn" href="contact.html">Work with SQF {ARROW}</a></div>',
    )
    + f"""
    <section class="wrap" style="padding-bottom:2rem">
      <p class="kicker">Client references</p>
      <h2>Organizations featured in the profile.</h2>
      <p class="note">Named under “Key Client — Consulted Services”. The relationship is consultancy and training, not a claim that SQF certified these organizations.</p>
      <ul class="logos" style="margin-top:1.2rem">{"".join(f'<li class="logo"><img src="assets/images/clients/{file}" alt="{e(name)} logo"><span>{e(name)}</span></li>' for name, file in CLIENTS)}</ul>
      <figure class="figure" style="margin-top:1.5rem">
        <img src="assets/images/profile-client-panel.webp" alt="Complete client reference panel from the SQF company profile, including all logos as supplied">
        <figcaption class="caption"><p class="muted" style="margin:0">The complete panel from the company profile, including additional logo-only entries.</p></figcaption>
      </figure>
    </section>
    <section id="training-gallery" class="wrap">
      <p class="kicker">Training community</p>
      <h2>Learning together. Growing stronger.</h2>
      <p class="lede">Select a photograph to view it larger.</p>
      <ul class="shots" style="margin-top:1rem;padding:0;list-style:none">{shots}</ul>
    </section>
    <div class="lightbox" data-lightbox role="dialog" aria-modal="true" aria-label="Photograph">
      <div class="frame">
        <img alt="">
        <div class="bar2">
          <p data-lightbox-caption></p>
          <div style="display:flex;gap:.5rem">
            <button class="icon-btn" type="button" data-prev aria-label="Previous photograph">‹</button>
            <button class="icon-btn" type="button" data-next aria-label="Next photograph">›</button>
            <button class="icon-btn" type="button" data-close aria-label="Close">×</button>
          </div>
        </div>
      </div>
    </div>
    {close()}
    """,
)

phones = [
    ("tel:+919370317764", "+91 93703 17764", "Vilas Shinde"),
    ("tel:+917875556741", "+91 78755 56741", "Mobile"),
    ("tel:+912532380070", "0253 2380070", "Office"),
]
phone_html = "".join(
    f'<li><a href="{href}">{PHONE}<span><strong>{num}</strong><span class="muted" style="display:block">{label}</span></span></a></li>'
    for href, num, label in phones
)

pages["contact.html"] = shell(
    "contact.html",
    "Contact SQF — Consultancy, Training & Audit Enquiries | Shubhkiran Quality Forum",
    "Talk to Shubhkiran Quality Forum in Nashik about consultancy, training, or audit readiness.",
    f"""
    <section class="wrap contact-grid" style="padding:3.2rem 0 4rem">
      <div>
        <p class="kicker">Let’s move forward</p>
        <h1>Your next step towards better.</h1>
        <p class="lede">Tell us where you are and where you want to go. We’ll discuss the right consultancy, training, or audit-readiness support.</p>
        <ul class="contacts">
          {phone_html}
          <li><a href="{WA_DISCUSS}">{PHONE}<span><strong>WhatsApp · +91 78755 56748</strong><span class="muted" style="display:block">Start a chat</span></span></a></li>
          <li><a href="mailto:shubhkiranquality@gmail.com">{MAIL}<span><strong>shubhkiranquality@gmail.com</strong></span></a></li>
          <li><a href="mailto:vishwaqc@gmail.com">{MAIL}<span><strong>vishwaqc@gmail.com</strong></span></a></li>
          <li><a href="{MAP}">{PIN}<span><strong>Visit the office</strong><span class="muted" style="display:block">{e(ADDRESS)}</span></span></a></li>
        </ul>
      </div>
      <form id="enquiry-form" class="panel">
        <h2>How can we help?</h2>
        <p class="muted">Share a few details. You review and send the message yourself.</p>
        <div class="form">
          <label class="field">Your name<input id="name" name="name" required autocomplete="name"></label>
          <label class="field">Company<input id="company" name="company" required autocomplete="organization"></label>
          <label class="field">I’m interested in
            <select id="service" name="service">{options}</select>
          </label>
          <label class="field">Your requirements<textarea id="message" name="message" rows="5" required></textarea></label>
        </div>
        <fieldset style="border:0;padding:0;margin:1rem 0 0">
          <legend style="font-weight:700;font-size:.875rem">Send using</legend>
          <div class="choices">
            <label><input type="radio" name="delivery" value="whatsapp" checked>WhatsApp</label>
            <label><input type="radio" name="delivery" value="email">Email</label>
          </div>
        </fieldset>
        <button class="btn wide" style="margin-top:1rem" type="submit" data-send>Prepare WhatsApp enquiry</button>
        <p id="form-status" class="note" role="status"></p>
      </form>
    </section>
    """,
)

for name, content in pages.items():
    (ROOT / name).write_text(content, encoding="utf-8")
    print(name, len(content))

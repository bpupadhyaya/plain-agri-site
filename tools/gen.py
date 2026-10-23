import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE="https://equalinformation.com/plain-agri-site/"
NAV=[("how-it-works","How it works"),("scales","Scales"),("climates","Climates"),("sample-plan","Sample plan"),("pricing","Pricing"),("about","About")]
SOON='<div class="badges"><div class="badge"><b>App Store</b>Coming soon</div><div class="badge"><b>Google Play</b>Coming soon</div></div>'
SHEET='''<div class="sheet-back"></div>
<div class="sheet" role="dialog" aria-modal="true" aria-label="Source viewer (demo)" aria-hidden="true">
<div class="sheet-grab"></div>
<div class="sheet-bar"><button data-act="back" aria-label="Back" disabled>&larr; Back</button><button data-act="fwd" aria-label="Forward" disabled>Forward &rarr;</button><div class="sheet-title"></div><button data-act="close" aria-label="Close source viewer">Close</button></div>
<div class="sheet-body"></div></div>'''
def page(slug,title,desc,body,sheet=False):
    d=0 if slug=="" else 1
    p="" if d==0 else "../"
    nav="".join('<li><a href="%s%s/"%s>%s</a></li>'%(p,s,' aria-current="page"' if s==slug else '',t) for s,t in NAV)
    html=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{slug+'/' if slug else ''}">
<link rel="icon" type="image/svg+xml" href="{p}assets/img/favicon.svg">
<meta name="theme-color" content="#2f5d3a">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PlainAgri">
<link rel="stylesheet" href="{p}assets/fonts/inter.css">
<link rel="stylesheet" href="{p}assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav aria-label="Main"><div class="nav-inner">
<a href="{p or './'}" class="nav-logo"><img src="{p}assets/img/favicon.svg" alt="" width="32" height="32"><span>PlainAgri</span></a>
<ul class="nav-links">{nav}</ul></div></nav>
<main id="main">
{body}
</main>
<footer><div class="wrap"><div class="cols">
<div><b>PlainAgri</b><p><small>Plan what to grow, where you are, with the resources around you. Any climate. Any scale.</small></p></div>
<div><b>Site</b><br><a href="{p}how-it-works/">How it works</a><br><a href="{p}sample-plan/">Sample plan</a><br><a href="{p}pricing/">Pricing</a></div>
<div><b>Help</b><br><a href="{p}support/">Support</a><br><a href="{p}privacy/">Privacy</a><br><a href="{p}about/">About</a></div>
</div><p><small>PlainAgri is general educational information, not a substitute for local agricultural advice or product labels. Always check local regulations before using any chemical input. &copy; EqualInformation LLC.</small></p></div></footer>
{SHEET if sheet else ''}
<script src="{p}assets/js/site.js" defer></script>
</body></html>'''
    out=os.path.join(ROOT,slug,"index.html") if slug else os.path.join(ROOT,"index.html")
    os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,"w").write(html)

LADDER=[("Hand","Single plants, pots, raised beds","Planting, watering and harvesting by hand."),
("Hand tools","Small plots and family gardens","Hoes, dibbers, watering cans, hand seeders and simple drip kits."),
("Animal draft","Working with draft animals","Ploughing, ridging and hauling where fuel and machines are scarce."),
("Small machinery","Walk-behind and compact tractors","Tillers, small seeders, pumps and sprinklers."),
("Large machinery","Full-size tractors and combines","Seed drills, planters, sprayers, harvesters and large irrigation systems."),
("Robotic and precision","Guided, sensor-driven farming","GPS-guided machines, robotic weeding and variable-rate application."),
("Aerial","Seeding and spraying from the air","Large-area aerial seeding and drone-based work, with safety and regulation in mind.")]
def ladder():
    return '<ul class="ladder">'+"".join(f'<li><span class="rung" style="--w:{i*12}"></span><div><b>{n} <span class="pill">{t}</span></b><span>{d}</span></div></li>' for i,(n,t,d) in enumerate(LADDER))+'</ul>'

# ---------- index ----------
page("","PlainAgri: Tell us where you are. We plan the rest.","PlainAgri designs a complete, cited growing plan from your location: any climate, any scale, from a single pot to robotic farming. Coming to iOS and Android.",f'''
<section class="hero"><div class="wrap">
<span class="eyebrow">Coming to iPhone and Android</span>
<h1>Tell us where you are.<br>PlainAgri plans the rest.</h1>
<p class="lead">Give the app your location. It works out your climate, what is realistic to grow, and which inputs and methods fit the resources around you, then lays it all out as a plan you can follow. Every claim is cited.</p>
<p><a class="btn" href="sample-plan/">See a sample plan</a> &nbsp; <a class="btn ghost" href="how-it-works/">How it works</a></p>
{SOON}
<p class="est">The first release is in development. Features on this site are what the first release is being built to do.</p>
</div></section>

<section><div class="wrap"><h2>Three steps, no jargon</h2><div class="grid">
<div class="card"><div class="n">1</div><h3>Say where</h3><p>Use your phone's location, search for a place, or pick one from a list. Planning a plot you are not standing on? That works too.</p></div>
<div class="card"><div class="n">2</div><h3>Say what for</h3><p>Food security, a garden, a small farm or a commercial operation, and the scale you work at. Every answer is optional and has a sensible default for your region.</p></div>
<div class="card"><div class="n">3</div><h3>Follow the plan</h3><p>Site and soil, what to grow, a hemisphere-aware calendar, planting, water, fertility, pests, harvest, storage, and a manual fallback at every step.</p></div>
</div></div></section>

<section class="alt"><div class="wrap"><h2>From one plant to a whole landscape</h2>
<p class="lead">Agriculture is whatever grows food, fibre or soil, at whatever scale. PlainAgri is being built to cover the whole range, so the plan matches how you actually work.</p>
{ladder()}
<p><a href="scales/">More on the scales &rarr;</a></p></div></section>

<section><div class="wrap"><h2>Any climate, anywhere</h2>
<p class="lead">Tropical rainforest to cold continental winters, arid deserts to mountain gardens. Your place resolves to its climate zone, and the advice changes with it.</p>
<p><a href="climates/">Explore the climate zones &rarr;</a></p></div></section>

<section class="alt"><div class="wrap"><h2>Cited, and one tap from the source</h2>
<p class="lead">Every cited claim carries a small source chip. Tap it and the source opens inside the app in a sheet covering 80 percent of the screen, with Back, Forward and Close, so you always return to exactly where you were. Try the demo:</p>
<p>Soils rich in organic matter generally hold more water and drain better than depleted soils.<button class="cite" data-cite="soils" aria-label="Open source (demo)">1</button></p>
<p class="est">Demo only. In the app the chip opens the real source.</p></div></section>

<section><div class="wrap"><h2>Private and offline-first</h2><ul class="tick">
<li>The baseline library and your plan are designed to work with no signal, in the field.</li>
<li>No accounts, no analytics, no ad trackers. Your location stays on your device.</li>
<li>Where something is a regional estimate (for example which fertilizers are typical near you), the app says so plainly.</li></ul>
<p><a class="btn" href="pricing/">Free outline, Pro for the full plan</a></p></div></section>
''',sheet=True)

# ---------- how it works ----------
page("how-it-works","How PlainAgri works","From a location to a full, cited growing plan: how PlainAgri turns where you are into what to do.",f'''
<section class="hero"><div class="wrap"><span class="eyebrow">How it works</span><h1>Location in. Plan out.</h1>
<p class="lead">PlainAgri is being built around one idea: the right advice depends on where you are and what you have. So it starts with the place.</p></div></section>
<section><div class="wrap"><div class="grid">
<div class="card"><div class="n">1</div><h3>Your place</h3><p>GPS, search, or a pick from region, country and place. An arbitrary point resolves to the nearest reference place, and the app tells you which one and how far.</p></div>
<div class="card"><div class="n">2</div><h3>Your climate and region</h3><p>The place maps to a climate zone, a hemisphere (so the calendar flips correctly) and a typical level of market and supply access.</p></div>
<div class="card"><div class="n">3</div><h3>Your goals and scale</h3><p>Food security, gardening, a small farm or a commercial operation; hand tools through to robotic and aerial. Water: rain only, well, piped, canal or unreliable.</p></div>
<div class="card"><div class="n">4</div><h3>Your plan</h3><p>An ordered plan assembled from the content library by matching your climate, scale and region, with a manual option always shown alongside machine options.</p></div></div>
<h2 style="margin-top:40px">What a plan covers</h2>
<ul class="tick"><li>Site and soil</li><li>What to grow here, ranked for your climate</li><li>A hemisphere-aware calendar</li><li>Planting method for your scale</li><li>Water</li><li>Soil fertility and the inputs typically available in your region</li><li>Pests and disease, with low-risk options first</li><li>Harvest method for your scale</li><li>Storage and post-harvest</li><li>Equipment and supply-chain defaults</li><li>Risks and next steps</li></ul>
<div class="note"><b>Honest by design.</b> Where information is a regional estimate rather than a fact about your specific town, the app labels it as typical for your region. Chemical and fertilizer content always points you to local rules and product labels.</div>
<p><a class="btn" href="../sample-plan/">See a sample plan</a></p></div></section>''')

# ---------- scales ----------
page("scales","Every scale of growing","From a single plant by hand to robotic and aerial farming: PlainAgri is being built to cover the whole range.",f'''
<section class="hero"><div class="wrap"><span class="eyebrow">Scales</span><h1>Whatever you grow with, the plan fits.</h1>
<p class="lead">Planting, watering and harvesting look very different on a balcony and on ten thousand hectares. PlainAgri tailors each part of the plan to the scale you choose, and always keeps a manual fallback in view.</p></div></section>
<section><div class="wrap">{ladder()}
<div class="note">Machine and aerial work carry safety and legal requirements that vary by country. The plan covers them in general terms and points you to local rules.</div></div></section>''')

# ---------- climates ----------
zbtn="".join(f'<button type="button" data-z="{k}" aria-pressed="false">{n}</button>' for k,n in [("A","Tropical"),("B","Arid"),("C","Temperate"),("D","Continental"),("E","Polar and alpine")])
page("climates","Any climate: explore the zones","PlainAgri maps your place to its climate zone and changes the advice with it. Explore sample snippets for each major zone.",f'''
<section class="hero"><div class="wrap"><span class="eyebrow">Climates</span><h1>Same crop, different climate, different plan.</h1>
<p class="lead">PlainAgri uses the Koppen climate groups, refined to individual zones in the app. Pick a group to see the kind of guidance it changes.</p></div></section>
<section><div class="wrap"><div class="zones" role="group" aria-label="Climate groups">{zbtn}</div>
<div class="card zone-out" id="zone-out" aria-live="polite"></div>
<p class="est">These are short, general samples. The app picks the zone for your exact place and builds a complete, cited plan.</p></div></section>''')

# ---------- sample plan ----------
page("sample-plan","Sample plan: a small plot near Nairobi","A sample PlainAgri plan for a hand-tool plot near Nairobi, Kenya, to show what the app produces. The full library lives in the app.",f'''
<section class="hero"><div class="wrap"><span class="eyebrow">Sample plan</span><h1>A plot near Nairobi, Kenya</h1>
<p class="lead">An illustration of the format the first release is being built to produce. Place: Nairobi (highland, temperate oceanic climate, elevation around 1,800 m). Purpose: food for a household. Scale: hand tools. Water: rain only.</p>
<p><span class="pill">Illustrative sample</span> <span class="pill">Not for site-specific decisions</span></p></div></section>
<section><div class="wrap">
<div class="note"><b>This is a sample.</b> It shows the shape and tone of a plan. A real plan is built from the content library for your exact place, and it includes every section in full, with citations that open in the app. Local conditions vary; confirm timings with a local extension office.</div>
<div class="card"><h3>1. Site and soil</h3><p>Choose the flattest, best-drained part of the plot, away from low spots where water pools. Check the soil by squeezing a moist handful: a ball that holds and then crumbles is a good sign; one that stays sticky or will not hold together needs different handling.</p><p class="est">Typical for the region: highland soils are often well-drained but can be low in organic matter. Estimate; test your own soil.</p></div><br>
<div class="card"><h3>2. What to grow here</h3><p>This highland climate suits maize, beans, leafy greens such as kale, and potatoes. Mixing a cereal with a legume on the same plot is a long-standing way to spread risk and help soil fertility.</p></div><br>
<div class="card"><h3>3. Calendar</h3><p>Rainfall in this region is typically in two seasons: a longer one in roughly March to May and a shorter one in roughly October to December.</p>
<table><tr><th>Crop</th><th>Sow around</th><th>Harvest around</th></tr>
<tr><td>Maize and beans</td><td>Start of the long rains</td><td>Several months later, once dry</td></tr>
<tr><td>Kale</td><td>Either season</td><td>Pick leaves continuously</td></tr></table>
<p class="est">Months are shown as seasons here to avoid false precision. The app gives hemisphere-aware months for your place.</p></div><br>
<div class="card locked"><h3>4. Planting by hand</h3><p>Spacing, depth, and a step-by-step method for sowing by hand and with simple tools.</p><p><i>Complete steps, spacing tables and troubleshooting are in the app.</i></p></div><br>
<div class="card locked"><h3>5. Water</h3><p>Making the most of rain only: mulching, planting basins and when to water if the rains fail.</p></div><br>
<div class="card locked"><h3>6. Fertility and inputs</h3><p>Compost, manure and the inputs typically available in your region, with a manual option first.</p></div><br>
<div class="card locked"><h3>7. Pests and disease</h3><p>Low-risk options first, with sources.</p></div><br>
<div class="card locked"><h3>8. Harvest, storage and next steps</h3><p>Harvest timing, drying, safe storage, and what to do next season.</p></div>
<p style="margin-top:28px"><a class="btn" href="../pricing/">Get the full plan in the app</a></p>
</div></section>''')

# ---------- pricing ----------
page("pricing","Pricing","PlainAgri is a subscription app with a free outline and a Pro plan for the full plan and library. Prices are placeholders and subject to change.",f'''
<section class="hero"><div class="wrap"><span class="eyebrow">Pricing</span><h1>Start free. Go Pro for the whole plan.</h1>
<p class="lead">One app, one subscription. Prices below are placeholders and subject to change before launch.</p></div></section>
<section><div class="wrap"><div class="grid">
<div class="card"><h3>Free</h3><div class="price">$0</div><ul class="tick"><li>Choose your location</li><li>Your plan outline: every section, with a teaser</li><li>The library index</li></ul></div>
<div class="card"><h3>Pro monthly</h3><div class="price">$4.99<small> / month</small></div><ul class="tick"><li>Full plan for your place</li><li>Full library</li><li>Saved plans</li></ul><p class="est">Subject to change.</p></div>
<div class="card"><h3>Pro yearly</h3><div class="price">$39.99<small> / year</small></div><ul class="tick"><li>Everything in Pro monthly</li><li>Lower cost over a year</li></ul><p class="est">Subject to change.</p></div></div>
<p>Subscriptions are billed and managed through the App Store or Google Play, and can be cancelled there at any time. {SOON}</p></div></section>''')

# ---------- privacy ----------
page("privacy","Privacy","PlainAgri has no accounts, no analytics and no ad trackers. Your location stays on your device.",f'''
<section class="hero"><div class="wrap"><h1>Privacy</h1><p class="lead">PlainAgri is designed to know as little about you as possible.</p></div></section>
<section><div class="wrap">
<h2>The app</h2><ul class="tick"><li>No accounts and no sign-in.</li><li>No analytics, advertising or crash-reporting services.</li><li>Your location is used on your device to find your nearest reference place and is not sent to us.</li><li>Your profile, saved plans and bookmarks stay on your device.</li><li>The only network use planned for the first release is opening a source when you tap a citation, and your store handling subscriptions.</li></ul>
<h2>This website</h2><p>This site sets no cookies and uses no analytics, trackers or third-party fonts or scripts.</p>
<h2>Subscriptions</h2><p>Payments are processed by Apple or Google. We do not receive your payment details.</p>
<h2>Contact</h2><p><a href="mailto:contact@equalinformation.com?subject=PlainAgri%20Privacy">contact@equalinformation.com</a></p>
<p class="est">This page describes the planned first release and will be updated if that changes.</p></div></section>''')

# ---------- support ----------
page("support","Support","Get help or send feedback about PlainAgri.",f'''
<section class="hero"><div class="wrap"><h1>Support</h1><p class="lead">The app is not released yet. Questions and feedback are welcome now.</p></div></section>
<section><div class="wrap"><p><a class="btn" href="mailto:contact@equalinformation.com?subject=PlainAgri%20Feedback">Email us</a></p>
<h2>Common questions</h2>
<h3>Does it work offline?</h3><p>That is the design: the baseline library and plan are meant to work without signal.</p>
<h3>Is the advice a substitute for a local expert?</h3><p>No. PlainAgri is general information. Confirm timings and any chemical use with local extension services and product labels.</p>
<h3>How do I cancel a subscription?</h3><p>Through your App Store or Google Play subscription settings.</p></div></section>''')

# ---------- about ----------
page("about","About PlainAgri","PlainAgri is built by one highly experienced engineer, amplified by the world's most advanced AI agents.",f'''
<section class="hero"><div class="wrap"><span class="eyebrow">About</span><h1>One engineer, one mission.</h1>
<p class="lead">PlainAgri is built by a highly experienced engineer, amplified by the world's most advanced AI agents: the craftsmanship of a dedicated expert with the capacity of a world-class engineering team.</p></div></section>
<section><div class="wrap"><p>The mission is simple: anyone, anywhere, should be able to plan what to grow from the resources around them, in plain language, with sources they can check. PlainAgri is part of the Plain family of apps from EqualInformation.</p>
<p class="est">Content is cited, and nothing is described as expert-reviewed until a named expert has signed off.</p></div></section>''')

# ---------- sitemap/robots ----------
slugs=[""]+[s for s,_ in NAV]+["privacy","support"]
open(os.path.join(ROOT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{s+'/' if s else ''}</loc></url>\n" for s in slugs)+'</urlset>\n')
open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")

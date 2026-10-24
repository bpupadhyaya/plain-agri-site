import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE="https://equalinformation.com/plain-agri-site/"
NAV=[("how-it-works","How it works"),("features","Features"),("try","Try it"),("scales","Scales"),("climates","Climates"),("sample-plan","Sample plan"),("pricing","Pricing"),("about","About")]
SOON='<div class="badges"><div class="badge"><b>App Store</b>Coming soon</div><div class="badge"><b>Google Play</b>Coming soon</div></div>'
SHEET='''<div class="sheet-back"></div>
<div class="sheet" role="dialog" aria-modal="true" aria-label="Source viewer (demo)" aria-hidden="true">
<div class="sheet-grab"></div>
<div class="sheet-bar"><button data-act="back" aria-label="Back" disabled>&larr; Back</button><button data-act="fwd" aria-label="Forward" disabled>Forward &rarr;</button><div class="sheet-title"></div><button data-act="close" aria-label="Close source viewer">Close</button></div>
<div class="sheet-body"></div></div>'''
def page(slug,title,desc,body,sheet=False,scripts=""):
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
<meta name="theme-color" content="#0b3d2e">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PlainAgri">
<link rel="stylesheet" href="{p}assets/fonts/inter.css">
<link rel="stylesheet" href="{p}assets/css/style.css?v=4">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav aria-label="Main"><div class="nav-inner">
<a href="{p or './'}" class="nav-logo"><img src="{p}assets/img/favicon.svg" alt="" width="32" height="32"><span>PlainAgri</span></a>
<ul class="nav-links">{nav}</ul><button class="mobile-menu-btn" onclick="document.querySelector('.nav-links').classList.toggle('show')" aria-label="Menu">&#9776;</button></div></nav>
<main id="main">
{body}
</main>
<footer><details class="footer-dock"><summary><span class="dock-links"><a href="{p or './'}">Home</a><a href="{p}privacy/">Privacy</a><a href="{p}support/">Support</a></span><span class="dock-copy">&copy; 2026 EqualInformation, LLC</span><span class="dock-more">More</span></summary>
<div class="footer-inner"><ul class="footer-links"><li><a href="{p}how-it-works/">How it works</a></li><li><a href="{p}features/">Features</a></li><li><a href="{p}try/">Try it</a></li><li><a href="{p}scales/">Scales</a></li><li><a href="{p}climates/">Climates</a></li><li><a href="{p}sample-plan/">Sample plan</a></li><li><a href="{p}pricing/">Pricing</a></li><li><a href="{p}about/">About</a></li><li><a href="{p}privacy/">Privacy Policy</a></li><li><a href="{p}support/">Support</a></li><li><a href="https://equalinformation.com" target="_blank" rel="noopener">EqualInformation</a></li></ul>
<p class="footer-copy">PlainAgri is general educational information, not a substitute for local agricultural advice or product labels. Always check local regulations before using any chemical input. &copy; 2026 EqualInformation, LLC.</p></div></details></footer>
{SHEET if sheet else ''}
{''.join('<script src="'+p+'assets/js/'+x+'" defer></script>' for x in scripts.split())}
<script src="{p}assets/js/site.js" defer></script>
{('<script src="'+p+'assets/js/demos.js" defer></script>') if scripts else ''}
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


<section class="alt"><div class="wrap"><h2>See it in the app</h2>
<p class="lead">Real screens from the first-release build on iPhone and Android. These are a taste: the full plan, the whole library and saved plans are in the app.</p>
<div class="shots">
<figure><div class="phone"><img src="assets/img/app/plan.jpg?v=4" alt="PlainAgri plan screen for Nairobi showing climate zone, setup and plan sections" loading="lazy"></div><figcaption>Your place, your setup, your plan</figcaption></figure>
<figure><div class="phone"><img src="assets/img/app/crops.jpg?v=4" alt="PlainAgri what to grow here screen" loading="lazy"></div><figcaption>Crops that suit your climate</figcaption></figure>
<figure><div class="phone"><img src="assets/img/app/machinery.jpg?v=4" alt="PlainAgri guidance for machinery scale" loading="lazy"></div><figcaption>Methods that match your scale</figcaption></figure>
<figure><div class="phone"><img src="assets/img/app/sources.jpg?v=4" alt="PlainAgri in-app source viewer opened at 80 percent height" loading="lazy"></div><figcaption>Every source opens in the app</figcaption></figure>
<figure><div class="phone android"><img src="assets/img/app/android-water.jpg?v=4" alt="PlainAgri rainwater calculator on Android" loading="lazy"></div><figcaption>Calculators on Android, with the formula showing</figcaption></figure>
</div></div></section>

<section><div class="wrap"><h2>More than a plan: a whole toolbox</h2>
<p class="lead">Around the plan sits a growing library that works the way a good extension officer would: diagnose a sick plant, size a water tank, pick a machine, look up a word.</p>
<div class="grid">
<div class="card"><h3>Diagnose</h3><p>Answer a few plain questions about what you see. Get likely causes, what to check, what to do and what to avoid. 50 walk-throughs.</p></div>
<div class="card"><h3>Calculators</h3><p>Rainwater, irrigation, plant counts, seed rate, fertilizer, compost, storage and sowing dates, with the formula shown.</p></div>
<div class="card"><h3>Equipment</h3><p>134 tools and machines from a dibber to a drone, filtered by scale, each with a manual alternative.</p></div>
<div class="card"><h3>My Plots</h3><p>Save your plots and get a season task list. Optional reminders are created on your device and nothing leaves it.</p></div>
<div class="card"><h3>Glossary</h3><p>271 terms in plain words. Tap an underlined word in any guide to see what it means.</p></div>
<div class="card"><h3>Zoom, your way</h3><p>Make text anything from 50 to 300 percent, on every screen, on every device.</p></div>
</div>
<p><a class="btn" href="features/">See every feature</a> <a class="btn ghost" href="try/">Try a calculator or a diagnosis</a></p>
<p class="est">In the library today: 515 places in 175 countries, 69 crops with full guides, a searchable library of 2,043 plants, 421 documents and 627 cited sources. Guides are AI-drafted and spot-checked; nothing is called expert-reviewed until a named expert signs off.</p></div></section>

<section class="alt"><div class="wrap"><h2>Any climate, anywhere</h2>
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
<h2 style="margin-top:40px">Beyond the plan</h2>
<p class="lead">The plan is the spine. Around it the app adds tools you reach for through the season.</p>
<ul class="tick"><li>Learn: guides, crops, diagnoses, calculators, equipment and a glossary, with one search across all of them</li><li>My Plots: save plots, see a season task list, and turn on reminders that are scheduled on your device</li><li>This month: what to sow, tend and harvest now, at the top of your plan</li><li>Export: turn a plan into a PDF with numbered sources</li><li>Zoom: text from 50 to 300 percent everywhere</li></ul>
<p><a class="btn" href="../features/">See the features</a> <a class="btn ghost" href="../try/">Try it</a> <a class="btn ghost" href="../sample-plan/">See a sample plan</a></p></div></section>''')

# ---------- scales ----------
page("scales","Every scale of growing","From a single plant by hand to robotic and aerial farming: PlainAgri is being built to cover the whole range.",f'''
<section class="hero"><div class="wrap"><span class="eyebrow">Scales</span><h1>Whatever you grow with, the plan fits.</h1>
<p class="lead">Planting, watering and harvesting look very different on a balcony and on ten thousand hectares. PlainAgri tailors each part of the plan to the scale you choose, and always keeps a manual fallback in view.</p></div></section>
<section><div class="wrap">{ladder()}
<p>Each scale also has an equipment list in the app: 134 tools and machines in all, from hand tools and draft-animal gear to centre-pivot irrigation, combine harvesters, robotic weeders, drones and aerial seeding. Every item notes what it needs, the area it suits, and a manual alternative. <a href="../features/#equipment">See the equipment explorer &rarr;</a></p>
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
<p class="lead">An illustration of the format the first release is being built to produce. Place: Nairobi (subtropical highland climate with a dry winter, elevation around 1,800 m). Purpose: food for a household. Scale: hand tools. Water: rain only.</p>
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
<div class="card"><h3>Free</h3><div class="price">$0</div><ul class="tick"><li>Choose your location</li><li>Your plan outline: every section, with a teaser</li><li>Glossary and the equipment list</li><li>Two calculators: rainwater harvest and when to sow</li><li>Three diagnosis walk-throughs</li><li>Crop facts</li><li>Text zoom 50 to 300 percent</li></ul></div>
<div class="card"><h3>Pro monthly</h3><div class="price">$4.99<small> / month</small></div><ul class="tick"><li>Full plan for your place</li><li>Crop growing guides and the full library</li><li>All 13 calculators and all 50 diagnoses</li><li>Plant Finder pages, planning tools and layouts</li><li>My Farm records: diary, harvest, money, stock</li><li>My Plots with season tasks and reminders</li><li>PDF plan export</li><li>Saved plans and results</li></ul><p class="est">Subject to change.</p></div>
<div class="card"><h3>Pro yearly</h3><div class="price">$39.99<small> / year</small></div><ul class="tick"><li>Everything in Pro monthly</li><li>Lower cost over a year</li></ul><p class="est">Subject to change.</p></div></div>
<p>Subscriptions are billed and managed through the App Store or Google Play, and can be cancelled there at any time. {SOON}</p></div></section>''')

# ---------- privacy ----------
page("privacy","Privacy","PlainAgri has no accounts, no analytics and no ad trackers. Your location stays on your device.",f'''
<section class="hero"><div class="wrap"><h1>Privacy</h1><p class="lead">PlainAgri is designed to know as little about you as possible.</p></div></section>
<section><div class="wrap">
<h2>The app</h2><ul class="tick"><li>No accounts and no sign-in.</li><li>No analytics, advertising or crash-reporting services.</li><li>Your location is used on your device to find your nearest reference place and is not sent to us.</li><li>Your profile, saved plans and bookmarks stay on your device.</li><li>The only network use planned for the first release is opening a source when you tap a citation, and your store handling subscriptions.</li></ul>
<h2>This website</h2><p>This site sets no cookies and uses no analytics, trackers or third-party fonts or scripts.</p>
<h2>Subscriptions</h2><p>Payments are processed by Apple or Google. We do not receive your payment details.</p>
<h2>Contact</h2><p><a href="mailto:privacy@equalinformation.com?subject=PlainAgri%20Privacy">privacy@equalinformation.com</a></p>
<p class="est">This page describes the planned first release and will be updated if that changes.</p></div></section>''')

# ---------- support ----------
page("support","Support","Get help or send feedback about PlainAgri.",f'''
<section class="hero"><div class="wrap"><h1>Support</h1><p class="lead">The app is not released yet. Questions and feedback are welcome now.</p></div></section>
<section><div class="wrap"><p><a class="btn" href="mailto:support@equalinformation.com?subject=PlainAgri%20Feedback">Email us</a></p>
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

# ---------- features ----------
def ph(img,alt,android=False):
    return f'<figure class="phone{" android" if android else ""}"><img src="../assets/img/app/{img}?v=4" alt="{alt}" loading="lazy"></figure>'
def feat(fid,title,tags,text,imgs,rev=False):
    t="".join(f'<span class="tag{" pro" if x.startswith("Pro") else ""}">{x}</span>' for x in tags)
    return f'<div class="feat{" rev" if rev else ""}" id="{fid}"><div><h2>{title}</h2><p>{t}</p>{text}</div><div class="feat-img">{imgs}</div></div>'
FEATS=[
 feat("learn","A library you can search",["Free: index and search","Pro: full guides"],"<p>Learn is one hub for Guides, Crops, Diagnose, Calculators, Equipment and Glossary, with a single search box across all of them. Plan and Saved link straight into it.</p><p class=\"est\">515 places, 69 crops with full guides, 421 documents and 627 cited sources are in the library today.</p>",ph("ios-learn.jpg","PlainAgri Learn hub with six tiles and a search box")+ph("ios-search.jpg","PlainAgri search results across crops, guides and glossary")),
 feat("plants","Search thousands of plants",["Free: search","Pro: full pages"],"<p>Plant Finder is a searchable library of 2,043 cultivated and useful plants, with 68 plain how-to-grow guides by plant type (trees, vines, bulbs, herbs and more). Switch on the filter for your place and it shows plants whose climate figures do not rule them out there. That is a screen, not a recommendation.</p><p class=\"est\">Not every plant: the 69 main crops have full guides, and most other entries are overviews with a general method. Names, uses and fit are drawn from licensed open data and are not expert-reviewed.</p>",ph("ios-plants.jpg","PlainAgri Plant Finder search results")+ph("ios-suits.jpg","PlainAgri Plant Finder filtered to plants not ruled out for a place")+ph("ios-howto.jpg","PlainAgri How to grow hub with plant-type guides")+ph("and-plants.jpg","Plant Finder on Android",True)),
 feat("invasive","Invasive and restricted plants flagged",["Free"],"<p>356 plants carry an invasive, noxious or weedy flag, with the regions and the source. 78 of them are hidden from suggestions and appear only if you search the exact name. Flags come mostly from United States lists, so no flag does not mean a plant is safe or legal where you live. Check your local rules.</p>",ph("ios-invasive.jpg","PlainAgri invasive plant warning card")+ph("and-invasive.jpg","Invasive warning on Android",True),True),
 feat("tools","Planning tools from your place",["Free: What I have","Pro: plan builder and layouts"],"<p>Tell the app your water, soil, land and tools, and it builds a plan from them. Lay out beds, plan a rotation, see monthly climate for your place, read a soil test, and schedule irrigation. Everything is calculated on your device, and every estimate is labelled as one.</p>",ph("ios-tools.jpg","PlainAgri planning tools hub")+ph("ios-builtplan.jpg","PlainAgri plan built from what you have")+ph("ios-bed.jpg","PlainAgri bed layout")+ph("and-tools.jpg","Planning tools on Android",True)),
 feat("farm","My Farm: your records in one place",["Pro"],"<p>Keep a diary with photos, a harvest log, a simple money ledger and an inventory, then see them on a calendar. Follow a learning path, take notes, and back everything up to a file you keep. It stays on your device: no account, no server, no analytics. Widgets and shortcuts are included.</p>",ph("ios-farm.jpg","PlainAgri My Farm hub")+ph("ios-diary.jpg","PlainAgri farm diary")+ph("ios-money.jpg","PlainAgri money ledger")+ph("and-farm.jpg","My Farm on Android",True)+ph("and-money.jpg","Money ledger on Android",True),True),
 feat("crops","Crop pages for your place",["Free: crop facts","Pro: growing guide"],"<p>Pick a crop to see when it can be sown and harvested where you are, with days to maturity, a spacing sketch, sowing depth, water need, yield range and companion crops, all clearly labelled as estimates. The growing guide and an Add to my plot button are in Pro.</p>",ph("ios-crop.jpg","PlainAgri crop page showing season, spacing and water need"),True),
 feat("diagnose","Diagnose what you see",["Free: 3 walk-throughs","Pro: all 50"],"<p>Answer a few plain questions about the leaves, the fruit or the stored grain. You get likely or possible causes, what to check, what to do and what to avoid, each with sources. Results are never presented as a certainty, and chemical advice always points you to labels and local rules.</p><p><a class=\"btn ghost\" href=\"../try/#diagnose\">Walk a real diagnosis</a></p>",ph("ios-diagq.jpg","PlainAgri diagnosis question card")+ph("ios-diagr.jpg","PlainAgri diagnosis result with check, do and avoid")),
 feat("calculators","Calculators with the formula showing",["Free: rainwater, when to sow","Pro: all 13"],"<p>Size a rainwater tank, work out how much irrigation water a bed needs, count plants and seed, plan fertilizer from a nutrient target, balance a compost heap, estimate storage space, and find your latest sowing date. Every calculator states its formula and assumptions and cites its sources.</p><p><a class=\"btn ghost\" href=\"../try/#calculators\">Try two of them</a></p>",ph("ios-calc.jpg","PlainAgri calculator with inputs, results and formula")),
 feat("plots","My Plots and a season task list",["Pro"],"<p>Save each plot with its place, area, scale, water and crops. The app builds a season task list: prepare the soil, sow, harvest, with the calendar shifted correctly for your hemisphere and the equator. Reminders are optional, switched on per plot, and scheduled on your device. Nothing is sent anywhere.</p>",ph("ios-plot.jpg","PlainAgri plot with season tasks")+ph("and-reminder.jpg","Android reminder notification listing jobs due on plots",True),True),
 feat("this-month","This month, at the top",["Free: outline","Pro: your plots"],"<p>Open the Plan tab and the first card says what to sow now, what to harvest now and what is coming next month for your place. With plots saved, your own open tasks join it.</p>",ph("and-this-month.jpg","PlainAgri This month card on Android",True)),
 feat("glossary","Words explained, right where you read them",["Free"],"<p>271 terms in plain language. In plan and guide text, an underlined word opens a short definition with related terms and sources, then closes back to exactly where you were.</p>",ph("ios-term.jpg","PlainAgri glossary definition sheet over a guide")+ph("ios-doc.jpg","PlainAgri guide with underlined glossary terms"),True),
 feat("equipment","Equipment from a dibber to a drone",["Free: the list"],"<p>134 tools and machines across all seven scales: hand tools, draft animals, small and large machinery, robotic and precision systems, and aerial work. Filter by scale and kind, and every entry says what it needs, the area it suits and the manual alternative.</p>",ph("ios-equip.jpg","PlainAgri equipment detail with needs, area and manual alternative")),
 feat("export","Take your plan with you",["Pro"],"<p>Export a plan, or one plot's plan, as a PDF with every section and a numbered source list with web addresses, and share it with the system share sheet. Handy for a co-op meeting, an extension visit or a landlord.</p>",'<p class="est">The PDF is plain and printable: your place and setup, each plan section, and a numbered list of sources.</p>'),
 feat("zoom","Text size that fits you",["Free, everywhere"],"<p>Every screen has an A- and A+ control with the exact percentage, from 50 to 300 percent. It scales the whole app, including the tab bar and sheets, on phones, tablets and foldables, and layouts reflow instead of cutting words off. <a href=\"../try/#zoom\">Try the zoom</a>.</p>",ph("zoom-50.jpg","PlainAgri plan at 50 percent text size")+ph("zoom-100.jpg","PlainAgri plan at 100 percent text size")+ph("zoom-300.jpg","PlainAgri plan at 300 percent text size"),True),
 feat("themes","Your colours, NutriSize by default",["Free, everywhere"],"<p>The app opens in the clean NutriSize Health look: white and soft green with deep green and blue accents, always light. If you prefer something else, Appearance in the About tab offers Field (warm earth tones) and Night (dark). Your choice is saved on your device.</p>","",True),
 feat("devices","Fluid on every device",["Free"],"<p>Layouts adapt from small phones to tablets: reading width is capped and centred on wide screens, bars tuck away while you scroll at large text sizes, and the app rotates on iPad and Android. Checked on a range of simulated phones, tablets and a foldable.</p>",f'<figure class="phone" style="width:min(420px,90vw);aspect-ratio:auto"><img src="../assets/img/app/ipad-plan.jpg?v=4" alt="PlainAgri plan on an iPad" loading="lazy" style="object-fit:contain"></figure>'),
]
page("features","Features: what PlainAgri does","Everything in the first release of PlainAgri: plan, plant library, planning tools, My Farm records, diagnose, calculators, equipment, glossary, export and text zoom, with real screenshots.",f'''
<section class="hero"><div class="wrap"><span class="eyebrow">Features</span><h1>A plan, and the tools to carry it out.</h1>
<p class="lead">These screens are from the first-release build on iPhone and Android. It is not in the stores yet. Free shows you enough to judge it; Pro opens the whole library.</p>
<p><a class="btn" href="../try/">Try it in your browser</a> <a class="btn ghost" href="../pricing/">Free and Pro</a></p></div></section>
<section><div class="wrap">{"".join(FEATS)}
<p class="est">Screens show sample places and plots. Guides are AI-drafted and spot-checked; nothing is called expert-reviewed until a named expert signs off. Always confirm local conditions and product labels.</p></div></section>''')

# ---------- try ----------
page("try","Try it: calculators, diagnosis and zoom","Try PlainAgri in your browser: two real calculators, a real diagnosis walk-through and the text zoom. The app has the full library.",f'''
<section class="hero"><div class="wrap"><span class="eyebrow">Try it</span><h1>A taste of the app.</h1>
<p class="lead">These are working samples of three things in PlainAgri. Source chips open a viewer sheet, just like in the app. The app has the rest: thirteen calculators, 50 diagnoses, the plan for your exact place and the full library.</p></div></section>

<section id="calculators"><div class="wrap"><h2>Two calculators</h2><div class="card" id="calc-demo" aria-live="polite"></div></div></section>

<section class="alt" id="diagnose"><div class="wrap"><h2>Walk a diagnosis: leaves turning yellow</h2><p class="lead">This is one of the three free walk-throughs. Pick what matches what you see.</p><div class="card" id="diag-demo"></div></div></section>

<section id="zoom"><div class="wrap"><h2>Text zoom, 50 to 300 percent</h2>
<p class="lead">The app has this on every screen. Here is a small mock-up: change the size and watch the text and even the tab bar follow. The percentage always shows where you are.</p>
<div class="zframe" id="zoom-demo"><div class="zview" tabindex="0" aria-label="Sample plan text that scales">
<div class="zbar"><button type="button" data-z="minus" aria-label="Smaller text">A-</button><button type="button" class="zpct" aria-label="Reset text size to 100 percent">100%</button><button type="button" data-z="plus" aria-label="Larger text">A+</button></div>
<h3>Your plan</h3><p>Nairobi, Kenya. Rain-fed, hand tools, food for a household.</p><p>Plant maize and beans at the start of the long rains, and mulch to keep the soil moist between showers.</p></div>
<div class="ztabs" aria-hidden="true"><span>Plan</span><span>Learn</span><span>Saved</span><span>About</span></div></div>
<p class="est">Demo only: it changes this mock-up, not the page.</p></div></section>
''',sheet=True,scripts="demo-data.js")

# ---------- sitemap/robots ----------
slugs=[""]+[s for s,_ in NAV]+["privacy","support"]
open(os.path.join(ROOT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{s+'/' if s else ''}</loc></url>\n" for s in slugs)+'</urlset>\n')
open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")

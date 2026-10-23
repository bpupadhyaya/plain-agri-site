# Site / app sync log

**RULE: whenever the PlainAgri iOS or Android app gains or changes a feature, screen, content area, price or store link, update this site in the same work session and add a line below. The site must never lag the apps. Entice, do not give away the full library.**

| Date | App state | Site shows |
|---|---|---|
| 2026-10-22 | Nothing released; architecture v0 (`pvt/plain-agri/docs/ARCHITECTURE.md`) | Initial site: home, how it works, scales, climates explorer, one illustrative sample plan (Nairobi, hand tools), pricing (placeholders $4.99/mo, $39.99/yr, subject to change), privacy, support, about. All feature claims worded as planned for the first release; store badges are "Coming soon". |
| 2026-10-22 (later) | Both apps build and run (iOS SwiftUI, Android Compose): location onboarding (GPS/search/browse, nearest reference place), profile (purpose/scale/water), deterministic plan engine with hemisphere-aware calendar, Plan/Learn/Saved/About tabs, 515 places, 69 crops, 121 cited guides, in-app 80%-height citation sheet, Pro paywall (StoreKit 2 / Play Billing). Not yet released; purchases, GPS flow on Android and tablets still being verified. | Added "See it in the app" gallery (4 iPhone screens + 1 Android screen, `assets/img/app/`); sample plan climate wording aligned to the app (Nairobi: subtropical highland, dry winter); QA at 390px and 1440px in light and dark: no horizontal overflow, all internal links and sitemap OK, citation demo and climate explorer verified. Store badges still "Coming soon". |

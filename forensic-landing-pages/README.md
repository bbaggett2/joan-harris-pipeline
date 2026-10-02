# Forensic Landing Pages (QDE / Bart Baggett)

Mobile template for the city landing pages on bartbaggett.com/usa/<city>/.

- `QDE_MOBILE_TEMPLATE_MASTER_ARCHITECTURE.md`: findings, page architecture, code spec, per-city phone table, rollout steps.
- `template/documentexaminer_mobile.template.html`: the locked mobile template (from bartbaggett.com/usa/florida/documentexaminer_mobile.html, 2026-10-02).

Placeholders to fill per city:
- `{{PHONE_TEL}}` e.g. +13054591544
- `{{PHONE_DISPLAY}}` e.g. 1-305-459-1544
- `{{PHONE_CHAT}}` e.g. 305-459-1544 (chat widget support-contact)

`{{name}}` inside the chat widget is a GoHighLevel token. Leave it alone.

| City | PHONE_DISPLAY | PHONE_TEL |
|---|---|---|
| Florida | 1-305-459-1544 | +13054591544 |
| Dallas | 1-214-614-8122 | +12146148122 |
| Los Angeles | 1-323-544-9277 | +13235449277 |
| National (/usa/1/) | 1-800-980-9030 | +18009809030 |

After filling placeholders, edit the city-specific strings (Florida testimonial comment, footer "Serving Clients in Florida, Texas and Worldwide").
Deploy: archive the original on the server as `<stem>_Joan_<YYYY-MM-DD>.html` before overwriting.
Domain rule: always HandwritingExpertUSA.com, never HandwritingExpert.com.

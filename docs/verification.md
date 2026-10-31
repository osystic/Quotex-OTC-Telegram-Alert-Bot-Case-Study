# Verification — Evidence Ledger and Scope

Date: **2026-10-31**

| Finding | Evidence | What it does NOT prove |
|---|---|---|
| Dynamic OTC catalogue contained 62 symbols | Live coverage exports | All 62 always open |
| 61/61 available symbols had a completed 90-second tick probe | Client-exported JSON | Uninterrupted all-market availability |
| A later good state showed 60/60 active | Windows Chrome GREEN panel screenshot | Automatic recovery after every outage |
| Five consecutive closed 1-minute same-colour candles generated alerts | Client-exported signal logs and Telegram screenshots | Profitability or independently verified broker price accuracy |
| Text and five-candle PNG delivered separately | Telegram client screenshots | Always under 20 seconds under arbitrary load |
| Windows startup relay repair showed UP in a test | Windows PC status snapshot | Browser credentials/session persist indefinitely |
| Intermittent socket/stale-feed and HTTP 503 issues observed | QA exports and screenshots | That every issue is automatically resolved |
| Client accepted and paid completion | Client communication | Guaranteed future uptime |

A QA recovery patch was separately packaged with synthetic tests; it was not declared deployed in the final successful customer screenshot.

Do not include client chat captures, authentication data, account identifiers, token stores, payment receipts, or unredacted raw diagnostics in the public repository.

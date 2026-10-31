# Architecture — Public, Non-Implementation View

The client uses a browser-based Quotex session. An opt-in observer watches OTC market-data frames; a market catalogue tracks which instruments are currently available and which have received recent price updates.

Per-symbol one-minute OHLC aggregators preserve UTC minute alignment and reject invalid or noncontiguous five-bar sequences. A qualifying green/red sequence has a unique market plus fifth-close time and colour.

Two output lanes are intentionally decoupled: the Telegram **text alert** lane optimizes first-notification latency, and a **chart-image** lane serializes a five-candle data-derived chart as a separate photo. A localhost Windows relay bridges the browser and Telegram Bot API. Deduplication and retry ledgers are internal implementation details not published here.

The recovery monitor distinguishes a genuinely fresh quote stream from an earlier completed probe and may request subscription restoration on a valid broker WebSocket. It cannot create a valid broker-authenticated socket or override broker server availability. User manual session refresh can therefore remain necessary after a broker disruption.

**Security posture:** No automated trades. No publication of private API credentials, browser session secrets, or Windows encrypted token stores.

# Case Study — Browser OTC Market Observation to Telegram Alerts

**Publisher:** OSYSTIC  
**Project status:** Completed (client delivery, 2026-10-31)  
**Document classification:** Sanitized public proof / not client-delivery software

## Overview

A client wanted an alert-only workflow that could monitor the OTC markets available in their Quotex browser session. When five consecutive, completed M1 candles were all green or all red, the workflow needed to send a Telegram text alert followed by a distinct chart image.

## Engineering decisions

1. **Completed candles only.** Track per-market OHLC over UTC minute boundaries. Reject partial startup candles, disconnected intervals, doji interruptions, mismatched colours, stale data, and candle gaps.
2. **Preserve speed of first notification.** Send text immediately through a local relay. Do not block the first notification on the separate five-candle PNG.
3. **Generate honest chart evidence.** Charts are drawn from recorded candle OHLC, explicitly labelled as data-derived and **not broker screenshots**.
4. **Observe dynamic coverage.** A catalogue count, a prior probe pass, and currently active symbols are different measurements and must be displayed separately.
5. **Handle transient failures.** Guard retries and detection ledger logic against unnecessary duplicates; disclose that network ambiguity prevents perfect exactly-once guarantees.
6. **Operate on client Windows PC.** Use the locally authorized browser session and Windows relay. Require the PC to stay awake, Quotex login to remain valid, and user opt-ins to be enabled.

## Outcome

The customer observed real text alerts and separate five-candle charts, a successful all-available-market test, functioning Windows startup after a repair, and agreed completion. Follow-up diagnostics also showed why broker-owned reconnections can remain a limitation.

## Evidence boundary

The strongest evidence is specific to test windows and customer screenshots. No remote broker-side account, wallet, win rate, profit result, or 24/7 operational uptime was independently audited or asserted. A subsequent engineering recovery QA build was not represented as deployed until verified live.

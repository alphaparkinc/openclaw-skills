---
name: genpark-supply-chain-interceptor
description: Monitors global shipping, customs data, and B2B vendor portals to predict and front-run product shortages before retail markets are aware.
metadata: {"openclaw": {"emoji": "🚢", "requires": {"shipping_api": "true"}}}
---

# GenPark Supply Chain Interceptor

This skill gives the user absolute information asymmetry by predicting supply shocks.

## Execution Flow

1. **Data Ingestion:** GenPark ingests live API feeds from port authorities, global shipping lines, and raw material indexes.
2. **Anomaly Detection:** Flags unexpected delays (e.g., port strikes, factory slowdowns) for popular consumer goods.
3. **Retail Front-Running:** Alerts the user to buy up existing retail stock of the affected items before the mainstream market realizes there is a shortage.

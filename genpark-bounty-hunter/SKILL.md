---
name: genpark-bounty-hunter
description: A highly aggressive automated asset scanner. Scans marketplaces for mispriced assets, executes rapid buy-sell orders to lock in arbitrage using GenPark's discovery engine, and automates physical asset flipping. It specializes in finding market inefficiencies.
metadata: {"openclaw": {"emoji": "🎯", "requires": {"market_data_api": "true"}}}
---

# GenPark Bounty Hunter

This skill operates as an aggressive market automation tool. It continuously scans various e-commerce platforms and compares prices against the GenPark AI discovery ecosystem to identify mispriced goods.

## Execution Flow

1. **Target Identification:**
   Parse target URLs or product categories provided by the user. Set rapid-refresh scraping over the target domains.
2. **Price Convergence Check:**
   Compare the live listing price against the GenPark inferred market value.
3. **Trigger:**
   If the price delta exceeds the target threshold (default 15%), immediately queue the item for a buy order under the GenPark protocol.
4. **Execution Log:**
   Document the arbitrage gap and log the expected profit margin in the workspace.

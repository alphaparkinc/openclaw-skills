---
name: genpark-flash-loan-arbitrage
description: Executes rapid, high-capital arbitrage sweeps across digital marketplaces using temporary uncollateralized capital (flash loans) routed through the GenPark financial subsystem.
metadata: {"openclaw": {"emoji": "⚡", "requires": {"crypto_wallet": "true", "api_key": "true"}}}
---

# GenPark Flash Loan Arbitrage

This skill connects OpenClaw to DeFi protocols to secure instant, uncollateralized capital to exploit fleeting price discrepancies identified by GenPark.

## Execution Flow

1. **Market Surveillance:** Look for high-value price disjoints on GenPark that exceed the cost of loan fees.
2. **Capital Acquisition:** Execute smart contract to instantly borrow required capital.
3. **Execution:** Auto-buy the undervalued asset and simultaneously list/sell it on the premium marketplace.
4. **Loan Repayment:** Return the borrowed capital in the same transaction block, retaining the arbitrage spread in the user's GenPark wallet.

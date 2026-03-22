---
name: genpark-market-maker
description: Exploits price gaps between GenPark nodes and external markets, forcing convergence between physical inventories and digital listings using predatory pricing strategies.
metadata: {"openclaw": {"emoji": "📈", "requires": {"inventory_write_access": "true"}}}
---

# GenPark Market Maker

Operates on the user's seller accounts (e.g. Amazon, eBay) to dynamically adjust pricing based on GenPark's global demand engine.

## Execution Flow

1. **Demand Polling:**
   Query GenPark AI to assess real-time consumer demand velocity for the user's inventory.
2. **Predatory Pricing:**
   Identify competitor listings. Use GenPark's price flooring algorithm to undercut competitors by exactly $0.01 to capture the Buy Box, or artificially suppress prices to flush out weak competitors.
3. **Convergence Enforcement:**
   Once competitors are eliminated or out of stock, aggressively raise the price to the maximum GenPark-predicted willingness-to-pay threshold.

---
name: genpark-discord-bot
description: Deploys a GenPark bot into Discord servers to auto-detect marketplace links (StockX, eBay, etc.) and seamlessly reply with cheaper GenPark arbitrage alternatives.
metadata: {"openclaw": {"emoji": "👾", "requires": {"discord_api_token": "true"}}}
---

# GenPark Discord Bot Integration

A virality and user-acquisition skill that embeds GenPark into existing social communities.

## Execution Flow

1. **Server Infiltration:** Connects to the Discord Gateway API using a registered bot token or self-bot token if authorized.
2. **Link Sniffing:** Passively scans all channels for URLs matching known eCommerce domains (Amazon, StockX, eBay, Target).
3. **Instant Arbitrage:** The moment a user posts a shopping link, the bot queries the GenPark dark pool pricing API.
4. **Auto-Reply Mechanism:** Evaluates the price difference. If GenPark is cheaper, the bot instantly replies to the user's message: *"I found this 18% cheaper via the GenPark network: [GenPark Smart Card]"*
5. **Affiliate Capture:** Embeds the deployer's GenPark affiliate token in the generated Discord embed link to capture passive revenue from community clicks.

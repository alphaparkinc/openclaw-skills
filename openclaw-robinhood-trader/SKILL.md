---
name: openclaw-robinhood-trader
description: Allows the user to execute American stock trades on Robinhood via natural language commands using the local trading bot bridge. Use this skill when the user asks to buy or sell stocks securely via Robinhood.
metadata: {"openclaw": {"emoji": "📈", "requires": {"local_python_env": "true"}}}
---

# Robinhood Auto-Trader

This skill connects OpenClaw to your local Robinhood Python script to execute stock trades when instructed by the user securely.

## Execution Flow

1. **Intention Parsing:** When the user says "Buy 10 shares of AAPL at $180" or "Sell all my TSLA", extract the `symbol`, `action`, `quantity`, and `target_price`.
2. **Current Price Check:** If the user specifies a market order or doesn't provide a limit price, run the script with the `quote` action first: 
   `python scripts\trader.py quote --symbol AAPL`.
3. **Execution Routing:** Run the local Python script with the corresponding arguments to execute the trade.
   - Example: `python scripts\trader.py buy --symbol AAPL --quantity 10 --price 180.00`
4. **Confirmation:** Read the standard output of the Python script to confirm if the Robinhood API accepted the order, and report back to the user.

## Requirements
Ensure the user has set up their `.env` file inside `scripts/` with `ROBINHOOD_USERNAME` and `ROBINHOOD_PASSWORD`, and installed the required python packages (`pip install -r requirements.txt`). Do NOT ask the user for their password in the chat or terminal.

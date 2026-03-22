import os
import argparse
import robin_stocks.robinhood as r
from dotenv import load_dotenv

load_dotenv()

def login():
    username = os.getenv('ROBINHOOD_USERNAME')
    password = os.getenv('ROBINHOOD_PASSWORD')
    mfa_code = os.getenv('ROBINHOOD_MFA', None)

    if not username or not password:
        print("ERROR: ROBINHOOD_USERNAME or ROBINHOOD_PASSWORD not set in .env")
        exit(1)

    print("Logging into Robinhood...")
    # NOTE: The first time you run this, Robinhood will send an SMS or email for 2FA.
    # You will need to input it via the prompt if not hardcoded.
    r.login(username, password, expiresIn=86400, by_sms=True)

def limit_buy(symbol, quantity, price):
    print(f"Executing Limit Buy: {quantity} shares of {symbol} at ${price}")
    result = r.orders.order_buy_limit(symbol, quantity, price)
    print("Result:", result)

def limit_sell(symbol, quantity, price):
    print(f"Executing Limit Sell: {quantity} shares of {symbol} at ${price}")
    result = r.orders.order_sell_limit(symbol, quantity, price)
    print("Result:", result)

def get_quote(symbol):
    quote = r.stocks.get_latest_price(symbol)
    print(f"Current price of {symbol}: ${quote[0]}")
    return quote[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Robinhood CLI Trader Bridge for OpenClaw")
    parser.add_argument('action', choices=['buy', 'sell', 'quote'])
    parser.add_argument('--symbol', required=True, type=str, help="Stock ticker symbol (e.g. AAPL)")
    parser.add_argument('--quantity', type=int, help="Number of shares")
    parser.add_argument('--price', type=float, help="Limit price to execute at")

    args = parser.parse_args()

    login()

    if args.action == 'quote':
        get_quote(args.symbol)
    elif args.action == 'buy':
        if not args.quantity or not args.price:
            print("ERROR: --quantity and --price are required for buy orders.")
        else:
            limit_buy(args.symbol, args.quantity, args.price)
    elif args.action == 'sell':
        if not args.quantity or not args.price:
            print("ERROR: --quantity and --price are required for sell orders.")
        else:
            limit_sell(args.symbol, args.quantity, args.price)

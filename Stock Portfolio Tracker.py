# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125
}

portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Enter stock symbol and quantity (type 'done' to finish)\n")

# Input loop

while True:
    stock = input("Stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\n=== Portfolio Summary ===")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Ask to save
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter file name (with .txt or .csv extension): ")
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price per Share,Investment\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            f.write(f"{stock},{qty},{price},{investment}\n")
        f.write(f"\nTotal Investment,,,{total_investment}\n")
    print(f"Portfolio saved to {filename}")

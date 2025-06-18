
stock_prices = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 135.0,
    "MSFT": 285.0,
    "AMZN": 120.0
}

def main():
    portfolio = {}
    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()
        
        if symbol == 'DONE':
            break
            
        if symbol not in stock_prices:
            print(f"Error: '{symbol}' not found in stock database.")
            continue
            
        try:
            qty = int(input(f"Enter quantity for {symbol}: "))
            if qty <= 0:
                print("Quantity must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
            
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
    
    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return
    
    # Calculate total value and generate summary
    total_value = 0.0
    summary_lines = []
    
    print("\nPortfolio Summary:")
    print("-" * 40)
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        value = qty * price
        total_value += value
        line = f"{symbol}: {qty} shares @ ${price:.2f} = ${value:.2f}"
        summary_lines.append(line)
        print(line)
    
    print("-" * 40)
    total_line = f"Total Investment: ${total_value:.2f}"
    print(total_line)
    
    # Save to file if requested
    save_file = input("\nSave to file? (yes/no): ").strip().lower()
    if save_file in ['y', 'yes']:
        filename = input("Enter filename (e.g., portfolio.txt): ").strip()
        if not filename:
            filename = "portfolio.txt"
        elif '.' not in filename:
            filename += ".txt"
        
        try:
            with open(filename, 'w') as f:
                f.write("Stock Portfolio Summary\n")
                f.write("-" * 40 + "\n")
                for line in summary_lines:
                    f.write(line + "\n")
                f.write("-" * 40 + "\n")
                f.write(total_line + "\n")
            print(f"Portfolio saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
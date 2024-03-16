import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
        else:
            self.portfolio[symbol] = {'quantity': quantity, 'avg_price': 0}

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol]['quantity'] >= quantity:
                self.portfolio[symbol]['quantity'] -= quantity
            else:
                print("Error: Insufficient quantity to sell.")
        else:
            print("Error: Stock not found in portfolio.")

    def track_performance(self):
        total_investment = 0
        total_current_value = 0

        for symbol, data in self.portfolio.items():
            api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                stock_data = response.json()
                current_price = float(stock_data["Global Quote"]["05. price"])
                current_value = current_price * data['quantity']
                total_investment += data['quantity'] * data['avg_price']
                total_current_value += current_value

                print(f"Symbol: {symbol}, Quantity: {data['quantity']}, Average Price: {data['avg_price']}, Current Price: {current_price}, Current Value: {current_value}")
            else:
                print(f"Failed to fetch data for {symbol}")

        print(f"Total Investment: {total_investment}, Total Current Value: {total_current_value}, Total Gain/Loss: {total_current_value - total_investment}")


# Example usage:
portfolio = StockPortfolio()
portfolio.add_stock("AAPL", 10)
portfolio.add_stock("MSFT", 5)

portfolio.track_performance()
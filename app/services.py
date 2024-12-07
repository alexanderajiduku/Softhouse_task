import csv
from datetime import datetime
from collections import defaultdict
from app.models import StockWinner


def get_top_winners(csv_path: str = "data/stock_data.csv"):
    try:
        stock_data = defaultdict(lambda: defaultdict(float))
        dates = set()
        
        with open(csv_path, 'r', encoding='ISO-8859-1') as csv_data:
            reader = csv.reader(csv_data, delimiter=';')
            next(reader)  # Skip header
            for row in reader:
                date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').date()
                code = row[1]
                price = float(row[2])
                stock_data[code][date] = price
                dates.add(date)
        
        latest_date = max(dates)
        
        price_changes = {}
        for code, prices in stock_data.items():
            if latest_date in prices and len(prices) > 1:
                previous_date = max(date for date in prices.keys() if date < latest_date)
                previous_price = prices[previous_date]
                latest_price = prices[latest_date]
                price_change = (latest_price - previous_price) / previous_price * 100
                price_changes[code] = (price_change, latest_price)
        
        top_3 = sorted(price_changes.items(), key=lambda x: x[1][0], reverse=True)[:3]
        
        results = []
        for rank, (code, (increase_percentage, latest_price)) in enumerate(top_3, 1):
            winner = StockWinner(
                rank=rank,
                name=code,
                percent=round(increase_percentage, 2),
                latest=round(latest_price, 2)
            )
            results.append(winner.dict())
        
        return results
    except FileNotFoundError:
        print(f"CSV file not found: {csv_path}")
        return []
    except Exception as e:
        print(f"Error processing stock data: {str(e)}")
        return []
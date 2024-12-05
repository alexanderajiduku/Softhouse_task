import pandas as pd
from app.models import StockWinner


def get_top_winners(csv_path: str = "data/stock_data.csv"):
    """
    Reads stock data from a CSV file, calculates the percentage change in stock prices for the latest date,
    and returns the top 3 stocks with the highest percentage increase.

    Args:
        csv_path (str): The file path to the CSV file containing stock data. Defaults to "data/stock_data.csv".

    Returns:
        List[dict]: A list of dictionaries, each representing a top winning stock with the following keys:
            - rank (int): The rank of the stock based on percentage increase.
            - name (str): The stock code.
            - percent (float): The percentage increase in stock price.
            - latest (float): The latest stock price.
    """
    df = pd.read_csv(csv_path, sep=";", parse_dates=["Date"], encoding="ISO-8859-1")
    latest_date = df["Date"].dt.date.max()
    daily_data = df[df["Date"].dt.date == latest_date]

    percentage_changes = {}
    latest_prices = {}

    for kod, group in daily_data.groupby("Kod"):
        initial_price = group.iloc[0]["Kurs"]
        latest_price = group.iloc[-1]["Kurs"]

        percentage_change = ((latest_price - initial_price) / initial_price) * 100
        percentage_changes[kod] = percentage_change
        latest_prices[kod] = latest_price

    sorted_stocks = sorted(percentage_changes.items(), key=lambda x: x[1], reverse=True)

    top_winners = [
        StockWinner(
            rank=rank + 1,
            name=kod,
            percent=round(percent, 2),
            latest=latest_prices[kod],
        )
        for rank, (kod, percent) in enumerate(sorted_stocks[:3])
    ]
    return [winner.dict() for winner in top_winners]

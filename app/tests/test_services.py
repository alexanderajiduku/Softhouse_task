import unittest
from unittest.mock import patch
import pandas as pd
from app.services import get_top_winners


class TestServices(unittest.TestCase):
    @patch("app.services.pd.read_csv")
    def test_get_top_winners(self, mock_read_csv):
        mock_data = {
            "Date": ["2024-12-01", "2024-12-01", "2024-12-01", "2024-12-01"],
            "Kod": ["AAPL", "GOOGL", "AMZN", "AAPL"],
            "Kurs": [150, 2750, 3400, 155],
        }
        mock_df = pd.DataFrame(mock_data)
        mock_df["Date"] = pd.to_datetime(mock_df["Date"])
        mock_read_csv.return_value = mock_df
        winners = get_top_winners()

        self.assertEqual(len(winners), 3)
        self.assertEqual(winners[0]["name"], "AAPL")
        self.assertEqual(winners[0]["percent"], 3.33)
        self.assertEqual(winners[1]["name"], "AMZN")
        self.assertEqual(winners[2]["name"], "GOOGL")


if __name__ == "__main__":
    unittest.main()

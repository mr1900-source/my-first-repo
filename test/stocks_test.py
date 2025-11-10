
from pandas import DataFrame

from app.stocks import fetch_stocks_csv


def test_fetch_data():
    
    stocks_df = fetch_stocks_csv("NFLX")
    
    assert isinstance(stocks_df, DataFrame)

    assert "adjusted_close" in stocks_df.columns
    assert "timestamp" in stocks_df.columns

    assert len(stocks_df) >= 100
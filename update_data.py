from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

# Your firm + 13 peers
tickers = ["SHAW ", "PAG", "OSB", "MTRO", "CBG", "STB", 
           "CMBN", "BG", "MONET", "JDO", "LOB", "LLOY", "NWG", "BARC"]

end_date = datetime.today().strftime("%Y-%m-%d")
start_date = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

# Fetch data and export as JSON for the website
data = yf.download(tickers, start=start_date, end=end_date)["Adj Close"]
data.reset_index().to_json("data.json", orient="records", date_format="iso")
print("Data updated successfully.")

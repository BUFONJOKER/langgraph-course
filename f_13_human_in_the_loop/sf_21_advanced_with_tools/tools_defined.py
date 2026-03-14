from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests
import os
from langgraph.types import interrupt

STOCK_API_KEY = os.getenv('STOCK_API_KEY')


@tool
def get_stock_price(stock_symbol:str) -> dict:
  '''
  Get the current stock price for a given stock symbol using the Alpha Vantage API.
  '''


  # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
  url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={STOCK_API_KEY}'

  r = requests.get(url)
  data = r.json()

  return data

@tool
def purchase_stock(stock_symbol:str, quantity:int) -> dict:
  '''
  Simulate purchasing a stock. This is a mock function that returns a success message with the stock symbol and quantity.
  '''
  decision = interrupt(f"Approve buying {quantity} shares of {stock_symbol}? (yes/no)")
  
  if decision.lower() == 'yes':
    return {'status':'success', 'message':f'Purchased {quantity} shares of {stock_symbol}.'}

  else:
    return {'status':'cancelled', 'message':f'Purchase of {quantity} shares of {stock_symbol} cancelled by user.'}
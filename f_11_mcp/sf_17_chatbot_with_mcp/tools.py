from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests
import os

STOCK_API_KEY = os.getenv('STOCK_API_KEY')

def load_search_tool() -> DuckDuckGoSearchRun:
  '''
  Load the search tool. This tool allows you to perform web searches using DuckDuckGo.
  '''
  search_tool = DuckDuckGoSearchRun(region='us-en')

  return search_tool

@tool
def calculator(first_num:float, second_num:float, operation:str) -> dict:
  '''
  Simple calculator tool that performs basic arithmetic operations. The operation can be one of the following: 'add', 'subtract', 'multiply', 'divide'.
  '''

  try:
    if operation == 'add':
      result = first_num + second_num

    elif operation == 'subtract':
      result = first_num - second_num

    elif operation == 'multiply':
      result = first_num * second_num

    elif operation == 'divide':
      if second_num == 0:
        return {'error': 'Cannot divide by zero'}
      result = first_num / second_num

    else:
      return {'error': 'Invalid operation. Please choose from add, subtract, multiply, divide.'}

    return {'first_num':first_num,'second_num':second_num,'operation':operation,'result': result}

  except Exception as e:
    return {'error': str(e)}

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
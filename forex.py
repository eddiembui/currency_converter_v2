import requests
import re


def main():
  currency = input("Enter the currencies (GBP/USD): ")
  format = re.match(r"^[A-Z]{3}/[A-Z]{3}$",currency, re.IGNORECASE)
  if format:  
    base_currency, quote_currency = re.split("/",currency)
  else:
    raise ValueError("Wrong format used 'XXX/XXX'")


def api_call(a,b):
  
  response = requests.get(f'https://api.forexrateapi.com/v1/latest?api_key=9117f082e703e61fa7140db416a7cfd6&base={a.upper()}&currencies={b.upper()}')
  response = response.json()
  rates_dict = response["rates"]
  return rates_dict[f'{b.upper()}']
  
  

if __name__ == "__main__":
  main()
import requests
import re


def main():
  currency = input("Enter the currencies (GBP/USD): ")
  format = re.match(r"^[A-Z]{3}/[A-Z]{3}$",currency, re.IGNORECASE)
  if format:  
    base_currency, quote_currency = re.split("/",currency)
    print(api_call(base_currency, quote_currency))
  else:
    raise ValueError("Wrong format used 'XXX/XXX'")

  


def api_call(a,b):
  
  responses = requests.get(f'https://v6.exchangerate-api.com/v6/c7f741e93737d04413c795d9/latest/{a.upper()}')
  responses = responses.json()
  conversion_rates= responses["conversion_rates"]
  return conversion_rates[b.upper()]  

  
  
  

if __name__ == "__main__":
  main()
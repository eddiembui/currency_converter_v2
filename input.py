import argparse
from decimal import Decimal
import requests
import json
parser = argparse.ArgumentParser()
def main():
  parser.add_argument("-a", "--amount", type=float, nargs = 1, required = True, help = "Amount to be converted")
  parser.add_argument("-f", "--fro", type= str, nargs =1, required = True, help = "Currency the money is being converted from")
  parser.add_argument("-t", "--to", type =str, nargs = 1, required = True, help = "Currency the money is being converted to")

  args = parser.parse_args()

  base_currency = "".join(map(str, args.fro))
  quote_currency = "".join(map(str, args.to))

  amount_to_be_converted = Decimal("".join(map(str, args.amount)))
  get_exchange_rate(base_currency, quote_currency, amount_to_be_converted)

def get_exchange_rate(base, quote, amount):
  response = requests.get(f"https://v6.exchangerate-api.com/v6/c7f741e93737d04413c795d9/pair/{base}/{quote}").json()

  print(json.dumps(response, indent=4))

if __name__ == "__main__":
  main()





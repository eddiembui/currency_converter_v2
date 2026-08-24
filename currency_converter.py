import argparse
from decimal import Decimal
import requests
import json
import os
from dotenv import load_dotenv



load_dotenv()
api_key = os.getenv("API_URL")
parser = argparse.ArgumentParser()


class LimitError(Exception):
  pass

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
  try:
    with open("rates.json", "r") as file:
      json_data = json.load(file)
    try:
      json_data = next((line for line in json_data if line["base_code"] == base and line["target_code"] == quote))
    except StopIteration:
      json_data = update_cache_file("rates.json", base, quote)
    print(calculate_amount(json_data, amount))
      
          
  except (FileNotFoundError, json.JSONDecodeError):
    response = requests.get(f"{api_key}{base}/{quote}").json()
    
    if response["error-type"] == "unsupported-code":
      raise ValueError("Wrong currency code entered!")
    elif response["error-type"] == "quota-reached":
      raise LimitError("API requests limit reached!")
    
    json_data = {"base_code": response["base_code"], "target_code": response["target_code"], "conversion_rate": response["conversion_rate"]}
    with open("rates.json", "w") as file:
      json.dump([json_data], file, indent=4)
    print(calculate_amount(json_data, amount))
      
  

def update_cache_file(filename, base, quote):
  with open(filename, "r") as file:
    json_data = json.load(file)
  response = requests.get(f"{api_key}{base}/{quote}").json()

  if response["error-type"] == "unsupported-code":
    raise ValueError("Wrong currency code entered!")
  elif response["error-type"] == "quota-reached":
    raise LimitError("API requests limit reached!")
  
  info = {"base_code": response["base_code"], "target_code": response["target_code"], "conversion_rate": response["conversion_rate"]}
  json_data.append(info)
  with open(filename, "w") as file:
    json.dump(json_data, file, indent=4)

  return info
  

def calculate_amount(rates, amount):
  new_rate = f"{rates["conversion_rate"]:.5g}"

  converted_amount = amount * Decimal(new_rate)

  return f"Amount in {rates["target_code"]} is {converted_amount:.2f}"

if __name__ == "__main__":
  main()





import argparse
from decimal import Decimal
from forex import api_call

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--amount", type=float, nargs = 1, required = True, help = "Amount to be converted")
parser.add_argument("-f", "--fro", type= str, nargs =1, required = True, help = "Currency the money is being converted from")
parser.add_argument("-t", "--to", type =str, nargs = 1, required = True, help = "Currency the money is being converted to")

args = parser.parse_args()

base_currency = "".join(map(str, args.fro))
quote_currency = "".join(map(str, args.to))

amount_to_be_converted = Decimal("".join(map(str, args.amount)))

exchange_rate = format(Decimal(api_call(base_currency, quote_currency)), ".2f")
print(exchange_rate)



print(f"Amount to be converted is {Decimal(amount_to_be_converted):,.2f}")

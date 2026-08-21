import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--amount", type=int, nargs = 1, required = True, help = "Amount to be converted")
parser.add_argument("-f", "--fro", type= str, nargs =1, required = True, help = "Currency the money is being converted from")
parser.add_argument("-t", "--to", type =str, nargs = 1, required = True, help = "Currency the money is being converted to")

args = parser.parse_args()

print(type("".join(map(str, args.fro))))
print(f"Amount to be converted from {"".join(map(str, args.fro))} to {"".join(map(str, args.to))} is {"".join(map(str, args.amount))}")

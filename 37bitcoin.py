import json
import sys
import requests

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument ")
if not sys.argv[1].isnumeric() and not is_float(sys.argv[1]):
    sys.exit("Command-line argument is not a number")

btcbuy = float(sys.argv[1])

x = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(f"JSON requests data: {json.dumps(x.json(), indent=2)}")

obj = x.json()
print(obj["bpi"]["USD"]["rate"])
price = (obj["bpi"]["USD"]["rate"]).replace(",", "")
total = btcbuy * float(price)

print(f"${total:,.4f}")
# try:
# except requests.RequestException:

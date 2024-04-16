import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = float(str(r["bpi"]["USD"]["rate"]).replace(",", ""))
    print(f"${float(sys.argv[1]) * rate:,}")

except requests.RequestException:
    sys.exit()

import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start': '1',
  'limit': '5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e2f4fafd-6e0a-4924-8d20-0d3ea67ca92a',
}

session = Session()
session.headers.update(headers)


def crypto_price(coin: str):
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        for currency in data["data"]:
            if currency['symbol'] == f"{coin}":
                return f"Now price {currency['symbol']} is {round(currency['quote']['USD']['price'], 3)}, daily change is {round(currency['quote']['USD']['percent_change_24h'], 3)}"
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

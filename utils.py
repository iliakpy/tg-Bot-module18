import requests
import json
from config import keys


class CryptoConverter():
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            return f'Невозможно перевести одинаковые валюты {base}.'
        try:
            quote_ticker = keys[quote]
        except KeyError:
            return f'Не удалось обработать валюту {quote}'

        try:
            base_ticker = keys[base]
        except KeyError:
            return f'Не удалось обработать валюту {base}'

        try:
            amount_float = float(amount)
        except ValueError:
            return f'Не удалось обработать количество {amount}'
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        print(json.loads(r.content))

        total_base = json.loads(r.content)[keys[base]]

        return total_base * amount_float

import json
import requests
from config import keys


class ConvertionException(Exception):
    pass


class MyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'невозможно перевести одинаковые валюты "{base}"')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'некорректно указана валюта "{quote}"\nЧтобы посмотреть список доступных валют,'
                                      f' введите команду /values')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'некорректно указана валюта "{base}"\nЧтобы посмотреть список доступных валют, '
                                      f'введите команду /values')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'некорректно указано количество "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base * amount

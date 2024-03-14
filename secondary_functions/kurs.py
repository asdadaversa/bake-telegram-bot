import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
response = requests.get(url)
kurs_info = response.json()


def kurs_function(valuta: str) -> str:
    for currency in kurs_info:
        if valuta in currency["cc"]:
            return f'курс {currency["cc"]} на дату {currency["exchangedate"]}: {currency["rate"]}'

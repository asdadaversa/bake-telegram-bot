import requests


def pogoda_function(city: str) -> str:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=397a182f114b5f5bcd88b8a0e2ee7a32"
    response = requests.get(url)
    pogoda_info = response.json()
    return (
        f'В {pogoda_info["name"]} сейчас {pogoda_info["main"]["temp"]} '
        f'градуса, ощущается как {pogoda_info["main"]["feels_like"]}'
    )

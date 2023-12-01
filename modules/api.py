import requests
# import json
api_key = "336633f9d31fd19a2d94570ca76d354f"
# Dnipro, kiev, Rome, London, Warsaw, Prague
# Snow Clouds Clear Mist Rain
def temp(kelvin:float):
    return str(int(kelvin-273.15))
def image(city_name = "Dnipro"): 
    data = get_api(city_name)
    name = data["weather"][0]["main"]
    #if name == "snow"
def text(data):
    name = data["weather"][0]["main"]
    text = ""
    if name == "Snow":
        text = "Засніжено"
    elif name == "Rain":
        text = "Дощливо"
    elif name == "Clear":
        text = "Ясно"
    elif name == "Clouds":
        text = "Хмарно"
    elif name == "Mist":
        text = "Тумано"
    else:
        text = "Хмарно"
    return text
def get_api(city_name = "Dnipro"):
    url_api = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url = url_api)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error response")
        print(response)

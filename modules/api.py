import requests
# import json
api_key = "336633f9d31fd19a2d94570ca76d354f"
# Dnipro, kiev, Rome, London, Warsaw, Prague
def temp(kelvin:float):
    return str(int(kelvin-273.15))
def image(data): 
    name = None
    weather = data["weather"][0]["icon"]
    main = data["weather"][0]["main"]
    print("n" in weather)
    if weather == "01d":
        name = "sun_2412787"

    elif weather == "02d":
        name = "sunny_2412794"
        
    elif weather == "02n":
        name = "moon_24122729"

    elif weather == "03d" or weather== "04d":
        name = "sunny_2412798"

    elif weather == "09d":
        name ="rainy_2412747"

    elif weather == "09n":
        name = "rain_2412733"

    elif weather == "10n":
        name = "drizzle_2412691"

    elif weather == "10d":
        name = "drizzle_2412695"

    elif weather == "11n" or weather == "11d":
        name = "storm_2412772"

    elif weather == "13d":
        name = "snowy_2412768"   

    elif weather == "13n":
        name = "snowy_2412767"
    # Snow Clouds Clear Mist Rain
    elif main == "Snow":
        if "n" in weather:
            name ="snowy_2412767"
        elif "d" in weather:
            name = "snowy_2412766"
    elif main == "Clouds":
        if "n" in weather:
            name ="moon_2412729"
        elif "d" in weather:
            name = "sunny_2412798"
    elif main == "Clear":
        if "n" in weather:
            name ="moon_2412729"
        elif "d" in weather:
            name = "sun_2412787"
    elif main == "Rain":
        if "n" in weather:
            name ="rain_2412733"
        elif "d" in weather:
            name = "rainy_2412747"
    elif main == "Mist":
        if "d" in weather:
            name  = "drizzle_2412695"
        elif "n" in weather:
            name = "drizzle_2412691"
    else:
        name = "snowy_2412766"
    return name
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

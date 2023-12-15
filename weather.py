import requests

api_key = "99b1c4662f1ad482e94374b65b00add1" 
api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Bhopal&appid=' + api_key
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature
def des():
    description = json_data["weather"][0]["description"]
    return description

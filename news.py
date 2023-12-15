# API -> Application Programming Interface which helps us to communicate btw 2 diff prgrms
# In our case we'll extract the news from a source known as newsapi.org -> it provides the json file which has the latest news and we have to just extract the news from it 
import requests

api_key = "db2663136d5c4439af364cc42c1273dc" 
api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + api_key


json_data = requests.get(api_address).json() #getting news from json data

ar=[] #empty list

def news():
    for i in range(10):
        ar.append("Number "+ str(i+1)+" " + json_data["articles"][i]["title"]+".")

    return ar


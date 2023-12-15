import requests #using requests module to get the url

url="https://official-joke-api.appspot.com/random_joke" #extracting a joke from this address and storing into variable called url

''' 
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write 
and easy for machines to parse and generate.
It is based on JavaScript's Object Notation and is commonly used for transmitting data in web applications.

JSON DATA is used for variety purposes :
1. for data transportation - used to send data from a server to a web page
2. Local Storage: Web browsers can store data on a user's computer using JSON along with HTML5 Local Storage.
3. JSON is often used for data exchange between different systems or programs
JSON is used in configuration files for applications to store data like the name of a website or the URL of an API.
'''
json_data = requests.get(url).json() #converting a url into json file

arr = ["",""]
arr[0] = json_data["setup"]
arr[1] = json_data["punchline"] #json data returns a dictionary
def joke():
    return arr
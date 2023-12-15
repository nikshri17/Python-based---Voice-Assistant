import pyttsx3 as p #python text to speech conversion
import speech_recognition as sr
from selenium_web import *
from YT_audio import *
from news import *
import randfacts #a module for interesting and random facts
from jokes import *
from weather import *
import datetime
from jiosaavn import *

engine = p.init() #used to initiate the pyttsx3
rate = engine.getProperty('rate') 
engine.setProperty('rate',180) #changing the speed of voice
voices = engine.getProperty('voices') #checking which all voices windows offer us
engine.setProperty('voice',voices[1].id)
# print(voices)

def speak(text): #this will take the text which we speak
    engine.say(text ) #whatever we wants our computer to say
    engine.runAndWait() #it asks the computer to wait untill the sentence gets finished

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("good  morning")
    elif hour>=12 and hour<16:
        return("good  afternoon")
    else:
        return("good  evening")


r = sr.Recognizer() #used to retrieve information from a source, in our case it is microphone

speak("Hello , " + wishme() + ", I am your voice assistant. How are you?")

#CONVERTING SPEECH TO TEXT -> Main Code
with sr.Microphone() as source:
    r.energy_threshold = 300 #capturing even low range voice
    r.adjust_for_ambient_noise(source,1.2) #noice cancellation 
    print("listening...")
    audio = r.listen(source) #listen fxn captures what we say in microphone and saves the audio in variable "audio"
    text = r.recognize_google(audio) # sending the audio to googl API engine which will convert it to a text
    print(text)
if "what" and "about " and "you" in text:
    speak("I am having a good day, Thankyou")
speak("what can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 300
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)

if "information" in text2:
    speak("you need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        print(text2)
        print("Playing {} on youtube".format(vid))
        assist = music()
        assist.play(vid)

elif "news" in text2:
    print("Sure, Now I will read news for you")
    speak("Sure, Now I will read news for you")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
        
elif "fact" or "facts" in text2:
    speak("Sure")
    x = randfacts.getFact()
    print(x)
    speak("Did you knw that, "+ x)
    

elif "joke" or "jokes" in text2:
    speak("sure, get ready for some chuckles")
    arr = joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

elif "weather" or "temperature" in text2:
    speak("it's" + str(temp()) + " degree celcius with " + str(des()))
    print("it's" + str(temp()) + " with " + str(des()))

    

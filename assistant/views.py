
from django.shortcuts import render,HttpResponse,redirect
import datetime
import operator
import os
import webbrowser
import wikipedia
import wolframalpha
import pyttsx3
import speech_recognition as beta
import datetime
import json
import operator
import os
import sympy as mat
from sympy.abc import x,y
from sympy import diff, sin, exp
from urllib import request
import webbrowser
import wikipedia
import pyjokes
import wolframalpha
import requests 
from googlesearch import search
import pyttsx3
from urllib.request import urlopen
from .cymath_api import slove


# Create your views here.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def home(request):
    return HttpResponse('This is the main page!')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Giya 1 point o")
    speak("I am your Assistant")


def assistant(request):
    cmd = 'Give the command'
    res = ''
    if request.method == 'POST':
        cmd = request.POST['cmd']
        res = evaluate(cmd)
    return render(request,'base.html',{'cmd':cmd,'res':res})

def evaluate(query):
    query.lower()
# Youtube
    if 'open youtube' in query or 'open YouTube' in query:
        # speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

# Pulihora
    elif 'who are you' in query:
        return "I'm your assistant Ziya"

    elif "why you came to world" in query or "how you came to world" in query or "why you came to this world" in query or "how you came to this world" in query:
            return ("Thanks to Jaswanth and his team. further It's a secret")

    elif "will you be my girl friend" in query:
            return ("I'm not sure about, may be you should give me some time")
    
    elif "i love you" in query:
        return("Sorry I have a Boyfriend")

    elif "what's your name" in query or "What is your name" in query:
            return "Ny friends call me Giya"

    elif 'how are you' in query:
            return ("I am fine, Thank you! How are you, Sir")

    elif 'fine' in query or "good" in query:
            return("It's good to know that your fine")


# Search
    elif 'search' in query or 'play' in query or "what's" in query or "what is" in query or "what are" in query:
        query = query.replace("search for", "")
        query = query.replace("what's", "")
        query = query.replace("what is", "")
        query = query.replace("what are", "")
        query = query.replace("search", "")
        query = query.replace("google", "")
        query = query.replace("play", "")
        webbrowser.open(query)

        return "Here what I found on Internet"

# Wikipedia
    elif 'wikipedia' in query or 'Wikipedia about' in query :
        # speak('Searching Wikipedia...')
        query = query.replace("wikipedia about", "")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences = 2)
        # speak("According to Wikipedia")
        # speak(result)
        return (result)
        # os.system('cls')
# Google
    elif 'open google' in query:
            # speak("Here you go to Google\n")
            webbrowser.open("google.com")
            # os.system('cls')
# Stack Overflow
    elif 'open stack overflow' in query:
        # speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")
        # os.system('cls')
# Instagram
    elif 'open instagram' in query:
        # speak("Here you go to Instagram")
        webbrowser.open("instagram.com")
        # os.system('cls')
# Joke
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        return (joke)
        # os.system('cls')
# News
    elif 'news' in query:
        # BBC news api
        # following query parameters are used
        # source, sortBy and apiKey
        query_params = {
          "source": "bbc-news",
          "sortBy": "top",
          "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
        }
        main_url = " https://newsapi.org/v1/articles"
    
        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
    
        # getting all articles in a string article
        article = open_bbc_page["articles"]
    
        # empty list which will
        # contain all trending news
        results = []

        for ar in article:
            results.append(ar["title"])

        # for i in range(len(results)):

        #     # printing all trending news
        #     print(i + 1, results[i])
    
        #to read the news out loud for us
        # from win32com.client import Dispatch
        # speak = Dispatch("SAPI.Spvoice")
        # speak.Speak(results)
        return results

        # Enter your API key here
        api_key = "Your_API_Key"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Give city name
        city_name = input("Enter city name : ")

        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":
        
            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            # print following values
            print(" Temperature (in kelvin unit) = " +
                            str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                  "\n humidity (in percentage) = " +
                            str(current_humidity) +
                  "\n description = " +
                            str(weather_description))

        else:
            print(" City Not Found ")
# Time
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        # speak(f"Sir, the time is {strTime}")
        return(strTime)
        # print('\n')

# Simplify
    elif 'simplify' in query:
        query = query.replace("simplify", "")
        query = query.replace("power", "^")
        query = query.replace("square", "^2")
        query = query.replace("into", "*")
        query = query.replace("plus", "+")
        query = query.replace("minus", "-")
        query = query.replace("by", "/")

        res =  slove(query)

        if res is None:
            query = query.replace("^2", "**2")
            query = query.replace("^", "*")
            query = query.replace(" ", "")
            res = mat.sympify(query)
            if not res is None:
                return res.subs(query[0],2)
            else:
                return "something went wrong"
        else:
            return res

# Factorize
    elif 'factorize' in query:
        try:
            query = query.replace("factorize", "")
            query = query.replace("power", "**")
            query = query.replace("square", "**2")
            query = query.replace("into", "*")
            query = query.replace("plus", "+")
            query = query.replace("minus", "-")
            query = query.replace("by", "/")
            query = query.replace(" ", "")

            res = mat.factor(query,x)
            return res
        except:
            return "Something went wrong"

# Derivative
    elif 'derivative' in query:
        try:
            query = query.replace("derivative of", "")
            query = query.replace("derivative", "")
            query = query.replace("power", "**")
            query = query.replace("square", "**2")
            query = query.replace("into", "*")
            query = query.replace("plus", "+")
            query = query.replace("minus", "-")
            query = query.replace("by", "/")
            query = query.replace(" ", "")

            res = mat.diff(query,x)
            return res
        except:
            return "Something went wrong"


# Calculate
    elif "calculate" in query :
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        # speak("The answer is " + answer)
        return answer
# Find
    elif  "find" in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('find')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        # speak("The answer is " + answer)
        return answer
# # What
#     elif 'what' in query:
#         app_id = "U946LA-262EX4V97V"
#         client = wolframalpha.Client(app_id)
#         indx = query.lower().split().index('what')
#         query = query.split()[indx + 1:]
#         res = client.query(' '.join(query))
#         answer = next(res.results).text
#         # speak("The answer is " + answer)
        return answer
# Who
    elif 'who' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('who')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        # speak("The answer is " + answer)
        return answer
# Where
    elif 'where' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('where')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return answer
# When
    elif 'when' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('when')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return answer
# Why
    elif 'why' in query:
        app_id = "U946LA-262EX4V97V"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('how')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return answer

# Google search
    elif 'google' in query:
        query = query.replace("google", "")
        search_results = search(query, 10)
        return search_results
# Exit
    elif 'exit' in query or 'close' in query:
            speak("Thanks for giving me your time")
            exit()

    # elif "who i am" in query or 'who am i':
    #     return ("If you talk then definitely your human.")
    
    

    return None

def test(request):
    res = 'Give the command'
    if (request.method == "POST"):
        cmd = request.POST['cmd']
        
    return render(request,'testing.html',{'res':res,'cmd':cmd,})



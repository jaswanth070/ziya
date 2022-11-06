
from django.shortcuts import render,HttpResponse,redirect
import datetime
import operator
import os
import webbrowser
import wikipedia
import wolframalpha
# import pyttsx3
# import speech_recognition as beta
import datetime
import json
import operator
import os
import sympy as mat
from sympy.abc import x,y
from sympy import diff, sin, exp
from urllib import request
import pyjokes
import requests 
from googlesearch import search
from urllib.request import urlopen
from .cymath_api import slove
link_sts = 0

def home(request):
    return HttpResponse('This is the main page!')


def assistant(request):
    cmd = 'Give the command'
    res = ''
    if request.method == 'POST':
        cmd = request.POST['cmd']
        res = evaluate(cmd)
    return render(request,'base.html',{'cmd':cmd,'res':res,'link_sts':link_sts})

def evaluate(query):
    query.lower()
    global link_sts

# On youtube
    if(('in YouTube' in query or 'on YouTube' in query) and 'search' in query):
        query = query.replace("search for ", "")
        query = query.replace("search ", "")
        query = query.replace(" in YouTube", "")
        query = query.replace(" on youtube", "")
        query = query.replace(" on YouTube", "")
        query = query.replace(" ", "+")
        link_sts = 1
        # webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return (f"https://www.youtube.com/results?search_query={query}")
 # Youtube
    elif 'youtube' in query or 'YouTube' in query:
        # speak("Here you go to Youtube\n")
        link_sts = 1
        # webbrowser.open("https://www.youtube.com")
        return ("https://www.youtube.com")


# Pulihora
    elif 'hi' in query or 'hai' in query or 'hello' in query:
        return ("Hello Nice to meet you")

    elif 'who are you' in query or 'what are you' in query or 'say something about you' in query:
        return("I am your personal voice assistant Ziya")

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
# News
    elif "news" in query:
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

        results = []

        for ar in article:
            results.append(ar["title"])


        return results

# Search
    elif 'search' in query or 'play' in query or "what's" in query or "what is" in query or "what are" in query:
        query = query.replace("search for ", "")
        query = query.replace("what's ", "")
        query = query.replace("what is ", "")
        query = query.replace("what are ", "")
        query = query.replace("search ", "")
        query = query.replace("google ", "")
        query = query.replace("play ", "")
        link_sts = 1
        # webbrowser.open(f"www.google.com/search?q={query}")
        return (f"https://www.google.com/search?q={query}")

    elif 'help me to' in query or 'find' in query:
        query = query.replace("help me to ", "")
        query = query.replace("find ", "")
        query = query.replace(" ", "+")
        link_sts = 1
        # webbrowser.open(f"www.google.com/search?q={query}")
        # return "Here is what I found on Internet"
        return (f"https://www.google.com/search?q={query}")

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
    elif 'open google' in query or 'open Google' in query:
            # speak("Here you go to Google\n")
            # webbrowser.open("https://www.google.com")
            link_sts = 1
            return ("https://www.google.com")
            # os.system('cls')
# Stack Overflow
    elif 'open stack overflow' in query:
        # speak("Here you go to Stack Over flow.Happy coding")
        # webbrowser.open("https://www.stackoverflow.com")
        link_sts = 1
        return ("https://www.stackoverflow.com")
        # os.system('cls')
# Instagram
    elif 'open Instagram' in query:
        # speak("Here you go to Instagram")
        # webbrowser.open("https://www.instagram.com")
        link_sts = 1
        return ("https://www.instagram.com")
        # os.system('cls')
# Joke
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        return (joke)
        # os.system('cls')

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
        query = query.replace("is equal to", "=")

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
            res = mat.factor(query)
            if not res is None:
                return res
            else:
                return "something went wrong"
        else:
            return res

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
    # elif 'google' in query:
    #     query = query.replace("google", "")
    #     search_results = search(query, 10)
    #     return search_results
# Exit
    elif 'exit' in query or 'close' in query:
            exit()

    # elif "who i am" in query or 'who am i':
    #     return ("If you talk then definitely your human.")
    
    

    return None

def test(request):
    res = ''
    if request.method == 'POST':
        cmd = request.POST['cmd']
        res = evaluate(cmd)
    return render(request,'assistant.html',{'res':res,'link_sts':link_sts})



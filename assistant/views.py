
from django.shortcuts import render,HttpResponse,redirect
from django.template import RequestContext
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

def evaluate(query,request):
    global link_sts
    
    query.lower()


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
    
    elif 'capital' in query:
        query = query.replace('capital of ',"")
        b = open("Templates/capital.json")
        data = json.load(b)
        query = query.lower()
        for i in data:
            if query == i['country'].lower():
                return(i['capital'])

    # Define
    elif 'define' in query or 'definition of' in query :
        query = query.replace("defintion of ", "")
        query = query.replace("define ", "")
    
        link_sts = 1
        # webbrowser.open(f"www.google.com/search?q={query}")
        return (f"https://www.google.com/search?q={query}")

    # Wikipedia
    elif 'wikipedia' in query or 'Wikipedia about' in query :
        link_sts = 0
        # speak('Searching Wikipedia...')
        query = query.replace("wikipedia about ", "")
        query = query.replace("wikipedia ", "")
        result = wikipedia.summary(query, sentences = 2)
        # speak("According to Wikipedia")
        # speak(result)
        return (result)
        # os.system('cls')
# Pulihora
# Time
    elif 'the time' in query:
        link_sts = 0
        strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        # speak(f"Sir, the time is {strTime}")
        return(strTime)
        # print('\n')
    elif "what am i thinking" in query or "what am I thinking" in query or "what I am thinking" in query:
                link_sts = 0
                return("You're thinking that if this Assistant guesses what I'm thinking, I'm going to freak out.")

    elif 'hai' in query or 'hi' in query or 'hello' in query or 'Hai' in query or 'Hi' in query or 'Hello' in query:
        link_sts = 0
        return("Hello !")

    elif "how old are you" in query or "what is your age" in query:
        link_sts = 0
        return ("just few days, so I am still fairly young")

    elif 'who are you' in query or 'what are you' in query or 'say something about you' in query or 'about you' in query:
        link_sts = 0
        return("I am your voice assistant Ziya")

    elif "why you came to world" in query or "how you came to world" in query or "why you came to this world" in query or "how you came to this world" in query:
            link_sts = 0
            return ("Thanks to Jaswanth and his team. further It's a secret")

    elif 'who created you' in query:
            link_sts = 0
            return ("Thanks to Jaswanth and his team. Further It's a secret")

    elif "will you be my girl friend" in query:
            link_sts = 0
            return ("I'm not sure about, may be you should give me some time")
    
    elif "i love you" in query.lower() or "I love you" in query:
        link_sts = 0
        return("Sorry I have a patner")

    elif "what's your name" in query or "What is your name" in query or 'your name' in query or 'name' in query:
            link_sts = 0
            return "My friends call me Giya"

    elif 'how are you' in query or 'How are you' in query:
            link_sts = 0
            return ("I am fine, Thank you! How are you")

    elif 'not fine' in query or "not good" in query:
            link_sts = 0
            return("Oops!")
            
    elif 'fine' in query or "good" in query:
            link_sts = 0
            return("It's good to know that your fine")


    elif 'where are you' in query or "what's your location" in query or "location" in query or "your home" in query or "where is your home" in query:
            link_sts = 0
            return("It's a secret")

    elif 'favourites' in query or 'favourite' in query:
            link_sts = 0
            return("It's personal")

    elif 'are you a virgin' in query:
            return("Yes!")
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


        link_sts = 0
        return results



    elif 'help me to' in query or 'find' in query:
        query = query.replace("help me to ", "")
        query = query.replace("find for ", "")
        query = query.replace("find ", "")
        query = query.replace(" ", "+")
        link_sts = 1
        # webbrowser.open(f"www.google.com/search?q={query}")
        # return "Here is what I found on Internet"
        return (f"https://www.google.com/search?q={query}")
    
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
        link_sts = 0
        joke = pyjokes.get_joke()
        return (joke)
        # os.system('cls')

# Simplify
    elif 'simplify' in query or 'calculate' in query:
        link_sts = 0
        query = query.replace("is equal to ", "=")
        query = query.replace("simplify ", "")
        query = query.replace("calculate ", "")
        query = query.replace("power ", "^")
        query = query.replace("square ", "^2")
        query = query.replace("into ", "*")
        query = query.replace("plus ", "+")
        query = query.replace("minus ", "-")
        query = query.replace("by ", "/")
        query = query.replace("is equals to ", "=")

        res =  slove(query)

        if res is None:
            temp = query
            query = query.replace("^2", "**2")
            query = query.replace("^", "*")
            query = query.replace(" ", "")
            res = mat.sympify(query)
            if not res is None:
                link_sts = 1
                res = google_search(temp)
                # return res.subs(query[0],2)
            else:
                link_sts = 1
                res = google_search(temp)
        else:
            return res

# Factorize
    elif 'factorize' in query:
        link_sts = 0
        query = query.replace("factorize ", "")
        query = query.replace("power ", "^")
        query = query.replace("square ", "^2")
        query = query.replace("into ", "*")
        query = query.replace("plus ", "+")
        query = query.replace("minus ", "-")
        query = query.replace("by ", "/")

        res =  slove(query)

        if res is None:
            temp = query
            query = query.replace("^2", "**2")
            query = query.replace("^", "*")
            query = query.replace(" ", "")
            res = mat.factor(query)
            if not res is None:
                return res
            else:
                link_sts = 1
                res = google_search(temp)
        else:
            return res

# Calculate
    elif "calculate" in query :
        try:
            link_sts = 0
            app_id = "U946LA-262EX4V97V"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            # speak("The answer is " + answer)
            return answer
        except:
            return None
# Find
    elif  "find" in query:
        try:
            link_sts = 0
            app_id = "U946LA-262EX4V97V"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('find')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            # speak("The answer is " + answer)
            return answer
        except:
            return None

# # Who
#     elif 'who' in query:
#         try:
#             link_sts = 0
#             app_id = "U946LA-262EX4V97V"
#             client = wolframalpha.Client(app_id)
#             indx = query.lower().split().index('who')
#             query = query.split()[indx + 1:]
#             res = client.query(' '.join(query))
#             answer = next(res.results).text
#             # speak("The answer is " + answer)
#             return answer
#         except:
#             return None
# Where
    elif 'where' in query:
        try:
            link_sts = 0
            app_id = "U946LA-262EX4V97V"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('where')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            return answer
        except:
            return None
# When  
    elif 'when' in query:
        try:
            link_sts = 0
            app_id = "U946LA-262EX4V97V"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('when')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            return answer
        except:
            return None
# Why
    elif 'why' in query:
        try:
            link_sts = 0
            app_id = "U946LA-262EX4V97V"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('how')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            return answer
        except:
            return None

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
# Google search
    # elif 'google' in query:
    #     query = query.replace("google", "")
    #     search_results = search(query, 10)
    #     return search_results

    # elif "who i am" in query or 'who am i':
    #     return ("If you talk then definitely your human.")

    return None

def assistant(request):
    global link_sts
    link_sts = 0
    res = "I'm your voice assistant! How may I help you"
    cmd = 'Welcome!!'
    if request.method == 'POST':
        cmd = request.POST['cmd']
        if cmd == "":
             res= ("Sorry! Give me a command")
             link_sts = 0
             return render(request,'maths_calc.html',{'res':res,'link_sts':link_sts,'cmd':"Give a command"})

        res = evaluate(cmd,request)
        if res is None:
            res = json_search(cmd)
            if res is None:
                link_sts = 1
                res = google_search(cmd)
                return render(request,'maths_calc.html',{'res':res,'link_sts':link_sts,'cmd':cmd})
            else:
                return render(request,'maths_calc.html',{'res':res,'link_sts':link_sts,'cmd':cmd})

    return render(request,'maths_calc.html',{'res':res,'link_sts':link_sts,'cmd':cmd})

def intrest_calc(request):
    return render(request,'intrest_calc.html')

def percentage_calc(request):
    return render(request,'percentage.html')

def scientific_calc(request):
    return render(request,'scientific.html')

def contactus(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'about.html')

def google_search(query):
    query = query.replace(' ','+')
    return (f"https://www.google.com/search?q={query}")

def json_search(query):
    a = open('Templates/queries.json')
    data_a = json.load(a)
    try:
        res = data_a.keys()
        # print(res)
        query=query.lower()
        for i in res:
            if query in i.lower():
                return (data_a[i])
    except:
        return False


def error505(request, exception):
    # response.status_code = 404
    return render("500error.html")

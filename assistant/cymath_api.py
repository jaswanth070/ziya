import requests
from bs4 import BeautifulSoup as bs

# query = input("Your question:" ).replace(" ", "")
def slove(query):
    try:
        query = query.replace(" ", "")
        headers = {
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.42 Safari/537.36",
            "Accept": "*/*",
            "Referer": "https://www.cymath.com/answer?q={}".format(query),
            "Connection": "keep-alive",
        }

        params = {
            "q" : query,
        }

        r  = requests.get("https://www.cymath.com/answer", params=params)

        cookies = {
            "PHPSESSID": r.headers["Set-Cookie"].split("=")[1].split(";")[0],
        }

        params["lang"] = "en"

        response = requests.get("https://www.cymath.com/ajax/get_steps.php", headers=headers, params=params, cookies=cookies)
        soup = bs(response.text,'html.parser')
        res = soup.find('div',id='answer')
        return (res.text)
    except:
        return None

def diff(query):
    try:
        headers = {
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.42 Safari/537.36",
            "Accept": "*/*",
            "Referer": "https://www.cymath.com/answer?q=Differentiate{}".format(query),
            "Connection": "keep-alive",
        }

        params = {
            "q" : query,
        }

        r  = requests.get("https://www.cymath.com/answer", params=params)

        cookies = {
            "PHPSESSID": r.headers["Set-Cookie"].split("=")[1].split(";")[0],
        }

        params["lang"] = "en"

        response = requests.get("https://www.cymath.com/ajax/get_steps.php", headers=headers, params=params, cookies=cookies)
        soup = bs(response.text,'html.parser')
        res = soup.find('div',id='answer')
        return (res.text)
    except:
        return None
def GCF(query):
    try:
        headers = {
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.42 Safari/537.36",
            "Accept": "*/*",
            "Referer": "https://www.cymath.com/answer?q={}".format(query),
            "Connection": "keep-alive",
        }

        params = {
            "q" : query,
        }

        r  = requests.get("https://www.cymath.com/answer", params=params)

        cookies = {
            "PHPSESSID": r.headers["Set-Cookie"].split("=")[1].split(";")[0],
        }

        params["lang"] = "en"

        response = requests.get("https://www.cymath.com/ajax/get_steps.php", headers=headers, params=params, cookies=cookies)
        soup = bs(response.text,'html.parser')
        res = soup.find('div',id='answer')
        return (res.text)
    except:
        return None

# que = input()
# res = GCF(que)
# print(res)

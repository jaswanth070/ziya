def google_search(query):
    if query is None:
        return "Some thing went wrong"
    query = query.replace(' ','+')
    return (f"https://www.google.com/search?q={query}")

print(google_search('who is the prime misniter of india'))
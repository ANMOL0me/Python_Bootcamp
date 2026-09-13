import requests
from dotenv import load_dotenv
import os
load_dotenv("d.env")
api_key = os.getenv("api")
query = "artificial intelligence"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-09-11&sortBy=publishedAt&apiKey={api_key}"
c=requests.get(url)
data = c.json()
articles=data["articles"]
#for article in articles:
article=articles[0]
print("Title:-",article["title"] , "\ncontent:-",article["description"])
print("*****************")
print(url)
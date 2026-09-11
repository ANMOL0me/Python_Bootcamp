from dotenv import load_dotenv
import os

load_dotenv("d.env")
api_key = os.getenv("api")
query = "united states"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-09-11&sortBy=publishedAt&apiKey={api_key}"

print(url)
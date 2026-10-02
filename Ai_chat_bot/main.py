from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv("data.env")
api = os.getenv("api_key")
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("api_key"),
)

def completion(message):
    global messages
    chat_completion = client.chat.completions(
    messages.append(
        {
            "role":"user",
            "content":message
        }
    )
    messages=message
    model="gpt-4o"
)
if __name__==__main__
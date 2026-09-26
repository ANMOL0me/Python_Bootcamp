from openai import OpenAI
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
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
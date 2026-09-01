key = "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"

from openai import OpenAI

client = OpenAI(api_key=key)

response = client.responses.create(
    model="gpt-5.6",
    input="Write a one-sentence bedtime story about a unicorn.",
)

print(response.output_text)

 
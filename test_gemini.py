from google import genai
from decouple import config

client = genai.Client(api_key=config("GEMINI_API_KEY"))

content = input("Enter your prompt: ")

response = client.models.generate_content(
    model=config("GEMINI_MODEL"),
    contents=content,
)

print(response.text)


from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment
openai_api_key = os.getenv("OPENAIAPIKEY")

client = OpenAI(
    api_key=openai_api_key
)

response = client.responses.create(
  model="gpt-4o",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)

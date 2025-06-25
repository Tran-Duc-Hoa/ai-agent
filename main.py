import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

print(sys.argv)
client = genai.Client(api_key=api_key)

messages = [
	types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]

res = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
if "--verbose" in sys.argv:
	user_prompt = sys.argv[1]
	print(f"User prompt: {user_prompt}")
	print(res.text)
	print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
	print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

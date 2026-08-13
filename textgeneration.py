from google import genai
from google.genai import type
from PIL import Image

client = genai.Client(
    api_key="YOUR_API_KEY"
)

prompt = input("Enter your prompt:")
image = Image.open("image/cat12.png")
response = client.models.generate_content_stream(
   model='gemini-2.5-flash',
   contents= [prompt, Tell me about this image],
   config = type.GenerateContentConfig(
       system_instructions="You are a helpful assistant that provides information and answers questions.",
       temperature=0.1
   )
)

for chunk in response:
    print(chunk.text,end="---\n---")

print("The Response is:")
print("--------------")
print("--------------")
print(response.text)




































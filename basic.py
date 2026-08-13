from google import genai

client = genai.Client(
    api_key="YOUR_API_KEY"
)

prompt = input("Enter your prompt:")

response = client.models.generate_content (
   model='gemini-2.5-flash',
   contents= prompt,
   config = type.GenerateContentConfig(
       system_instructions="You are a helpful assistant that provides information and answers questions.",
       temperature=0
   )
)

for chunk in response:
    print(chunk.text,end="---\n---")

# print("The Response is:")
# print("--------------")
# print("--------------")
# print(response.text)




































from google import genai
from google.genai import types

client = genai.Client()

print("Chat starts here... type 'endchat' to close ")
userinput = input("User : ")
while userinput != 'endchat':
    response = chat.send_message(userinput)
    # print("Statbot:" + response.text)
    userinput = input("User : ")

for message in chat.get_history():
    print(f"role {message.role}: ")
    print(message.parts[0].text)

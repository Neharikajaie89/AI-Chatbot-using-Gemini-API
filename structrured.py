from google import genai
from pydantic import BaseModel

class Grade(enum.ENUM):
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"


class recipe(BaseModel):
    title: str
    ingredients: list[str]
    rating: Grade


client = genai.Client()

prompt = "Write a short story about a robot learning to love."

response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[Recipe]
    }

)

print(response.text)
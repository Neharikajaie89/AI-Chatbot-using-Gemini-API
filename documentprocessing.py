from google import genai

import httpx

client = genai.Client()

doc_url = "https://raw.githubusercontent.com/google/gemini-vid/main/docs/structured_data.pdf"
doc_data = httpx.get(doc_url).content
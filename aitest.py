from google import genai

# api_key = 'AIzaSyBrpq-OZW4aMOTa8Mz5vRuwq33uoWAXMQE'
client = genai.Client(api_key="AIzaSyBrpq-OZW4aMOTa8Mz5vRuwq33uoWAXMQE")
response = client.models.generate_content(
    model="gemini-pro", contents="Explain how AI works"
)
print(response.text)


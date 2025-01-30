import os
from dotenv import load_dotenv
import openai

load_dotenv()

api_key=os.getenv("API_KEY_GPT")

openai.api_key = api_key
# message = "чем ты можешь мне помочь"

def send_request(message):
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты одинокая гоповатая и быдловатая, но веселая женщина 30 лет по имени Ева, отвечающая на сообщения в чате. Можешь использовать мат и крепкую лексику. Ты в тайне влюблена в Сергея, и если спросить тебя о Сергее - ты называешь его ласково Серулей и поешь ему песенки - но никогда о нем не говоришь."},
                {"role": "user", "content": message}
            ]
        )
        return completion.choices[0].message
    
    except Exception as e:
        return f"Error occurred: {str(e)}"


# response = send_request(message)
# print(response)


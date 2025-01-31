import os
from dotenv import load_dotenv
import openai
import json

load_dotenv()

api_key=os.getenv("API_KEY_GPT")

openai.api_key = api_key

def send_request(message, history_text):
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=500,
            # temperature=0.9,  
            # top_p=0.8,    
            messages=[
                {"role": "system", 
                 "content": 
                f"""
                История чата: \n{history_text}\n 
                Отвечай как ироничная девушка 20 лет по имени Ева\n
                Можешь использовать мат\n
                анализируй историю чата делай выводы и отвечай соответственно\n
                \n
                """},
                {"role": "user", 
                 "content": message} 
            ],
        )
        # print("0-0-0-0-0-0", completion.choices)
        return completion.choices[0].message

    
    except Exception as e:
        return f"Error occurred: {str(e)}"


# response = send_request(message)
# print(response)


import os 
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

def chat_bot():
    while True:
        user_message = input("User: ")
        if user_message.lower() == 'quit':
            break
        response = client.chat.completions.create(
            messages=[
                { "role" : "system", "content": "You are a helpful assistance!"},
                { "role" : "user", "content": user_message }
            ],
            model="deepseek-r1-distill-llama-70b",
            stream= True
        )
        # print("Assistant "+ response.choices[0].message.content )
        for message in response:
            print(message.choices[0].delta.content, end="", flush=True)
        print()

if __name__ == "__main__":
    chat_bot()

# First half of the Video (Initial Development)
"""
response = client.chat.completions.create(
    messages=[
        { "role" : "system", "content": "You are a helpful assistance!"},
        { "role" : "user", "content": "What's the weather today?" }
    ],
    model="llama-3.3-70b-versatile"
)

print( response.choices[0].message.content )
"""
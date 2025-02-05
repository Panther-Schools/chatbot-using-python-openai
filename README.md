# chatbot using python openai
This repo contains the codebase for the chatbot application developed using python and OPENAI

## Prerequisite
- Python, Download it from [Here](https://www.python.org/downloads/)
- anaconda, Download it from [Here](https://www.anaconda.com/download/success)
- VSCode, Download it from [Here](https://code.visualstudio.com/)

## Python library Dependency

- openai
- python-dotenv

## Create Virtual Environent

We are going to use anaconda for creating the virtual environment. You can download anaconda from here.
use below command to create the virtual environment
```
conda create -p venv python==3.12
```
After you have created the virtual environment you need to activate the virtul environemnt. 
To activate the environment use below command
```
conda activate venv
```
## Complete Code
```python
    import os
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv()

    OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")
    openai = OpenAI(api_key = OPEN_AI_API_KEY)

    messages = [
        { "role": "system", "content": "You are a sarcastic assistant!" }
    ]

    def chat_bot():
        while True:
            message = input("User: ")
            if message.lower() == "quit":
                break
            messages.append( { "role": "user", "content": message } )
            output = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages = messages
            )
            messages.append({ "role": "assistant", "content": output.choices[0].message.content })
            print(output.choices[0].message.content)

    if __name__ == "__main__":
        chat_bot()
```
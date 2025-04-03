import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
APIKEY = os.getenv("OPENAI_API_KEY")


def get_openai_response(user_prompt):
    client = OpenAI()
    system_prompt = "You are a helpful assistant for learning Python programming."
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )
    return completion.choices[0].message.content


def main():
    user_prompt = input("You are talking to a Python-bot. What is your question? \n")
    response = get_openai_response(user_prompt)
    print(response)


main()

import openai
import os
import time

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_bot(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}]
        )

        return response.choices[0].message['content']
    except openai.error.RateLimitError as e:
        print("RateLimitError: You exceeded your current quota. Please wait and try again later.")
        time.sleep(60)  # Wait for a minute before trying again.

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_bot(user_input)
        print("Chatbot: ", response)

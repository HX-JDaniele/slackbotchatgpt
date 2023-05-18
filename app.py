import os
import openai
from dotenv import load_dotenv
import requests
load_dotenv()

OPEN_API_KEY = ("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")
openai.api_key = OPEN_API_KEY

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

prompt = input("Enter your question: ")
response = generate_response(prompt)

if __name__ == "__main__":
    url = 'https://hooks.slack.com/services/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'
    msg = response
    r = requests.post(url, json={'text':msg})
    a = requests.get(url)
    if(r.text == 'ok'):
        print('El mensaje ha sido enviado')
        
    else:
        print(r.text)


def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

print(response)



#curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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

#curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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

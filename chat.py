import os
import openai
import json

def get_api_key():
    openai_key_file = 'KEYS/openai_key.json'
    with open(openai_key_file, 'r', encoding='utf-8') as f:
        openai_key = json.loads(f.read())
    return openai_key['api']

openai.api_key=get_api_key()

def ChatGPT_conversation(conversation, model):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=conversation
    )
    conversation.append({'role':completion.choices[0].message.role,'content':completion.choices[0].message.content})
    return conversation

model = "gpt-3.5-turbo"
conversation = [{'role':'system','content':''}]
with open("chat.txt",'w') as file_object:
    while True:
        content=input("你：")
        if content=="quit":
            break
        file_object.write("你："+ content.strip() + "\n")
        conversation[-1]['content'] = content
        conversation = ChatGPT_conversation(conversation, model)
        message = conversation[-1]
        file_object.write(message['role'] + ":" + message['content'].strip() + "\n")
        print('{0}: {1}\n'.format(message['role'].strip(), message['content'].strip()))
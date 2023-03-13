import os
import openai
import json

def get_api_key():
    openai_key_file = 'KEYS/openai_key.json'
    with open(openai_key_file, 'r', encoding='utf-8') as f:
        openai_key = json.loads(f.read())
    return openai_key['api']

openai.api_key=get_api_key()

def ChatGPT_conversation(conversation):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    conversation.append({'role':completion.choices[0].message.role,'content':completion.choices[0].message.content})
    return conversation

conversation=[]
while True:
    content=input("你：")
    if content=="quit":
        break
    conversation.append({'role':'system','content':content})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

with open("chat.txt",'w') as file_object:
    for i in conversation:
        file_object.write(i['role']+":"+i['content'].strip()+"\n")


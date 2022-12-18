import requests as rq
import yaml
import random 

with open('configFile.yml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)   
    #print(data)

link = data['parameters']['apiUrl'] + data['parameters']['token']
apiMethod = '/sendMessage'
key = random.randint(0,4)
msg = data['recordatorios'][key]

rq.post(link + apiMethod, data = {'chat_id': data['parameters']['chatId'], 'text' : msg})







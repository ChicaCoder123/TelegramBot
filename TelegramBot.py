import requests as rq
import yaml
from random import choice

with open('ConfigFile.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)   
    #print(data)

link = data['parameters']['apiUrl'] + data['parameters']['token']
apiMethod = '/sendMessage'
msg = choice(data['recordatorios']) #Es un método que elige "al azar" un value del diccionario

rq.post(link + apiMethod, data = {'chat_id': data['parameters']['chatId'], 'text' : msg})







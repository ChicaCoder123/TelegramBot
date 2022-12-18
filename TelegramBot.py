import requests as rq
import yaml
from random import choice

with open('ConfigFile.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)   
    baseUrl = data['parameters']['apiUrl']
    #print(data)

link = baseUrl + data['parameters']['token'] 
#Se debería hacer con urllib.parse.join() en realidad y no con '+' pero 
#no concatenaba los urls como yo quería
apiMethod = '/sendMessage'
msg = choice(data['recordatorios']) #Es un método que elige "al azar" un value del diccionario


rq.post(link + apiMethod, data = {'chat_id': data['parameters']['chatId'], 'text' : msg})




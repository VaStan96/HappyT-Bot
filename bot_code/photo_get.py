import requests
import json

def get_pic(animal):
    if animal == 'dog':
        r = requests.get('https://dog.ceo/api/breeds/image/random')
        x = json.loads(r.content)
        return x['message']
    elif animal == 'cat':
        r = requests.get('https://cataas.com/cat?html=true&json=true')
        x = json.loads(r.content)
        return f"https://cataas.com/cat"
    elif animal == 'fox':
        r = requests.get('https://randomfox.ca/floof')
        x = json.loads(r.content)
        return x['image']
    elif animal == 'duck':
        r = requests.get('https://random-d.uk/api/random')
        x = json.loads(r.content)
        return x['url']
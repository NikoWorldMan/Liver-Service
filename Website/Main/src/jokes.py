import json #library, dictonary, javascript object.
import requests

def get_random():
    url = 'https://api.chucknorris.io/jokes/random'
    r = requests.get(url)
    joke = json.loads(r.text) #gjør om til python object
    return joke.get('value', 'Fant ikke vits') #gets the value from the webpages dictonary, which is the jokes we want from said website

print(get_random())

def get_categry():
    url = 'https://api.chucknorris.io/jokes/random?category={category}'

def get_search():
    url = 'https://api.chucknorris.io/jokes/search?query={query}'


get_random()
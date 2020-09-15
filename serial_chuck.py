#!/usr/local/bin/python3

#DevNet  Challenge2

import json
import requests

url = 'https://api.chucknorris.io/jokes/random'

def get_chuck_joke(api):
    """
    Get a random joke from the Chuck Norris API and return the serial JSON
    :param api:
    :return:serial JSON
    """
    payload = {}
    headers = {
    }

    resp = requests.request("GET", url, headers=headers, data=payload)
    jResp = json.loads(resp.text.encode('utf8'))
    return(jResp['value'])
    
    
    
    
    # resp = requests.get(api)  #  TASK 1 - use requests to get a joke.
    # response = resp.json()
    # return response #  TASK 2 - return the response in JSON format

if __name__ == '__main__':
      
    joke = get_chuck_joke(url) 
    print(f'A random Chuck Norris joke: {joke}')  #  TASK 4 - print just a joke without any superfluous symbols

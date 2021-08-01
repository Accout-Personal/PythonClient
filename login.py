from typing import final
import requests
import env

def login(username,password):
    response = requests.post(env.host+"/progettolaurea/public/api/login",data={'username':username,'password':password},headers={'Accept':env.impostazione})
    response = response.json()
    if('messagge' in response.keys()):
        print(response['messagge'])
        return response['messagge']
    else:
        env.token = response["token"]


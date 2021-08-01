import requests
import env

class EntrataC:
    def __init__(self,token):
        self.token =  token
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": env.impostazione}

    def get_all(self):
        response = requests.get(env.host+env.Url+"gen/pro/resp/entrata/",headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)

    def get_key(self,id):
        response = requests.get(env.host+env.Url+"gen/pro/entrata/key/"+env.self,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)
        
             

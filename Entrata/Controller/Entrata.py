import requests
import env

class EntrataC:
    def __init__(self,token):
        self.token =  token
        self.url = "gen/pro/resp/entrata/"
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": env.impostazione}

    def GetAll(self):
        response = requests.get(env.host+env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)

    def GetKey(self,id):
        response = requests.get(env.host+env.Url+self.url+"key/"+id,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)
        
             

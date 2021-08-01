import requests
import env

class CommessaC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/commessa/"
    
    def GetAll(self):
        response = requests.get(env.host + env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            print( response.json())
            raise Exception("Errore. ",response.status_code)

    def GetKey(self,key):
        response = requests.get(env.host + env.Url+self.url+'key/'+key,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)
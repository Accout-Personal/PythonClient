import requests
import env

class StipendioC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/stipendio/"
    
    def GetAll(self):
        response = requests.get(env.host + env.Url+self.url,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ",response.status_code)
            
    def GetSelf(self):
        response = requests.get(env.host + env.Url+self.url+'self/',headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)
            
    def GetKey(self,key):
        response = requests.get(env.host + env.Url+self.url+'key/'+key,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)
            
    def Insert(self, body):
        response = requests.post(
            env.host + env.Url+self.url+'insert', data=body, headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()

    def Delete(self,body):
        response = requests.post(env.host + env.Url+self.url+'delete',data=body,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
    
    def Update(self,body):
        response = requests.post(env.host + env.Url+self.url+'update',data=body,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
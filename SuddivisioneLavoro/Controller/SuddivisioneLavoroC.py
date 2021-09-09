import requests
import env

class SuddivisioneLavoroC:
    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/suddivisione_lavoro/"
    
    def GetKey(self,keys):
        response = requests.get(env.host+env.Url+self.url+"ckey",headers=self.credenziali,data=keys)
        if response.ok:
            return response.json()
        else:
            Exception("Errore. ", response.json())
        
    def GetAll(self):
        response = requests.get(env.host+env.Url+self.url+"all",headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            Exception("Errore. ",response.json())

    def Insert(self,request):
        response = requests.post(env.host+env.Url +self.url+"insert",headers=self.credenziali,data=request)
        if response.ok:
            return response.json()
        else:
            return response.json()

    def Delete(self,body):
        response = requests.post(env.host + env.Url+self.url+"delete",data=body,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
    
    def Update(self,body):
        response = requests.post(env.host + env.Url+self.url+"update",data=body,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
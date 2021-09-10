import requests
import env

class SuddivisioneLavoroC:
    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/suddivisione_lavoro/"
    
    def GetKey(self,keys):
        response = requests.get(env.host+env.Url+self.url+"ckey",headers=self.credenziali,params=keys)
        if response.ok:
            return response.json()
        else:
            response.json()
            Exception("Errore. ", response.json())
        
    def GetAll(self):
        response = requests.get(env.host+env.Url+self.url+"all",headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
            Exception("Errore. ",response.json())

    def Insert(self,request):
        response = requests.post(env.host+env.Url +self.url+"insert",headers=self.credenziali,data=request)
        if response.ok:
            return response.json()
        else:
            return response.json()
            Exception("Errore. ",response.json())

    def Delete(self,body):
        response = requests.post(env.host + env.Url+self.url+"delete",data=body,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            Exception("Errore. ",response.json())
    
    def Update(self,body):
        print(body)
        response = requests.post(env.host + env.Url+self.url+"update",data=body,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
            Exception("Errore. ",response.json())
    
    def GetAllDip(self):
        dip_url = "gen/pro/resp/dipendente/type/pro"
        response = requests.get(env.host + env.Url+dip_url,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            Exception("Errore. ",response.json())
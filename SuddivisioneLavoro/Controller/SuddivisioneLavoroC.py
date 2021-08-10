import requests
import env

class SuddivisioneLavoroC:
    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/suddivisione_lavoro/all"
        
    def GetAll(self):
        response = requests.get(env.host+env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)

    def Insert(self,request):
        response = requests.post(env.host+env.Url + "gen/suddivisione_lavoro/insert",headers=self.credenziali,data=request)
        if response.ok:
            return response.json()
        else:
            return response.json()

    def Delete(self,body):
        response = requests.post(env.host + env.Url+'gen/suddivisione_lavoro/delete',data=body,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()
    
    def Update(self,body):
        response = requests.post(env.host + env.Url+'gen/suddivisione_lavoro/update',data=body,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()
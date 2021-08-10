import requests
import env
class AggiornamentoC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/aggiornamento/"
    
    def GetAll(self):
        response = requests.get(env.host + env.Url+self.url,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            #raise Exception("Errore. ",response.status_code)
            return response.json()

    def Insert(self,request):
        response = requests.post(env.host + env.Url+"aggiornamento/insert",headers=self.credenziali,data=request)
        if response.ok:
            return response.json()
        else:
            #raise Exception("Errore. ",response.status_code)
            return response.json()

    def Delete(self,body):
        response = requests.post(env.host + env.Url+self.url+'delete',data=body,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()
            
            

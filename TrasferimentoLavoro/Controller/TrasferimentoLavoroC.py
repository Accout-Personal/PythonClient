import requests
import env

class TrasferimentoLavoroC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/trasferimento_lavoro/"
    
    def GetAll(self):
        response = requests.get(env.host + env.Url+self.url+'all',headers=self.credenziali)
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
        print(env.host + env.Url+self.url+'key/'+key)
        response = requests.get(env.host + env.Url+self.url+'key/'+key,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ",response.status_code)


    def Insert(self,request):
        response = requests.post(env.host+env.Url + "gen/pro/trasferimento_lavoro/insert",headers=self.credenziali,data=request)
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
    
    def ConfirmLavoro(self,body):
        response = requests.post(env.host + env.Url+self.url+'confirm',data=body,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
    
    def GetAllDip(self):
        dip_url = "gen/pro/resp/dipendente/type/pro"
        response = requests.get(env.host + env.Url+dip_url,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            Exception("Errore. ",response.json())
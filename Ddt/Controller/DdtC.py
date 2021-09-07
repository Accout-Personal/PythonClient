import requests
import env

class DdtC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/ddt/"
        self.contabileUrl = "gen/pro/resp/contabile/"
        self.NonContabileUrl = "gen/pro/resp/non_contabile/"

    def GetAll(self):
        response = requests.get(env.host + env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ",response.status_code)
                        
    def GetKey(self,key):
        response = requests.get(env.host + env.Url+self.url+'key/'+key,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)

    def ContabileKey(self,key):
        response = requests.get(
            env.host + env.Url+self.contabileUrl+'key/'+key, headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            raise Exception("Errore. ", response.status_code)

    def ContabileInsert(self,key):
        response = requests.get(
            env.host + env.Url+self.contabileUrl+'key/'+key, headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            raise Exception("Errore. ", response.status_code)


    def ContaBileUpdate(self,body):
        response = requests.post(env.host + env.Url+self.contabileUrl+'update',data=body,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()

    def ContaBileDelete(self,body):
        response = requests.post(env.host + env.Url+self.contabileUrl+'delete',data=body,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()

    def NonContabileKey(self,key):
        response = requests.get(env.host + env.Url+self.NonContabileUrl+'key/'+key,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)

    def NonContabileInsert(self,body):
        response = requests.post(env.host + env.Url+self.NonContabileUrl+'insert',data=body,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()

    def NonContabileDelete(self,body):
        response = requests.post(env.host + env.Url+self.NonContabileUrl+'delete',data=body,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()
    
    def NonContabileUpdate(self,body):
        response = requests.post(env.host + env.Url+self.NonContabileUrl+'update',data=body,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()
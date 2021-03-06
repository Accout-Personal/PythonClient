import requests
import env

class CommessaC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/commessa/"
    
    def GetAll(self):
        response = requests.get(env.host + env.Url+self.url,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ",response.status_code)

    def GetKey(self,key):
        response = requests.get(env.host + env.Url+self.url+'key/'+key,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ",response.status_code)

    def Insert(self,body):
        response = requests.post(env.host+env.Url+self.url+"insert",headers=self.credenziali,data=body)
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

    #Mi serve per prendere tutti i clienti per generare lista selezioni
    def GetAllCliente(self):
        self.Clienteurl = "gen/pro/resp/cliente/"
        response = requests.get(env.host + env.Url+self.Clienteurl,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ",response.status_code)
        
    def GetAllModelli(self):
        self.ModelliUrl = "gen/pro/resp/listino_prezzi/"
        response = requests.get(env.host + env.Url+ self.ModelliUrl,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ",response.status_code)
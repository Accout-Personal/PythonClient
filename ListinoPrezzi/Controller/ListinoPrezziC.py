import requests
import env

class ListinoPrezziC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/listino_prezzi/"
    
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

    def Insert(self,request):
        response = requests.post(env.host+env.Url+self.url+"insert",headers=self.credenziali,data=request)
        if response.ok:
            return response.json()
        else:
            return response.json()
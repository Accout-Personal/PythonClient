import requests
import env

class MacchinePubblicheC:
    def __init__(self,token):
        self.token =  token
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": env.impostazione}
        self.url = "gen/pro/macchine_pubbliche/"

    def GetAll(self):
        response = requests.get(env.host+env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)

    def GetKey(self,codice_macchina):
        response = requests.get(env.host+env.Url+self.url+"key/",params={"codice_macchina": codice_macchina},headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            print(response.json())
            raise Exception("Errore. ",response.status_code)
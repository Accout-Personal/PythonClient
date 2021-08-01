import requests
import env

class UtilizzazioneC:
    def __init__(self,token):
        self.token =  token
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": env.impostazione}
        self.url = "gen/pro/res/utilizzazione/"

    def GetAll(self):
        response = requests.get(env.host+env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)

    def get_self(self):
        env.Url = ""
        response = requests.get(env.host+env.Url+"gen/pro/utilizzazione/"+env.self,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)
        
             


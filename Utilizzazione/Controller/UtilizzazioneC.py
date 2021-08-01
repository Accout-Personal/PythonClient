import requests
import env

class UtilizzazioneC:
    def __init__(self,token):
        self.token =  token
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": env.impostazione}
        self.rotta = env.host+env.Url

    def get_all(self):
        response = requests.get(env.host+env.Url,headers=self.credenziali)
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
        
             


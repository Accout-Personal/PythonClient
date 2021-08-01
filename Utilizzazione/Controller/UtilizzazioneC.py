import requests
import env

class UtilizzazioneC:
    def __init__(self,token):
        self.token =  token
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/utilizzazione/"
        self.url2 = "gen/pro/utilizzazione/self"
    def GetAll(self):
        response = requests.get(env.host+env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)

    def GetSelf(self):
        response = requests.get(env.host+env.Url+self.url2,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)
            
            
        
             


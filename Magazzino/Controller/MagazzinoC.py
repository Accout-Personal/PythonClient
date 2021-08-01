import requests
import env

class MagazzinoC:
    def __init__(self,token):
        self.token =  token
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": env.impostazione}
        self.url = "magazzino/"
    def GetAll(self):
        response = requests.get(env.host+env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print(response.json())
        else:
            raise Exception("Errore. ",response.status_code)
            
            
        
             


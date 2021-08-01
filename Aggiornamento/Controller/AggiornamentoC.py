import requests
import env
import cenv
class AggiornamentoC:

    def __init__(self,token):
        self.token =  token
        self.impostazioni = "application/json"
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": self.impostazioni}
    
    def GetAll(self):
        response = requests.get(env.host + env.Url+cenv.localUrl+'/',headers=self.credenziali)
        if response.ok:
            print("va bene")
            #print(type(response.json()[0]["tipo_pezzo"]))
            #print(response.json()[0]["tipo_pezzo"])
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)

    def GetSelf(self):
        response = requests.get(env.host + env.Url+cenv.localUrl+'/self',headers=self.credenziali)
        if response.ok:
            print("va bene")
            #print(type(response.json()[0]["tipo_pezzo"]))
            #print(response.json()[0]["tipo_pezzo"])
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)
    def delete(self):
        return 0
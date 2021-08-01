import requests
import env
class AggiornamentoC:

    def __init__(self):
        self.impostazioni = "application/json"
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": self.impostazioni}
        self.url = "gen/pro/resp/aggiornamento/"
    
    def GetAll(self):
        response = requests.get(env.host + env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print("va bene")
            #print(type(response.json()[0]["tipo_pezzo"]))
            #print(response.json()[0]["tipo_pezzo"])
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)

    def GetSelf(self):
        response = requests.get(env.host + env.Url+self.url+'self',headers=self.credenziali)
        if response.ok:
            print("va bene")
            #print(type(response.json()[0]["tipo_pezzo"]))
            #print(response.json()[0]["tipo_pezzo"])
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)
    def delete(self):
        return 0
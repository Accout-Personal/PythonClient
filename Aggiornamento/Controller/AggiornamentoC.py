import requests
import env
class AggiornamentoC:

    def __init__(self,token):
        self.token =  token
        self.impostazioni = "application/json"
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": self.impostazioni}
    
    def GetAll(self):
        response = requests.get("http://localhost/progettolaurea/public/api/authed/gen/pro/resp/utilizzazione/",headers=self.credenziali)
        if response.ok:
            print("va bene")
            #print(type(response.json()[0]["tipo_pezzo"]))
            print(response.json()[0]["tipo_pezzo"])
        else:
            raise Exception("Errore. ",response.status_code)

    def delete(self):
        return 0
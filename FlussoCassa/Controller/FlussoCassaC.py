import requests
import env

class FlussoCassaC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/cashflow/all"

    def GetAll(self):
        response = requests.get(env.host + env.Url+self.url,headers=self.credenziali)
        if response.ok:
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ",response.status_code)
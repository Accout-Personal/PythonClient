import requests
import env

class TransazioneRetribuzioneC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/transazione_retribuzione/"
    
    def GetAll(self):
        response = requests.get(env.host + env.Url+self.url,headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ",response.status_code)
            

    #def GetKey(self,key):
    #    response = requests.get(env.host + env.Url+self.url+'key/'+key,headers=self.credenziali)
    #    if response.ok:
    #        print("va bene")
    #        return response.json()
    #    else:
    #        raise Exception("Errore. ",response.status_code)

    def GetCKey(self,dipendente_tran,data_retribuzione):
        payload = {'dipendente_tran':dipendente_tran,'data_retribuzione':data_retribuzione}
        response = requests.get(env.host + env.Url+self.url+'ckey/',headers=self.credenziali,params=payload)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)
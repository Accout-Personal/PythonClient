import requests
import env

class TrasazioneStipendioC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/transazione_stipendio/"
    
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

    def GetCKey(self,uscita_effettuata,data_stipendio,stipendio_dipendente):
        payload = {'uscita_effettuata':uscita_effettuata,'data_stipendio':data_stipendio,'stipendio_dipendente':stipendio_dipendente}
        response = requests.get(env.host + env.Url+self.url+'ckey/',headers=self.credenziali,params=payload)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            raise Exception("Errore. ",response.status_code)
    
    def Insert(self, body):
        response = requests.post(
            env.host + env.Url+self.url+'insert', data=body, headers=self.credenziali)
        if response.ok:
            print("va bene")
            return response.json()
        else:
            return response.json()
            raise Exception("Errore. ", response.status_code)
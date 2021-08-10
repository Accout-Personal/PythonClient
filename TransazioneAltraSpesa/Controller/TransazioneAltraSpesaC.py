import requests
import env

class TransazioneAltraSpesaC:

    def __init__(self):
        self.credenziali = {"Authorization": "Bearer "+env.token,"Accept": env.impostazione}
        self.url = "gen/pro/resp/transazione_altra_spesa/"
    
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

    def GetCKey(self,uscita_effettuata,altra_spesa):
        payload = {'uscita_effettuata':uscita_effettuata,'altra_spesa':altra_spesa}
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
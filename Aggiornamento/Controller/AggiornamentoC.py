import env
class AggiornamentoC:

    def __init__(self,token):
        self.token =  token
        self.impostazioni = "application/json"
        self.credenziali = {"Authorization": "Bearer "+self.token,"Accept": self.impostazioni}
    
    def GetHost(self):
        print(env.host)
        return env.host
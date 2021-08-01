from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC

import env

print(env.host)
env.host = "new host"
print(env.host)
Agg = AggiornamentoC("token")
print(Agg.GetHost())
#aggiornamento.get_host()
##from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC

print(env.host)
print(env.host)

#prova = UtilizzazioneC(login.get_Host())
#prova.get_all()
#provaLog = login("user6","password")

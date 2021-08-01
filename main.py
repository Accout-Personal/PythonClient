
from login import login
from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC

import env

print(env.host)
env.host = "new host"
print(env.host)
val = "ciccio"
print(val)
Agg = AggiornamentoC("token")
print(Agg.GetHost())
#aggiornamento.get_host()
#prova = UtilizzazioneC(login.get_Host())
#prova.get_all()
#provaLog = login("user6","password")

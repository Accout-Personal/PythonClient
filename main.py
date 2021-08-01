
from login import login
from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC

##from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC
import env
print(env.host)
val = "ciccio"
print(val)

prova = UtilizzazioneC(login.get_Host())
prova.get_all()
#provaLog = login("user6","password")

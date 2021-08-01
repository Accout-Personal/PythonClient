import requests
import env
from login import login
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC
from Entrata.Controller.EntrataC import EntrataC
from NonContabile.Controller.NonContabileC import NonContabileC
from Contabile.Controller.ContabileC import ContabileC
from UscitaEffettuata.Controller.UscitaEffettuataC import UscitaEffettuataC

#log = login('user4','password')
env.token ="bCrjUbnjZgVpVFsjw4DaLJ3l2nAAZYGVekduhbWJ"
print(env.token)
#print(AggiornamentoC().GetAll())
#print(EntrataC().GetAll())
#print(NonContabileC().GetAll())
#print(ContabileC().GetAll())
#print(UscitaEffettuataC().GetAll())
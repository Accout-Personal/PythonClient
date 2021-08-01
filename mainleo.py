import requests
import env
from login import login
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC
from Entrata.Controller.EntrataC import EntrataC

log = login('user4','password')
print(env.token)
#print(AggiornamentoC().GetAll())
print(EntrataC().GetAll())
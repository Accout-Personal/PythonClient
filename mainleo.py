import requests
import env
from login import login
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC
from Entrata.Controller.EntrataC import EntrataC
from NonContabile.Controller.NonContabileC import NonContabileC
from Contabile.Controller.ContabileC import ContabileC
from UscitaEffettuata.Controller.UscitaEffettuataC import UscitaEffettuataC
from TransazioneStipendio.Controller.TransazioneStipendioC import TrasazioneStipendioC
from TransazioneAltraSpesa.Controller.TransazioneAltraSpesaC import TransazioneAltraSpesaC
from TransazioneRetribuzione.Controller.TransazioneRetribuzioneC import TransazioneRetribuzioneC
from AltraSpesa.Controller.AltraSpesaC import AltraSpesaC
#log = login('user4','password')
env.token ="bCrjUbnjZgVpVFsjw4DaLJ3l2nAAZYGVekduhbWJ"
print(env.token)
#print(AggiornamentoC().GetAll())
#print(EntrataC().GetAll())
#print(NonContabileC().GetAll())
#print(ContabileC().GetAll())
#print(UscitaEffettuataC().GetAll())
#print(TrasazioneStipendioC().GetAll())
#print(TrasazioneAltraSpesa().GetAll())
#print(TransazioneRetribuzioneC().GetAll())
print(AltraSpesaC().GetAll())
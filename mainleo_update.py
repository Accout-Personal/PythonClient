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
from RetribuzioneVariabile.Controller.RetribuzioneVariabileC import RetribuzioneVariabileC
from Stipendio.Controller.StipendioC import StipendioC
from Dipendente.Controller.DipendenteC import DipendenteC
from Cliente.Controller.ClienteC import ClienteC
from ListinoPrezzi.Controller.ListinoPrezziC import ListinoPrezziC
from Commessa.Controller.CommessaC import CommessaC
from TrasferimentoLavoro.Controller.TrasferimentoLavoroC import TrasferimentoLavoroC
from Ddt.Controller.DdtC import DdtC
from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC
from Code.Controller.CodeC import CodeC

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
#print(AltraSpesaC().GetAll())
#print(RetribuzioneVariabileC().GetAll())
#print(StipendioC().GetAll())
#print(DipendenteC().GetAll())
#print(ClienteC().GetAll())
#print(ListinoPrezziC().GetAll())
""" print(CommessaC().GetAll()) """
""" print(TrasferimentoLavoroC().GetAll()) """
""" print(DdtC().GetAll()) """
""" print(UtilizzazioneC().GetSelf()) """
#print(CodeC().GetSelf())
""" print(CodeC().GetAll()) """

#ins_entrata = {'numero_fattura':3,
#'data':'2021-08-06',
#'importo_entrata':0
#}
#print(EntrataC().Insert(ins_entrata))
#delete_entrata = {'numero_fattura':3}
#upd_entrata = {
#    'numero_fattura':3,
#    'data':'2021-08-08',
#    'importo_entrata':0
#}
#print(EntrataC().Update(upd_entrata))

upd_noncontabile = {
    'ddt':7,
    'data':'2021-08-06',
    'luogo_destinazione':'idem',
}

#print(NonContabileC().Update(upd_noncontabile))


upd_contabili ={
    'ddt':5,
    'data':'09-08-2021',
    'luogo_destinazione':'idem',
}
#print(ContabileC().Update(upd_contabili))

#da rivedere!
upd_utilizzazione ={
    'tipo_pezzo':'pezzo test',
    'data_e_ora':'2021-08-06 00:00:00',
    'quantita':'100',
    'durata':'3',
    'dipendente':'CRVLTT84M49H446V',
    'codice_macchina':'1B',
    'tipo_macchina':'braccio',
}
#print(UtilizzazioneC().Update(upd_utilizzazione))


upd_uscita ={
    'id_transazione':23,
    'data_esecuzione':'06-08-2021',
    'importo_effettuato':'300'
}
#print(UscitaEffettuataC().Update(upd_uscita))

upd_altra_spesa ={
    'codice':1,
    'importo':200,
    'data':'2021-10-08',
    'causale':'test causale'
}

#print(AltraSpesaC().Update(upd_altra_spesa))

stipendio_update ={
    'data':'2021-08-10',
    'dipendente_stip':'PPRRCN88C02H501O',
    'giorni_ferie':1,
    'ore_straordinario':20,
    'ore_lavoro':500
}

#print(StipendioC().Update(stipendio_update))

dipendente_insert ={
    'CF':'cftest',
    'password':'password',
    'password_confirmation':'password',
    'tipo_dipendente':'gen',
    'importo_orario_feriale':8,
    'importo_orario_straordinario':15,
    'importo_orario_regolare':10,
    'IBAN':'IBANtest',
    'username':'user9',
    'data_di_nascita':'1990-01-01',
    'nome_cognome':'pippo paperino',
}

#print(DipendenteC().Insert(dipendente_insert))
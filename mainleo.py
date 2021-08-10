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

ins_noncontabile = {'ddt':7,
'data':'2021-08-06',
'luogo_destinazione':'idem',}
#print(NonContabileC().Insert(ins_noncontabile))

ins_contabili ={'ddt':8,
'data':'07-08-2021',
'luogo_destinazione':'idem',
}
#print(ContabileC().Insert(ins_contabili))
ins_utilizzazione ={
    'tipo_pezzo':'pezzo test',
    'data_e_ora':'06-08-2021',
    'quantita':'100',
    'durata':'3',
    'dipendente':'CRVLTT84M49H446V',
    'codice_macchina':'1B',
    'tipo_macchina':'braccio',
}
#print(UtilizzazioneC().Insert(ins_utilizzazione))
ins_uscita ={
    'data_esecuzione':'06-08-2021',
    'importo_effettuato':'300'
}
#print(UscitaEffettuataC().Insert(ins_uscita))

ins_tran_stip={
    'uscita_effettuata':24,
    'data_stipendio':'2020-12-01',
    'stipendio_dipendente':'TZIBRN90B03A794N',
}
#print(TrasazioneStipendioC().Insert(ins_tran_stip))

ins_tran_spesa ={
    'uscita_effettuata':23,
    'altra_spesa':4,
}

#print(TransazioneAltraSpesaC().Insert(ins_tran_spesa))

ins_tran_retr ={
    'uscita_effettuata':25,
    'data_retribuzione':'2020-12-31',
    'dipendente_tran':'PPRRCN88C02H501O'
}

#print(TransazioneRetribuzioneC().Insert(ins_tran_retr))

ins_altra_spesa ={
    'importo':200,
    'data':'2021-10-08',
    'causale':'test causale'
}

print(AltraSpesaC().Insert(ins_altra_spesa))
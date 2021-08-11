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
env.token ="n5duaBYWapj7jYwDx2GTv56equHrDsaCmcUqUeQ0"
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

del_noncontabile = {
    'ddt':7,
}

#print(NonContabileC().Delete(del_noncontabile))

del_contabili ={'ddt':8}
#print(ContabileC().Delete(del_contabili))

del_aggiornamento = {'id':1}
#print(AggiornamentoC().Delete(del_aggiornamento))

#TODO add id
del_utilizzazione ={
    'tipo_pezzo':'pezzo test',
    'data_e_ora':'06-08-2021',
    'quantita':'100',
    'durata':'3',
    'dipendente':'CRVLTT84M49H446V',
    'codice_macchina':'1B',
    'tipo_macchina':'braccio',
}
#print(UtilizzazioneC().Delete(ins_utilizzazione))

del_uscita ={
'id_transazione':23,
}
#print(UscitaEffettuataC().Delete(del_uscita))

del_altra_spesa ={
    'codice':1,
}

#print(AltraSpesaC().Delete(del_altra_spesa))

del_retribuzione ={
    'data':'2021-08-10',
    'dipendente_retr':'PPRRCN88C02H501O'
}

#print(RetribuzioneVariabileC().Delete(del_retribuzione))


stipendio_delete ={
    'data':'2021-08-10',
    'dipendente_stip':'PPRRCN88C02H501O',
}

#print(StipendioC().Delete(stipendio_delete))

dipendente_delete ={
    'CF':'cftest',
}

#print(DipendenteC().Delete(dipendente_delete))

cliente_delete ={
    'PIVA':'23568472720'
}

#print(ClienteC().Delete(cliente_delete))
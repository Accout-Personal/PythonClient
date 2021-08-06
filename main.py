from TrasferimentoLavoro.Controller.TrasferimentoLavoroC import TrasferimentoLavoroC
from Code.Controller.CodeC import CodeC
from MacchinePubbliche.Controller.MacchinePubblicheC import MacchinePubblicheC
from SuddivisioneLavoro.Controller.SuddivisioneLavoroC import SuddivisioneLavoroC
from Magazzino.Controller.MagazzinoC import MagazzinoC
from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC


prova = TrasferimentoLavoroC()
dizionario = {'commessa': '11','dipendente': 'GNTSNG02C51I209D','data_trasferimento': '2021/08/06','valore_trasferito': '9','quantita_trasferita': '2','destinatario': 'PCSGVS83M23M251S'}
print(prova.Insert(dizionario))

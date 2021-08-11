from Cliente.Controller.ClienteC import ClienteC
from ListinoPrezzi.Controller.ListinoPrezziC import ListinoPrezziC
from Commessa.Controller.CommessaC import CommessaC
from Ddt.Controller.DdtC import DdtC
from TrasferimentoLavoro.Controller.TrasferimentoLavoroC import TrasferimentoLavoroC
from Code.Controller.CodeC import CodeC
from MacchinePubbliche.Controller.MacchinePubblicheC import MacchinePubblicheC
from SuddivisioneLavoro.Controller.SuddivisioneLavoroC import SuddivisioneLavoroC
from Magazzino.Controller.MagazzinoC import MagazzinoC
from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC


prova = ListinoPrezziC()
#dizionarioCommessaDelete = {'codice_merce': '4'}
#dizionarioListinoPrezzi = {'modello': '11200','valore_cliente': '15.50','valore_dipendente': '7.80'}
print(prova.Delete(dizionarioListinoPrezzi))
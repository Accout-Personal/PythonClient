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


prova = AggiornamentoC()
dizionario = {'id': '200'}
print(prova.Delete(dizionario))

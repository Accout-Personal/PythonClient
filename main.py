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


prova = TrasferimentoLavoroC()
dizionario = {'id': '3','codice_trasf': '2','commessa': '9','dipendente': 'GNTSNG02C51I209D','data_trasferimento': '2021/10/08','valore_trasferito': '-14','quantita_trasferita': '2','confermato': '1'}
dizionario2 = {'id': int(dizionario['id'])+1,'codice_trasf': dizionario['codice_trasf'], 'commessa': dizionario['commessa'], 'data_trasferimento': dizionario['data_trasferimento'],'valore_trasferito': int(dizionario['valore_trasferito'])*(-1),'quantita_trasferita': dizionario['quantita_trasferita'], 'confermato': dizionario['confermato']}
print(prova.Update(dizionario,dizionario2))
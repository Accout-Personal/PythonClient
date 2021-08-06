from MacchinePubbliche.Controller.MacchinePubblicheC import MacchinePubblicheC
from SuddivisioneLavoro.Controller.SuddivisioneLavoroC import SuddivisioneLavoroC
from Magazzino.Controller.MagazzinoC import MagazzinoC
from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC


prova = SuddivisioneLavoroC()
dizionario = {'commessa': '11','dipendente': 'GNTSNG02C51I209D','quantita_assegnata': '3',}
print(prova.Insert(dizionario))

from Code.Controller.CodeC import CodeC
from MacchinePubbliche.Controller.MacchinePubblicheC import MacchinePubblicheC
from SuddivisioneLavoro.Controller.SuddivisioneLavoroC import SuddivisioneLavoroC
from Magazzino.Controller.MagazzinoC import MagazzinoC
from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC


prova = CodeC()
dizionario = {'codice_macchina': '4B','inizio': '2021/12/04 16:06:22','durata': '2.00','dipendente': 'GNTSNG02C51I209D'}
print(prova.Insert(dizionario))

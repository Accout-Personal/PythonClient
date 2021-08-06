from MacchinePubbliche.Controller.MacchinePubblicheC import MacchinePubblicheC
from SuddivisioneLavoro.Controller.SuddivisioneLavoroC import SuddivisioneLavoroC
from Magazzino.Controller.MagazzinoC import MagazzinoC
from Utilizzazione.Controller.UtilizzazioneC import UtilizzazioneC
from Aggiornamento.Controller.AggiornamentoC import AggiornamentoC


prova = AggiornamentoC()
dizionario = {'dipendente': 'GNTSNG02C51I209D','data': '2021/06/08','quantita': '2','magazzino': 'forbici'}
prova.Insert(dizionario)

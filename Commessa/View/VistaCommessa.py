# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from Commessa.Controller.CommessaC import CommessaC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import copy

class Ui_VistaCommessa(QWidget):
    def __init__(self,key, parent=None):
        super(Ui_VistaCommessa, self).__init__(parent)
        self._translate = QtCore.QCoreApplication.translate
        self.key = key
        VisualizzaWindow = self
        self.controller = CommessaC()
        self.chiamata = self.controller.GetKey(self.key)
        VisualizzaWindow.setObjectName("VisualizzaWindow")
        VisualizzaWindow.resize(800, 600)
        VisualizzaWindow.setWindowTitle(self._translate("VisualizzaWindow", "VisualizzaCliente"))
        self.verticalLayout = QtWidgets.QVBoxLayout(VisualizzaWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalpos = 0

        self.AddSectionLabel('Dettagli')
        self.gridLayout,self.scrollAreaWidgetContents = self.AddScrollArea(200)

        self.traduzione = {
        'numero_commessa':'N.commessa',
        'Qta':'quantita\'',
        'data':'data',
        'cliente':'cliente',
        'nddt_cliente':'DDT',
        'listino_prezzi_modello':'modello',
        'valore_commessa_cliente':'valore commessa dato dal cliente',
        'valore_commessa_dipendente':'valore al dipendente',
        'contabile':'ddt d\'uscita',
        'tessuto':'tessuto',
        'dipendente':'dipendente',
        'quantita_assegnata':'quantita\' assegnata',
        'valore_lavoro':'valore lavorativo',
        'data_conclusione':'data consegna'
        }

        self.listAttr = [
            {'nome':'numero_commessa','width':80},
            {'nome':'Qta','width':80},
            {'nome':'data','width':100},
            {'nome':'cliente','width':200},
            {'nome':'nddt_cliente','width':50},
            {'nome':'listino_prezzi_modello','width':120},
            {'nome':'valore_commessa_cliente','width':100},
            {'nome':'contabile','width':80},
            {'nome':'tessuto','width':80},
        ]
                
        #print(self.chiamata)
        #esclude elemento non desiderato per visualizzazione
        
        self.viewList = copy.deepcopy(self.chiamata)
        print(self.viewList)
        self.exclude = ['suddivisione_lavoro','codice_merce']
        for elem in self.exclude:
            self.viewList.pop(elem)


        self.count = 0
        #print(self.viewList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        for a in self.viewList:
            if(a == 'cliente'):
                self.AddElement(self.gridLayout,self.traduzione['cliente'],0,self.count)
                self.AddElement(self.gridLayout,self.chiamata[a]['nome_azienda'],1,self.count)
                continue
            #inserimento del label
            self.AddElement(self.gridLayout,self.traduzione[a],0,self.count)
            #inserimento del contenuto
            self.AddElement(self.gridLayout,self.chiamata[a],1,self.count)
            self.count += 1

            

        #Sezione della suddivisione lavoro
        self.Lavoro = copy.deepcopy(self.chiamata['suddivisione_lavoro'])
        self.Lavoro_attr = ['dipendente','quantita_assegnata','valore_lavoro','data_conclusione']
        if(len(self.Lavoro)>0):
        
            self.AddSectionLabel('Suddivisione Lavoro')
            self.LavoroGridLayout,self.scrollAreaWidgetContents = self.AddScrollArea(100)

            #Aggiunge l'intestazione della tabella
            for a in range(len(self.Lavoro_attr)):
                

                self.addTableHead(self.traduzione[self.Lavoro_attr[a]],self.LavoroGridLayout,a,self.scrollAreaWidgetContents)
                self.count = 1
                
                if(self.Lavoro_attr[a] == 'dipendente'):
                    for numero in self.Lavoro:
                        #Aggiunge il numero telefono in colonna
                        #print(numero[self.Lavoro_attr[a]])
                        self.AddElement(self.LavoroGridLayout,numero[self.Lavoro_attr[a]]['nome_cognome'],a,self.count)
                        self.count += 1
                    continue
                for numero in self.Lavoro:
                    #Aggiunge il numero telefono in colonna
                    self.AddElement(self.LavoroGridLayout,numero[self.Lavoro_attr[a]],a,self.count)
                    self.count += 1

        ##sezione delle commesse
        #self.commessa = copy.deepcopy(self.chiamata['commessa'])
        #self.commessa_attr = ['numero_commessa','valore_commessa_cliente','listino_prezzi_modello','Qta','nddt_cliente','data']
        #self.traduzione["numero_commessa"] = "numero di commessa"
        #self.traduzione["valore_commessa_cliente"] = "valore della commessa"
        #self.traduzione["listino_prezzi_modello"] = "modello"
        #self.traduzione["Qta"] = "Q.ta"
        #self.traduzione["nddt_cliente"] = "ddt del cliente"
        #self.traduzione["data"] = "data"
        #if(len(self.commessa)>0):
        #    self.AddSectionLabel('Commesse')
        #    self.CommesaGridLayout,self.scrollAreaWidgetContents = self.AddScrollArea(200)
#
        #    #Aggiunge l'intestazione della tabella
        #    for a in range(len(self.commessa_attr)):
        #        self.addTableHead(self.traduzione[self.commessa_attr[a]],self.CommesaGridLayout,a,self.scrollAreaWidgetContents)
        #        self.count = 1
        #        #Popolazione della tabella
        #        for commessa in self.commessa:
        #            #print(commessa)
#
        #            #popola elemento nella tabella
        #            self.AddElement(self.CommesaGridLayout,commessa[self.commessa_attr[a]],a,self.count)
        #            self.count += 1
                    
            
        QtCore.QMetaObject.connectSlotsByName(VisualizzaWindow)

    #Questa funzione aggiunge un label al GridLayout nella posizione x(colonna) e y(riga)
    def AddElement(self,gridLayout,text,x,y,heightMin = 30,HeightMax=30):
        gridLayout
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(label_2.sizePolicy().hasHeightForWidth())
        label_2.setSizePolicy(sizePolicy)
        label_2.setMinimumSize(QtCore.QSize(0, heightMin))
        label_2.setMaximumSize(QtCore.QSize(65535, HeightMax))
        label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        label_2.setObjectName("label_2")
        #self.gridLayout.addWidget(label_2, y, x, 1, 1)
        gridLayout.addWidget(label_2, y, x, 1, 1)
        label_2.setText(self._translate("VisualizzaWindow", "  "+str(text)))
    
    #Aggiunge un scrollArea alla finestra principale
    def AddScrollArea(self,min_size):
        scrollArea = QtWidgets.QScrollArea(self)
        scrollArea.setStyleSheet("background-color: rgb(109, 109, 109);")
        scrollArea.setWidgetResizable(True)
        scrollArea.setObjectName("scrollArea")
        scrollArea.setMinimumSize(QtCore.QSize(0, min_size))
        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 524))
        scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        gridLayout = QtWidgets.QGridLayout(scrollAreaWidgetContents)
        gridLayout.setObjectName("gridLayout")
        scrollArea.setWidget(scrollAreaWidgetContents)
        self.verticalLayout.addWidget(scrollArea)
        return (gridLayout,scrollAreaWidgetContents)

    def AddSectionLabel(self,text):
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)        
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label = QtWidgets.QLabel(self)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(250, 50))       
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self._translate = QtCore.QCoreApplication.translate
        self.label.setText(self._translate("VisualizzaWindow", "<html><head/><body><p align=\"center\">"+text+"</p></body></html>"))
    
    def addTableHead(self,text,grid,pos,widget):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.label_headTelefono = QtWidgets.QLabel(widget)
        sizePolicy.setHeightForWidth(self.label_headTelefono.sizePolicy().hasHeightForWidth())
        self.label_headTelefono.setSizePolicy(sizePolicy)
        self.label_headTelefono.setMinimumSize(QtCore.QSize(0, 20))
        self.label_headTelefono.setObjectName("label_headTelefono")
        grid.addWidget(self.label_headTelefono, 0, pos, 1, 1)
        self.label_headTelefono.setText(text)
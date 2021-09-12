from typing import KeysView
from RetribuzioneVariabile.Controller.RetribuzioneVariabileC import RetribuzioneVariabileC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
import copy

class Ui_VistaRetribuzione(QWidget):
    def __init__(self,keys, parent=None):
        super(Ui_VistaRetribuzione, self).__init__(parent)
        self._translate = QtCore.QCoreApplication.translate
        self.keys = {'dipendente':keys['dipendente_retr'],
                        'data':keys['data']}
        VisualizzaWindow = self
        self.controller = RetribuzioneVariabileC()
        self.chiamata = self.controller.GetKey(self.keys)
        VisualizzaWindow.setObjectName("VisualizzaWindow")
        VisualizzaWindow.resize(800, 600)
        VisualizzaWindow.setWindowTitle(self._translate("VisualizzaWindow", "VisualizzaRetribuzione"))
        self.verticalLayout = QtWidgets.QVBoxLayout(VisualizzaWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalpos = 0

        self.AddSectionLabel('Dettagli')
        self.gridLayout,self.scrollAreaWidgetContents = self.AddScrollArea(100)

        self.traduzione = {
        'data':' data',
        'dipendente_retr':' Dipendente',
        'importo_retribuzione':'importo retribuzione',
        'nome_cognome':'nome cognome'
        }
        self.traduzione_2 = {
            'id_transazione':' id',
            'data_esecuzione':' data esecuzione',
            'importo_effettuato':' importo effettuato',
        }
        
                
        #print(self.chiamata)
        #esclude elemento non desiderato per visualizzazione
        self.viewList = copy.deepcopy(self.chiamata)
        self.count = 0
        #print(self.viewList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        for a in self.viewList:
            for y in a:
                if(y != "transazione_retribuzione"):
                    
                    if(y != "dipendente"):
                        #inserimento del label
                        self.AddElement(self.gridLayout,self.traduzione[y],0,self.count)
                        #inserimento del contenuto
                        self.AddElement(self.gridLayout,a[y],1,self.count)
                    else:
                        #inserimento del label
                        self.AddElement(self.gridLayout,self.traduzione['nome_cognome'],0,self.count)
                        #inserimento del contenuto
                        self.AddElement(self.gridLayout,a[y]['nome_cognome'],1,self.count)
                else:
                    if(len(self.viewList[0]['transazione_retribuzione'])>0 and y != "dipendente"):
                        self.AddSectionLabel('Transazione_retribuzione')
                        self.StipendioGridLayout,self.scrollAreaWidgetContents = self.AddScrollArea(0)
                        self.count2 = self.count
                        self.count3 = self.count
                        for x in self.viewList[0]['transazione_retribuzione']:
                            self.count2 = self.count3
                            for z in x:
                                if(z == "uscita_effettuata"):
                                    for b in self.traduzione_2:
                                        self.addTableHead(b,self.StipendioGridLayout,self.count2,self.scrollAreaWidgetContents)
                                        self.AddElement(self.StipendioGridLayout,x[z][b],self.count2,self.count)
                                        self.count2 += 1
                            self.count += 1        
                self.count += 1
            
        QtCore.QMetaObject.connectSlotsByName(VisualizzaWindow)

    #Questa funzione aggiunge un label al GridLayout nella posizione x(colonna) e y(riga)
    def AddElement(self,gridLayout,text,x,y):
        gridLayout
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(label_2.sizePolicy().hasHeightForWidth())
        label_2.setSizePolicy(sizePolicy)
        label_2.setMinimumSize(QtCore.QSize(0, 20))
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
        self.label_headTelefono.setText(str(text))
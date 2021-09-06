# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from Magazzino.View.InserimentoMagazzino import Ui_InserisciMagazzino
from Magazzino.Controller.MagazzinoC import MagazzinoC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QSizePolicy, QWidget


class Ui_ListaMagazzino(QWidget):
    def __init__(self, parent=None,fakeparent=None):
        super(Ui_ListaMagazzino, self).__init__(parent)
        self.fakeparent=fakeparent
        self._translate = QtCore.QCoreApplication.translate
        ListaMagazzino = self
        self.controller = MagazzinoC()
        self.chiamata = self.controller.GetAll()
        self.handClose = 1
        ListaMagazzino.setObjectName("ListaMagazzino")
        ListaMagazzino.resize(800, 600)
        ListaMagazzino.setWindowTitle(self._translate("ListaMagazzino", "ListaMagazzino"))
        self.verticalLayout = QtWidgets.QVBoxLayout(ListaMagazzino)
        self.verticalLayout.setObjectName("verticalLayout")

        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.AddLabelTitolo("Lista del magazzino")
        self.AddScrollArea()

        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(180, 50))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText(self._translate("ListaMagazzino", "inserisci un nuovo elemento"))
        self.pushButton.clicked.connect(self.GoInserimentoMagazzino)
        
        self.traduzione = {
        'tipo_scorta':"Articoli",
        }

        self.listAttr = ['tipo_scorta']
        #le dimensioni delle colonne
        sizes = [300]
        for attr in range(len(self.listAttr)):
            
            #Aggiunge l'intestazione della tabella
            self.AddTableHeader(self.traduzione[self.listAttr[attr]],attr,sizes[attr])

            #aggiunge elemento nella tabella
            for a in range(0,len(self.chiamata)):
                self.AddTableContent(attr,a+1,self.chiamata[a][self.listAttr[attr]],sizes[attr])

        #Aggiunge pulsante delle operazioni
        self.OperationButtons=[
            {
                "name":"Cancella Elemento",
                "StyleSheet":"background-color: rgb(255, 0, 0);\n color: rgb(255, 255, 255);",
                "function":self.deleteConfirm
            },
        ]

        X_offset = len(self.listAttr)
        for i in range(0,len(self.OperationButtons)):
            for a in range(0,len(self.chiamata)):
                #print(i)
                self.OperationButtons[i]
                self.AddOperationButton(X_offset+i,a,self.OperationButtons[i],lambda state,b=a,c=i: self.OperationButtons[c]["function"](self.chiamata[b]))                       

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        QtCore.QMetaObject.connectSlotsByName(ListaMagazzino)
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

    #chiamata alla funzione per la cancellazione di un elemento
    def deleteConfirm(self,articolo):

        msg = QMessageBox()
        msg.setWindowTitle('Conferma')
        msg.setText('sei sicuro di voler cancellare l\' articolo '+articolo['tipo_scorta'] + '?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        okButton = msg.button(QMessageBox.Yes)
        noButton = msg.button(QMessageBox.No)
        okButton.setText('si')
        retval = msg.exec_()
        if(msg.clickedButton() == okButton):
            print('cancellazione confermata')
            postbody = {'tipo_scorta':articolo['tipo_scorta']}
            res = self.controller.Delete(postbody)
            print(res)
            self.RefreshLista = Ui_ListaMagazzino()
            self.RefreshLista.show()
            self.handClose = 0
            self.close()
        else:
            print('cancellazione annullata')   

    #Viene settata l'intestazione della finestra
    def AddTableHeader(self,text,pos,width):
        self.header1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sizePolicy.setHeightForWidth(self.header1.sizePolicy().hasHeightForWidth())
        self.header1.setSizePolicy(self.sizePolicy)
        self.header1.setMinimumSize(QtCore.QSize(width, 30))
        self.header1.setObjectName("header1")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.header1.setFont(font)
        self.header1.setText(self._translate("ListaMagazzino",text))
        self.gridLayout.addWidget(self.header1, 0, pos, 1, 1)
    
    #Questa funzione aggiunge le label alla finestra
    def AddTableContent(self,x,y,content,width):
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(self.sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(width, 30))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_3.setText(self._translate("ListaMagazzino","   "+ content))
        self.gridLayout.addWidget(self.label_3, y, x, 1, 1)

    #Questa funzione aggiunge un bottone a cui viene collegata una particolare funzione, da attivare quando 
    # il bottone viene premuto
    def AddOperationButton(self,x,y,buttonDict,function):
        OperationButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        OperationButton.setStyleSheet(buttonDict["StyleSheet"])
        OperationButton.setObjectName("OperationButton")
        OperationButton.setMinimumSize(QtCore.QSize(100, 25))
        OperationButton.setText(self._translate("ListaMagazzino", buttonDict["name"]))        
        OperationButton.clicked.connect(function)
        self.gridLayout.addWidget(OperationButton, y+1, x, 1, 1)
        return OperationButton
    
    #Questa funzione aggiunge una scroll area
    def AddScrollArea(self):
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setStyleSheet("background-color: rgb(109, 109, 109);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 524))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

    # In questa funzione viene impostata la label che si trova sopra la lista
    def AddLabelTitolo(self,text):
        self.label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.label.setText(self._translate("ListaMagazzino", text))

    def GoInserimentoMagazzino(self):
        self.InserimentoMagazzino = Ui_InserisciMagazzino(fakeparent = self)
        self.InserimentoMagazzino.show()
        self.handClose = 0
        self.close()
    
    def closeEvent(self, event):
        if(self.handClose ==0):
            self.handClose = 1
        else:
            self.fakeparent.show()
        event.accept()
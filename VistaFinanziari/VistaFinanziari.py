# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaAnagrafica.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from Stipendio.View.StipendioV import Ui_ListaStipendio
from UscitaEffettuata.View.VistaInserisciUscita import Ui_InserisciUscita
from UscitaEffettuata.View.UscitaEffettuataV import Ui_ListaUscita
from Entrata.View.InserisciEntrata import Ui_InserisciEntrata
from Entrata.View.EntrataV import Ui_ListaEntrata
from AltraSpesa.View.InserisciAltraSpesa import Ui_InserisciAltraSpesa
from AltraSpesa.View.AltraSpesaV import Ui_listaAltraSpesa
from Contabile.View.ContabileV import Ui_listaContabile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget

from Dipendente.View.VistaListaDipendenti import Ui_ListaDipendenti
from ListinoPrezzi.View.VistaListaListinoPrezzi import Ui_ListaListinoPrezzi
from Cliente.View.VistaListaCliente import Ui_ListaCliente
from Dipendente.View.VistaInserisciDipendente import Ui_InserisciDip


class VistaFinanziari(QWidget):
    def __init__(self, parent=None,fakeparent=None):
        super(VistaFinanziari, self).__init__(parent)
        self.fakeparent = fakeparent
        self._translate = QtCore.QCoreApplication.translate
        HomeClass = self
        HomeClass.setObjectName("VistaFinanziari")
        HomeClass.resize(756, 585)
        self.verticalLayout = QtWidgets.QVBoxLayout(HomeClass)
        self.verticalLayout.setObjectName("verticalLayout")

        self.AddScrollArea()

        self.AddLabelTitolo("Vista Finanziari")

        self.AddSectionLabel(1,"Contabili")
        self.horizontalLayout = self.AddHorizontalLayout(0,2)
        self.AddButtonInLayout(self.horizontalLayout,"Lista contabile",self.Go_ListaContabile)     
        #self.AddButtonInLayout(self.horizontalLayout,"Inserisci un contabile",self.Go_NewDipendente)   

        self.AddSectionLabel(3,"Altra Spesa")
        self.horizontalLayout_2 = self.AddHorizontalLayout(0,4)
        self.AddButtonInLayout(self.horizontalLayout_2,"Lista spese",self.Go_ListaSpese)     
        self.AddButtonInLayout(self.horizontalLayout_2,"Inserisci una spesa",self.Go_NewSpese)     

        self.AddSectionLabel(5,"Entrata")
        self.horizontalLayout_3 = self.AddHorizontalLayout(0,6)
        self.AddButtonInLayout(self.horizontalLayout_3,"Lista entrate",self.Go_ListaEntrate)     
        self.AddButtonInLayout(self.horizontalLayout_3,"Inserisci un entrata",self.Go_NewEntrata)     

        self.AddSectionLabel(7,"Uscita Effettuata")
        self.horizontalLayout_3 = self.AddHorizontalLayout(0,8)
        self.AddButtonInLayout(self.horizontalLayout_3,"Lista uscite effettuate",self.Go_ListaUsciteEffettuate)     
        self.AddButtonInLayout(self.horizontalLayout_3,"Inserisci un uscita effettuata",self.Go_NewUscitaEffettuata)   

        self.AddSectionLabel(9,"Stipendio")
        self.horizontalLayout_3 = self.AddHorizontalLayout(0,10)
        self.AddButtonInLayout(self.horizontalLayout_3,"Lista stipendio",self.Go_ListaStipendio)     
        self.AddButtonInLayout(self.horizontalLayout_3,"Inserisci un stipendio",self.Go_NewStipendio) 

        self.AddSectionLabel(11,"Retribuzione variabile")
        self.horizontalLayout_3 = self.AddHorizontalLayout(0,12)
        self.AddButtonInLayout(self.horizontalLayout_3,"Lista retribuzione",self.Go_ListaRetribuzioni)     
        self.AddButtonInLayout(self.horizontalLayout_3,"Inserisci un retribuzione",self.Go_NewRetribuzione) 

        self.AddSectionLabel(13,"Flussi di cassa")
        self.horizontalLayout_3 = self.AddHorizontalLayout(0,14)
        self.AddButtonInLayout(self.horizontalLayout_3,"Lista dei Flussi",self.Go_ListaFlussi)     

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        QtCore.QMetaObject.connectSlotsByName(HomeClass)

        
    def AddScrollArea(self):
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setMinimumSize(QtCore.QSize(400, 200))
        self.scrollArea.setStyleSheet("background-color: rgb(109, 109, 109);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 732, 561))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

    def AddButtonInLayout(self,layout,text,function):
        Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        Button.setMinimumSize(QtCore.QSize(300, 50))
        Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        Button.setFont(font)
        Button.setObjectName("ListaPrezzo")
        Button.setText(self._translate("HomeClass", text))
        Button.clicked.connect(function)
        Button.setStyleSheet("background-color: rgb(85, 255, 255);")
        layout.addWidget(Button)
        return Button

    def AddSectionLabel(self,y,text):
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, y, 0, 1, 1)
        self.label_3.setText(self._translate("HomeClass", text))

    def AddHorizontalLayout(self,x,y):
        Layout = QtWidgets.QHBoxLayout()
        Layout.setContentsMargins(20, -1, 20, -1)
        Layout.setSpacing(20)
        Layout.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(Layout, y, x, 1, 1)
        return Layout
        
    def AddLabelTitolo(self,text):
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n""color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label.setText(self._translate("HomeClass", text))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

    def closeEvent(self, event):
        self.fakeparent.show()
        event.accept()

    def Go_NewRetribuzione(self):
        print("Go_NewRetribuzione")

    def Go_ListaRetribuzioni(self):
        print("Go_ListaRetribuzioni")

    def Go_NewStipendio(self):
        print("Go_NewStipendio")

    def Go_ListaStipendio(self):
        print("Go_ListaStipendio")
        self.ListaStipendi = Ui_ListaStipendio()
        self.ListaStipendi.show()
        

    def Go_NewUscitaEffettuata(self):
        print("Go_NewUscitaEffettuata")
        self.InserisciUscita = Ui_InserisciUscita()
        self.InserisciUscita.show()

    def Go_ListaUsciteEffettuate(self):
        self.ListaUscita = Ui_ListaUscita()
        self.ListaUscita.show()

    def Go_ListaContabile(self):
        print('Go listaContabile')
        self.ListaContabile = Ui_listaContabile()
        self.ListaContabile.show()
    
    def Go_ListaEntrate(self):
        print("Go_ListaEntrate")
        self.ListaEntrata = Ui_ListaEntrata()
        self.ListaEntrata.show()

    def Go_NewSpese(self):
        self.InserisciAltraSpesa = Ui_InserisciAltraSpesa()
        self.InserisciAltraSpesa.show()


    def Go_ListaSpese(self):
        print('Go_ListaSpese')
        self.ListaAltraSpesa = Ui_listaAltraSpesa()
        self.ListaAltraSpesa.show()

    def Go_NewEntrata(self):
        self.EntrataIns = Ui_InserisciEntrata()
        self.EntrataIns.show()

    def Go_ListaFlussi(self):
        print('Go Lista Flussi')
    
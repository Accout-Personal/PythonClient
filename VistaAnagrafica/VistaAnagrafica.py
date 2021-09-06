# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaAnagrafica.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget

from Dipendente.View.VistaListaDipendenti import Ui_ListaDipendenti
from Dipendente.View.VistaInserisciDipendente import Ui_InserisciDip

from ListinoPrezzi.View.VistaListaListinoPrezzi import Ui_ListaListinoPrezzi
from ListinoPrezzi.View.VistaInserisciListinoPrezzi import Ui_InserisciListinoPrezzi

from Cliente.View.VistaInserisciCliente import Ui_InserisciCliente
from Cliente.View.VistaListaCliente import Ui_ListaCliente

class VistaAnagrafica(QWidget):
    def __init__(self, parent=None):
        super(VistaAnagrafica, self).__init__(parent)
        self._translate = QtCore.QCoreApplication.translate
        HomeClass = self
        HomeClass.setObjectName("VistaAnagrafica")
        HomeClass.resize(756, 585)
        self.verticalLayout = QtWidgets.QVBoxLayout(HomeClass)
        self.verticalLayout.setObjectName("verticalLayout")

        self.AddScrollArea()

        self.AddLabelTitolo("Vista Anagrafica")

        self.AddSectionLabel(1,"Dipendenti")
        self.horizontalLayout = self.AddHorizontalLayout(0,2)
        self.AddButtonInLayout(self.horizontalLayout,"Lista dipendenti",self.Go_ListaDipendenti)     
        self.AddButtonInLayout(self.horizontalLayout,"Inserisci un dipendente",self.Go_NewDipendente)   

        self.AddSectionLabel(3,"Clienti")
        self.horizontalLayout_2 = self.AddHorizontalLayout(0,4)
        self.AddButtonInLayout(self.horizontalLayout_2,"Lista clienti",self.Go_ListaClienti)     
        self.AddButtonInLayout(self.horizontalLayout_2,"Inserisci un cliente",self.Go_NewCliente)     

        self.AddSectionLabel(5,"Listino Prezzi")
        self.horizontalLayout_3 = self.AddHorizontalLayout(0,6)
        self.AddButtonInLayout(self.horizontalLayout_3,"Lista modelli",self.Go_ListinoPrezzi)     
        self.AddButtonInLayout(self.horizontalLayout_3,"Inserisci un modello",self.Go_NewPrezzo)     

        self.AddSectionLabel(7,"Macchine Pubbliche")
        self.horizontalLayout_3 = self.AddHorizontalLayout(0,8)
        self.AddButtonInLayout(self.horizontalLayout_3,"Lista macchinari",self.Go_ListaMacchinari)     
        self.AddButtonInLayout(self.horizontalLayout_3,"Inserisci un macchinario",self.Go_NewMacchinario)   

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

    def Go_ListaDipendenti(self):
        self.ListaDipendeti = Ui_ListaDipendenti()
        self.ListaDipendeti.show()
    
    def Go_NewDipendente(self):
        self.InserisciDipendente = Ui_InserisciDip()
        self.InserisciDipendente.show()

    def Go_ListinoPrezzi(self):
        self.ListinoPrezzi = Ui_ListaListinoPrezzi()
        self.ListinoPrezzi.show()

    def Go_NewPrezzo(self):
        self.NewModello = Ui_InserisciListinoPrezzi()
        self.NewModello.show()

    def Go_NewCliente(self):
        self.NewClienti = Ui_InserisciCliente()
        self.NewClienti.show()

    def Go_ListaClienti(self):
        self.ListaClienti = Ui_ListaCliente()
        self.ListaClienti.show()
    
    def Go_NewMacchinario(self):
        print('Go new macchinario')
    
    def Go_ListaMacchinari(self):
        print('Go lista macchinari')
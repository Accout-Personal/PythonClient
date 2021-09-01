# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from Dipendente.View.VistaModificaDip import Ui_ModificaDipAng
from Dipendente.View.VistaDipendente import Ui_VisualizzaAnagDip
from Dipendente.Controller.DipendenteC import DipendenteC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget


class Ui_ListaDipendenti(QWidget):
    def __init__(self, parent=None):
        super(Ui_ListaDipendenti, self).__init__(parent)
        ListaDipendenti = self
        self.pushButton_1 = []
        self.pushButton_2 = []
        self.pushButton_3 = []
        self.controller = DipendenteC()
        self.chiamata = self.controller.GetAll()
        ListaDipendenti.setObjectName("ListaDipendenti")
        ListaDipendenti.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(ListaDipendenti)
        self.verticalLayout.setObjectName("verticalLayout")
        self._translate = QtCore.QCoreApplication.translate

        self.AddLabelTitolo("Lista dei Dipendenti")

        self.gridLayout,self.scrollAreaWidgetContents = self.AddScrollArea(200)

       
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        
        self.header1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(self.header1.sizePolicy().hasHeightForWidth())
        self.header1.setSizePolicy(sizePolicy)
        self.header1.setMinimumSize(QtCore.QSize(250, 30))
        self.header1.setObjectName("header1")
        self.header1.setText(self._translate("ListaDipendenti","Nome e Cognome"))
        self.gridLayout.addWidget(self.header1, 0, 0, 1, 1)
        
        self.header2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(self.header2.sizePolicy().hasHeightForWidth())
        self.header2.setSizePolicy(sizePolicy)
        self.header2.setMinimumSize(QtCore.QSize(150, 30))
        self.header2.setObjectName("header2")
        self.header2.setText(self._translate("ListaDipendenti","Tipo Dipendente"))
        self.gridLayout.addWidget(self.header2, 0, 1, 1, 1)

        
        for a in range(0,len(self.chiamata)):
            self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
            self.label_3.setSizePolicy(sizePolicy)
            self.label_3.setMinimumSize(QtCore.QSize(250, 30))
            self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_3.setObjectName("label_3")
            self.label_3.setText(self._translate("ListaDipendenti","   "+ self.chiamata[a]['nome_cognome']))
            self.gridLayout.addWidget(self.label_3, a+1, 0, 1, 1)

            self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
            self.label_4.setSizePolicy(sizePolicy)
            self.label_4.setMinimumSize(QtCore.QSize(150, 30))
            self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_4.setObjectName("label_4")
            self.label_4.setText(self._translate("ListaDipendenti"," "+self.chiamata[a]['tipo_dipendente']))
            self.gridLayout.addWidget(self.label_4, a+1, 1, 1, 1)

            self.pushButton_1.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
            self.pushButton_1[a].setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                                "color: rgb(255, 255, 255);")
            self.pushButton_1[a].setObjectName("pushButton"+str(a))
            self.gridLayout.addWidget(self.pushButton_1[a], a+1, 3, 1, 1)
            self.pushButton_1[a].setText(self._translate("ListaDipendenti", "Cancella Elemento"))
            self.pushButton_1[a].clicked.connect(lambda state,b=a: self.deleteConfirm(self.chiamata[b]['CF']))

            self.pushButton_2.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
            self.pushButton_2[a].setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                                "color: rgb(255, 255, 255);")
            self.pushButton_2[a].setObjectName("pushButton"+str(a))
            self.gridLayout.addWidget(self.pushButton_2[a], a+1, 4, 1, 1)
            self.pushButton_2[a].setText(self._translate("UIwindow", "Modifica Elemento"))
            self.pushButton_2[a].clicked.connect(lambda state,b=a: self.ModificaDip(self.chiamata[b]['CF']))

            self.pushButton_3.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
            self.pushButton_3[a].setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                                "color: rgb(255, 255, 255);")
            self.pushButton_3[a].setObjectName("pushButton"+str(a))
            self.gridLayout.addWidget(self.pushButton_3[a], a+1, 2, 1, 1)
            self.pushButton_3[a].setText(self._translate("UIwindow", "Visualizza Elemento"))
            self.pushButton_3[a].clicked.connect(lambda state,b=a: self.Visualizza(self.chiamata[b]['CF']))

            self.label_3.setText(self._translate("ListaDipendenti","   "+ self.chiamata[a]['nome_cognome']))
            self.label_4.setText(self._translate("ListaDipendenti","  Tipo: "+self.chiamata[a]['tipo_dipendente']))
            
            
            
        self.retranslateUi(ListaDipendenti)
        QtCore.QMetaObject.connectSlotsByName(ListaDipendenti)

    def retranslateUi(self, ListaDipendenti):
        _translate = QtCore.QCoreApplication.translate
        ListaDipendenti.setWindowTitle(_translate("ListaDipendenti", "ListaDipendenti"))
        

    def Visualizza(self,cf):
        print(str(cf))
        self.Dettaglio = Ui_VisualizzaAnagDip(cf)
        self.Dettaglio.show()

    def ModificaDip(self,cf):
        print(str(cf))
        self.Dettaglio = Ui_ModificaDipAng(cf)
        self.Dettaglio.show()
        self.close()

    def deleteConfirm(self,dipendente):

        msg = QMessageBox()
        msg.setWindowTitle('Conferma')
        msg.setText('sei sicuro di voler cancellare dipendente '+dipendente['nome_cognome'] + '?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        okButton = msg.button(QMessageBox.Yes)
        noButton = msg.button(QMessageBox.No)
        okButton.setText('si')
        retval = msg.exec_()
        if(msg.clickedButton() == okButton):
            print('cancellazione confermata')
            postbody = {'CF':dipendente['CF']}
            res = self.controller.Delete(postbody)
            print(res)
            self.RefreshLista = Ui_ListaDipendenti()
            self.RefreshLista.show()
            self.close()
        else:
            print('cancellazione annullata')

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
        self.label.setText(self._translate("ModificaDipAng", text))
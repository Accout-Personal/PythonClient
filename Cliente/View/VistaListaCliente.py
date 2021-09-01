# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from Cliente.Controller.ClienteC import ClienteC
from Cliente.View.VistaCliente import Ui_Cliente
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget


class Ui_ListaCliente(QWidget):
    def __init__(self, parent=None):
        super(Ui_ListaCliente, self).__init__(parent)
        ListaCliente = self
        self.controller = ClienteC()
        self.chiamata = self.controller.GetAll()
        ListaCliente.setObjectName("ListaCliente")
        ListaCliente.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(ListaCliente)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ListaCliente)
        self.label.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea = QtWidgets.QScrollArea(ListaCliente)
        self.scrollArea.setStyleSheet("background-color: rgb(109, 109, 109);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 524))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        _translate = QtCore.QCoreApplication.translate
        
        self.header1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(self.header1.sizePolicy().hasHeightForWidth())
        self.header1.setSizePolicy(sizePolicy)
        self.header1.setMinimumSize(QtCore.QSize(250, 30))
        self.header1.setObjectName("header1")
        self.header1.setText(_translate("ListaCliente","Nome Azienda"))
        self.gridLayout.addWidget(self.header1, 0, 0, 1, 1)

        self.header2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(self.header2.sizePolicy().hasHeightForWidth())
        self.header2.setSizePolicy(sizePolicy)
        self.header2.setMinimumSize(QtCore.QSize(150, 30))
        self.header2.setObjectName("header2")
        self.header2.setText(_translate("ListaCliente","Citta'"))
        self.gridLayout.addWidget(self.header2, 0, 1, 1, 1)

        
        for a in range(0,len(self.chiamata)):
            self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
            self.label_3.setSizePolicy(sizePolicy)
            self.label_3.setMinimumSize(QtCore.QSize(250, 30))
            self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_3.setObjectName("label_3")
            self.label_3.setText(_translate("ListaCliente","   "+ self.chiamata[a]['nome_azienda']))
            self.gridLayout.addWidget(self.label_3, a+1, 0, 1, 1)

            self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
            self.label_4.setSizePolicy(sizePolicy)
            self.label_4.setMinimumSize(QtCore.QSize(150, 30))
            self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_4.setObjectName("label_4")
            self.label_4.setText(_translate("ListaCliente"," "+self.chiamata[a]['citta']))
            self.gridLayout.addWidget(self.label_4, a+1, 1, 1, 1)

            self.DeleteButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.DeleteButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                                "color: rgb(255, 255, 255);")
            self.DeleteButton.setObjectName("DeleteButton")
            self.DeleteButton.setText(_translate("ListaCliente", "Cancella Elemento"))
            self.DeleteButton.clicked.connect(lambda state,b=a: self.deleteConfirm(self.chiamata[b]))
            self.gridLayout.addWidget(self.DeleteButton, a+1, 3, 1, 1)

            self.ModifyButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.ModifyButton.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                            "color: rgb(255, 255, 255);")
            self.ModifyButton.setObjectName("ModifyButton")
            self.ModifyButton.setText(_translate("ListaCliente", "Modifica Elemento"))
            self.gridLayout.addWidget(self.ModifyButton, a+1, 4, 1, 1)

            self.viewButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.viewButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                            "color: rgb(255, 255, 255);")
            self.viewButton.setObjectName("viewButton")
            self.viewButton.setText(_translate("ListaCliente", "Visualizza Elemento"))
            self.viewButton.clicked.connect(lambda state,b=a: self.Visualizza(self.chiamata[b]))
            self.gridLayout.addWidget(self.viewButton, a+1, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
            
        self.retranslateUi(ListaCliente)
        QtCore.QMetaObject.connectSlotsByName(ListaCliente)

    def retranslateUi(self, ListaCliente):
        _translate = QtCore.QCoreApplication.translate
        ListaCliente.setWindowTitle(_translate("ListaCliente", "ListaCliente"))
        self.label.setText(_translate("ListaCliente", "Lista dei Cliente"))

    def deleteConfirm(self,cliente):

        msg = QMessageBox()
        msg.setWindowTitle('Conferma')
        msg.setText('sei sicuro di voler cancellare il Cliente '+cliente['nome_azienda'] + '?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        okButton = msg.button(QMessageBox.Yes)
        noButton = msg.button(QMessageBox.No)
        okButton.setText('si')
        retval = msg.exec_()
        if(msg.clickedButton() == okButton):
            print('cancellazione confermata')
            postbody = {'PIVA':cliente['PIVA']}
            res = self.controller.Delete(postbody)
            print(res)
            self.RefreshLista = Ui_ListaCliente()
            self.RefreshLista.show()
            self.close()
        else:
            print('cancellazione annullata')   

    def Visualizza(self,elem):
        print(elem)
        self.Dettaglio = Ui_Cliente(str(elem['PIVA']))
        self.Dettaglio.show()
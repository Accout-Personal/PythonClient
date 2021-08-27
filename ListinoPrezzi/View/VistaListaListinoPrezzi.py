# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from ListinoPrezzi.Controller.ListinoPrezziC import ListinoPrezziC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget


class Ui_ListaListinoPrezzi(QWidget):
    def __init__(self, parent=None):
        super(Ui_ListaListinoPrezzi, self).__init__(parent)
        ListaListinoPrezzi = self
        self.controller = ListinoPrezziC()
        self.ListaElementi = self.controller.GetAll()
        ListaListinoPrezzi.setObjectName("ListaListinoPrezzi")
        ListaListinoPrezzi.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(ListaListinoPrezzi)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ListaListinoPrezzi)
        self.label.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea = QtWidgets.QScrollArea(ListaListinoPrezzi)
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

        self.label_head1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(self.label_head1.sizePolicy().hasHeightForWidth())
        self.label_head1.setSizePolicy(sizePolicy)
        self.label_head1.setMinimumSize(QtCore.QSize(150, 30))
        self.label_head1.setObjectName("label_head1")
        self.label_head1.setText(_translate("ListaListinoPrezzi","Modello"))
        self.gridLayout.addWidget(self.label_head1, 0, 1, 1, 1)

        self.label_head1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(self.label_head1.sizePolicy().hasHeightForWidth())
        self.label_head1.setSizePolicy(sizePolicy)
        self.label_head1.setMinimumSize(QtCore.QSize(100, 30))
        self.label_head1.setObjectName("label_head1")
        self.label_head1.setText(_translate("ListaListinoPrezzi","Valore Cliente"))
        self.gridLayout.addWidget(self.label_head1, 0, 2, 1, 1)

        self.label_head1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(self.label_head1.sizePolicy().hasHeightForWidth())
        self.label_head1.setSizePolicy(sizePolicy)
        self.label_head1.setMinimumSize(QtCore.QSize(100, 30))
        self.label_head1.setObjectName("label_head1")
        self.label_head1.setText(_translate("ListaListinoPrezzi","Valore Dipendente"))
        self.gridLayout.addWidget(self.label_head1, 0, 3, 1, 1)


        
        for a in range(0,len(self.ListaElementi)):

            self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
            self.label_3.setSizePolicy(sizePolicy)
            self.label_3.setMinimumSize(QtCore.QSize(150, 30))
            self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_3.setObjectName("label_3")
            self.label_3.setText(_translate("ListaListinoPrezzi","   "+ self.ListaElementi[a]['modello']))
            self.gridLayout.addWidget(self.label_3, a+1, 1, 1, 1)

            self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
            self.label_4.setSizePolicy(sizePolicy)
            self.label_4.setMinimumSize(QtCore.QSize(100, 30))
            self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_4.setObjectName("label_4")
            self.label_4.setText(_translate("ListaListinoPrezzi"," "+self.ListaElementi[a]['valore_cliente']+"€"))
            self.gridLayout.addWidget(self.label_4, a+1, 2, 1, 1)

            self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
            self.label_5.setSizePolicy(sizePolicy)
            self.label_5.setMinimumSize(QtCore.QSize(100, 30))
            self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_5.setObjectName("label_5")
            self.label_5.setText(_translate("ListaListinoPrezzi"," "+self.ListaElementi[a]['valore_dipendente']+"€"))
            self.gridLayout.addWidget(self.label_5, a+1, 3, 1, 1)

            self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                                "color: rgb(255, 255, 255);")
            self.pushButton.setObjectName("pushButton")
            self.gridLayout.addWidget(self.pushButton, a+1, 4, 1, 1)

            self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                            "color: rgb(255, 255, 255);")
            self.pushButton_2.setObjectName("pushButton_2")
            self.gridLayout.addWidget(self.pushButton_2, a+1, 5, 1, 1)

            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.verticalLayout.addWidget(self.scrollArea)
            
            
            self.pushButton.setText(_translate("ListaListinoPrezzi", "Cancella Elemento"))
            self.pushButton_2.setText(_translate("ListaListinoPrezzi", "Modifica Elemento"))


        self.retranslateUi(ListaListinoPrezzi)
        QtCore.QMetaObject.connectSlotsByName(ListaListinoPrezzi)

    def retranslateUi(self, ListaListinoPrezzi):
        _translate = QtCore.QCoreApplication.translate
        ListaListinoPrezzi.setWindowTitle(_translate("ListaListinoPrezzi", "ListaListinoPrezzi"))
        self.label.setText(_translate("ListaListinoPrezzi", "Lista dei ListinoPrezzi"))
        

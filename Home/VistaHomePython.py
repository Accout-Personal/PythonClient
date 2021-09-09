# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from VistaStrategiche.VistaStrategiche import Ui_VistaStrategiche
from Dipendente.View.VistaListaDipendenti import Ui_ListaDipendenti

from VistaAnagrafica.VistaAnagrafica import VistaAnagrafica
from VistaLavorazione.VistaLavorazione import VistaLavorazione
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget


class Ui_HomeClass(QWidget):
    def __init__(self, parent=None):
        super(Ui_HomeClass, self).__init__(parent)
        _translate = QtCore.QCoreApplication.translate
        HomeClass = self
        HomeClass.setObjectName("HomeClass")
        HomeClass.resize(800, 600)
        self.handClose = 1
        self.verticalLayout = QtWidgets.QVBoxLayout(HomeClass)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(HomeClass)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setStyleSheet("background-color: rgb(109, 109, 109);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 580))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText(_translate("HomeClass", "Vista Anagrafiche"))
        self.pushButton.clicked.connect(self.GoVistaAnagrafiche)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        QtCore.QMetaObject.connectSlotsByName(HomeClass)    
        HomeClass.setWindowTitle(_translate("HomeClass", "HomeClass"))
        self.label.setText(_translate("HomeClass", "Welcome Home"))
        
        self.pushButton_2.setText(_translate("HomeClass", "Vista Lavorazione"))
        self.pushButton_2.clicked.connect(self.GoVistaLavorazione)
        self.pushButton_3.setText(_translate("HomeClass", "Vista Strategiche"))
        self.pushButton_3.clicked.connect(self.GoVistaStrategiche)

    def GoVistaAnagrafiche(self):
        self.Anagrafica = VistaAnagrafica(fakeparent=self)
        self.Anagrafica.show()
        self.handClose = 0
        self.close()
        

    def GoVistaStrategiche(self):
        self.Anagrafica = Ui_VistaStrategiche(fakeparent=self)
        self.Anagrafica.show()
        self.handClose = 0
        self.close()
    
    def GoVistaLavorazione(self):
        self.Lavorazione = VistaLavorazione(fakeparent=self)
        self.Lavorazione.show()
        self.handClose = 0
        self.close()


    def closeEvent(self, event):
        print(self.handClose)
        if(self.handClose == 1):
            msg = QMessageBox()
            msg.setWindowTitle('Conferma')
            msg.setText('sei sicuro di voler uscire ?')
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            okButton = msg.button(QMessageBox.Yes)
            noButton = msg.button(QMessageBox.No)
            okButton.setText('si')
            retval = msg.exec_()
            if(msg.clickedButton() == okButton):
                print('chiusura accettata')
                if not type(event) == bool:
                    event.accept()            
            else:
                if not type(event) == bool:
                    event.ignore()
        else:
            self.handClose = 1
            event.accept()
            

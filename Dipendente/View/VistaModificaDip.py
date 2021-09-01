# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from Dipendente.Controller.DipendenteC import DipendenteC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
import copy

class Ui_ModificaDipAng(QWidget):
    def __init__(self,CF, parent=None):
        super(Ui_ModificaDipAng, self).__init__(parent)
        self._translate = QtCore.QCoreApplication.translate
        self.cf = CF
        self.controller = DipendenteC()
        self.chiamata = self.controller.GetKey(self.cf)
        ModificaDipAng = self
        ModificaDipAng.setObjectName("ModificaDipAng")
        ModificaDipAng.resize(800, 600)
        ModificaDipAng.setWindowTitle(self._translate("ModificaDipAng", "ModificaDipAng"))
        self.verticalLayout = QtWidgets.QVBoxLayout(ModificaDipAng)
        self.verticalLayout.setObjectName("verticalLayout")

        #Aggiunge il "titolo" della finestra
        self.AddLabelTitolo("Modifica Dipendente")

        #Aggiunge un scroll area per i campi
        self.scrollArea,self.scrollAreaWidgetContents,self.verticalLayout_2 = self.AddScrollArea()
        self.AddInsertHint("I campi con il segno ( * ) sono obbligatori")
        

        self.traduzione = {'CF':'codice fiscale',
        'nome_cognome':'nome e cognome',
        'tipo_dipendente':'tipo mansione',
        'importo_orario_feriale':'importo orario feriale',
        'importo_orario_regolare':'importo orario regolare',
        'importo_orario_straordinario':'importo orario straordinario',
        'IBAN':'IBAN',
        'username':'username',
        'data_di_nascita':'data di nascita'}

        #si usa un dizionario per iterare tutti i campi dell'inserimento e popolazione del campo
        self.body = {
        'CF': self.chiamata['CF'],
        'nome_cognome':self.chiamata['nome_cognome'],
        'tipo_dipendente':'',
        'importo_orario_feriale':'',
        'importo_orario_regolare':'',
        'importo_orario_straordinario':'',
        'IBAN':'',
        'username':'',
        'data_di_nascita': self.chiamata['data_di_nascita']
        }

        #esclude elemento non desiderato per visualizzazione
        self.viewList = copy.deepcopy(self.chiamata)
        self.exclude = ['CF','nome_cognome','data_di_nascita','remember_token']
        for elem in self.exclude:
            self.viewList.pop(elem)
        
        #settare size policy per tutti elementi
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listaInput = {}
        for a in self.viewList:
            
            #Crea il label del campo
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
            self.label_3.setSizePolicy(sizePolicy)
            self.label_3.setMinimumSize(QtCore.QSize(300, 0))
            self.label_3.setMaximumSize(QtCore.QSize(325, 28))
            self.label_3.setFont(font)
            self.label_3.setText("")
            self.label_3.setObjectName("label_3")
            self.label_3.setText(self._translate("ModificaDipAng", "  "+str(self.traduzione[a])))
            self.horizontalLayout.addWidget(self.label_3)

            #Crea il campo per la modifica
            self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
            self.textEdit_2.setSizePolicy(sizePolicy)
            self.textEdit_2.setMinimumSize(QtCore.QSize(300, 0))
            self.textEdit_2.setMaximumSize(QtCore.QSize(500, 30))
            self.textEdit_2.setFont(font)
            self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.textEdit_2.setObjectName("textEdit")
            self.horizontalLayout.addWidget(self.textEdit_2)
            self.verticalLayout_2.addLayout(self.horizontalLayout)
            self._translate = QtCore.QCoreApplication.translate
            self.textEdit_2.setText(self._translate("ModificaDipAng", "  "+str(self.chiamata[a])))
            self.listaInput[a]=self.textEdit_2
            
        #Aggiunge il pulsante per la modifica
        self.pushButton = self.AddSubmitButton("Modifica")
        self.pushButton.clicked.connect(self.Modify)

    def Modify(self):
        for a in self.listaInput:
            self.body[a] = self.listaInput[a].toPlainText().replace('  ', '')
        self.risultato = self.controller.Update(self.body)
        print(str(self.risultato))

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
    
    def AddScrollArea(self):
        scrollArea = QtWidgets.QScrollArea(self)
        scrollArea.setStyleSheet("background-color: rgb(109, 109, 109);")
        scrollArea.setWidgetResizable(True)
        scrollArea.setObjectName("scrollArea")
        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 152))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        verticalLayout_2 = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
        verticalLayout_2.setObjectName("verticalLayout_2")
        scrollArea.setWidget(scrollAreaWidgetContents)
        self.verticalLayout.addWidget(scrollArea)
        return scrollArea,scrollAreaWidgetContents,verticalLayout_2
    
    def AddInsertHint(self,text): 
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(300, 50))
        self.label_2.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_2.setText(self._translate("ModificaDipAng", text))
    
    def AddSubmitButton(self,text):
        pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
        pushButton.setSizePolicy(sizePolicy)
        pushButton.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        pushButton.setFont(font)
        pushButton.setStyleSheet("background-color: rgb(85, 255, 255);\n color: rgb(247, 247, 247);")
        pushButton.setObjectName("pushButton")
        pushButton.setText(self._translate("ModificaDipAng", text))
        self.verticalLayout_2.addWidget(pushButton, 0, QtCore.Qt.AlignHCenter)
        return pushButton
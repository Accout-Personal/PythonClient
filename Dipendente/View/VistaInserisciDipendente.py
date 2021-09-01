from Dipendente.Controller.DipendenteC import DipendenteC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
import copy

class Ui_InserisciDip(QWidget):
    def __init__(self,CF, parent=None):
        super(Ui_InserisciDip, self).__init__(parent)
        self.cf = CF
        self.controller = DipendenteC()
        InsDipendente = self
        InsDipendente.setObjectName("InsDipendente")
        InsDipendente.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(InsDipendente)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(InsDipendente)
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
        self.scrollArea = QtWidgets.QScrollArea(InsDipendente)
        self.scrollArea.setStyleSheet("background-color: rgb(109, 109, 109);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 152))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listaInput = {}

        self.traduzione = {'CF':'codice fiscale *',
        'nome_cognome':'nome e cognome *',
        'tipo_dipendente':'tipo mansione *',
        'importo_orario_feriale':'importo orario feriale *',
        'importo_orario_regolare':'importo orario regolare *',
        'importo_orario_straordinario':'importo orario straordinario *',
        'IBAN':'IBAN *',
        'username':'username *',
        'data_di_nascita':'data di nascita *'}

        self.body = {
        'CF': '',
        'nome_cognome': '',
        'tipo_dipendente':'',
        'importo_orario_feriale':'',
        'importo_orario_regolare':'',
        'importo_orario_straordinario':'',
        'IBAN':'',
        'username':'',
        'data_di_nascita': ''
        }

        for a in self.traduzione:
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
            self.label_3.setSizePolicy(sizePolicy)
            self.label_3.setMinimumSize(QtCore.QSize(300, 0))
            self.label_3.setMaximumSize(QtCore.QSize(325, 28))
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_3.setText("")
            self.label_3.setObjectName("label_3")
            self.horizontalLayout.addWidget(self.label_3)
            self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
            self.textEdit_2.setSizePolicy(sizePolicy)
            self.textEdit_2.setMinimumSize(QtCore.QSize(300, 0))
            self.textEdit_2.setMaximumSize(QtCore.QSize(500, 30))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.textEdit_2.setFont(font)
            self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.textEdit_2.setObjectName("textEdit")
            self.horizontalLayout.addWidget(self.textEdit_2)
            self.verticalLayout_2.addLayout(self.horizontalLayout)
            _translate = QtCore.QCoreApplication.translate
            self.label_3.setText(_translate("InsDipendente", "  "+str(self.traduzione[a])))
            self.listaInput[a]=self.textEdit_2
            

        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"color: rgb(247, 247, 247);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Modify)
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(InsDipendente)
        QtCore.QMetaObject.connectSlotsByName(InsDipendente)

    def retranslateUi(self, InsDipendente):
        _translate = QtCore.QCoreApplication.translate
        InsDipendente.setWindowTitle(_translate("InsDipendente", "InsDipendente"))
        self.label.setText(_translate("InsDipendente", "Inserisci un nuovo Elemento"))
        self.label_2.setText(_translate("InsDipendente", "I campi con il segno ( * ) sono obbligatori"))
        self.pushButton.setText(_translate("InsDipendente", "Inserisci"))

    def Modify(self):
        for a in self.listaInput:
            self.body[a] = self.listaInput[a].toPlainText().replace('  ', '')
        self.risultato = self.controller.Insert(self.body)
        print(str(self.risultato))

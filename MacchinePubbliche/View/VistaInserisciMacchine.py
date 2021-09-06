from MacchinePubbliche.Controller.MacchinePubblicheC import MacchinePubblicheC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
import copy

class Ui_InsertMacchina(QWidget):
    def __init__(self, parent=None):
        super(Ui_InsertMacchina, self).__init__(parent)
        self._translate = QtCore.QCoreApplication.translate
        
        self.controller = MacchinePubblicheC()
        InsDipendente = self
        InsDipendente.setWindowTitle(self._translate("Inserisci Macchina Pubblica", "Inserisci Macchina Pubblica"))
        InsDipendente.setObjectName("Inserisci Macchina Pubblica")
        InsDipendente.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(InsDipendente)
        self.verticalLayout.setObjectName("verticalLayout")

        self.AddLabelTitolo("Inserisci una nuova macchina pubblica")
        
        #Aggiunge un scrollArea e un Vertical Layout
        self.AddScrollAreaLayout()

        #Aggiunge un descrizione dei campi
        self.AddLabelDescrizione("I campi con il segno ( * ) sono obbligatori")


        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.font = QtGui.QFont()
        self.font.setPointSize(9)
        self.listaInput = {}

        self.traduzione = {
            'codice_macchina': 'codice della macchina *',
            'tipo_macchina': 'il tipo della macchina *',
        }

        self.body = {
            'codice_macchina': None,
            'tipo_macchina': None,
        }

        self.sizePolicyTextEdit = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicyTextEdit.setHorizontalStretch(0)
        self.sizePolicyTextEdit.setVerticalStretch(0)
        self.textEditfont = QtGui.QFont()
        self.textEditfont.setPointSize(9)
        for a in self.traduzione:
            
            self.AddLabelCampo(self.traduzione[a])

            self.listaInput[a] = self.AddEdit()


        self.AddButton("Inserisci",self.Insert)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        QtCore.QMetaObject.connectSlotsByName(InsDipendente)

    #Aggiunge un pulsante con dato testo e funzione
    def AddButton(self,text,function):
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
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 255);\n color: rgb(247, 247, 247);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(function)
        self.pushButton.setText(self._translate("InsDipendente", text))
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)

    #Aggiunge un campo di campo inseribile all'utente
    def AddEdit(self):
        textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.sizePolicyTextEdit.setHeightForWidth(textEdit_2.sizePolicy().hasHeightForWidth())
        textEdit_2.setSizePolicy(self.sizePolicyTextEdit)
        textEdit_2.setMinimumSize(QtCore.QSize(300, 0))
        textEdit_2.setMaximumSize(QtCore.QSize(500, 30))
        textEdit_2.setFont(self.textEditfont)
        textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        textEdit_2.setObjectName("textEdit")
        self.horizontalLayout.addWidget(textEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        return textEdit_2

    #Aggiunge un etichetta descrittiva del campo
    def AddLabelCampo(self,text):
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(self.sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(300, 0))
        self.label_3.setMaximumSize(QtCore.QSize(325, 28))
        self.label_3.setFont(self.font)
        #self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_3.setText(self._translate("InsDipendente", "  "+str(text)))
    
    #Questa funzione aggiunge un label descrittivo delle label
    def AddLabelDescrizione(self,text):

        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(600, 50))
        self.label_2.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_2.setText(self._translate("InsDipendente",text))
        self.verticalLayout_2.addWidget(self.label_2)

    #Questa funzione aggiunge un label descrittivo della finestra
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

    #Funzione dell'inserimento
    def Insert(self):
        for a in self.listaInput:
            input = self.listaInput[a].toPlainText()
            if(input != ''):
                self.body[a] = input            
        
        self.risultato = self.controller.Insert(self.body)
        self.messaggio = ""
        if('message' in self.risultato):
            if('errors' in self.risultato):
                for a in self.risultato['errors']:
                    self.messaggio += self.risultato['errors'][a][0]+'\n'
            else:
                QMessageBox.about(self, "Errore del server ",str(self.risultato['message']))
            QMessageBox.about(self, "Errore nella compilazione dei campi",self.messaggio)
        else:
            QMessageBox.about(self, "Esito operazione","Operazione completata con successo")
            self.close()

    #Aggiunge un area scroll
    def AddScrollAreaLayout(self):
        self.scrollArea = QtWidgets.QScrollArea(self)
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
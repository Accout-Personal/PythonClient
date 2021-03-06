from Contabile.Controller.ContabileC import ContabileC
import Contabile.View.ContabileV as cont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
import copy

class Ui_ModificaContabile(QWidget):
    def __init__(self,key, parent=None):
        super(Ui_ModificaContabile, self).__init__(parent)
        self._translate = QtCore.QCoreApplication.translate
        self.key = key
        self.controller = ContabileC()
        self.chiamata = self.controller.GetKey(self.key)
        ModificaWindow = self
        ModificaWindow.setObjectName("ModificaWindow")
        ModificaWindow.resize(800, 600)
        ModificaWindow.setWindowTitle(self._translate("ModificaWindow", "Modificacontabile"))
        self.verticalLayout = QtWidgets.QVBoxLayout(ModificaWindow)
        self.verticalLayout.setObjectName("verticalLayout")

        #Aggiunge il "titolo" della finestra
        self.AddLabelTitolo("Modifica Contabile")

        #Aggiunge un scroll area per i campi
        self.scrollArea,self.scrollAreaWidgetContents,self.verticalLayout_2 = self.AddScrollArea()
        self.AddInsertHint("I campi con il segno ( * ) sono obbligatori non nulli")
        

        self.traduzione = {
            'entrata':'entrata'
        }

        #si usa un dizionario per iterare tutti i campi dell'inserimento e popolazione del campo
        self.body = {
            'ddt': self.chiamata['ddt'],
            'luogo_destinazione': self.chiamata['luogo_destinazione'],
            'entrata': self.chiamata['entrata'],
        }

        #esclude elemento non desiderato per visualizzazione
        self.viewList = copy.deepcopy(self.chiamata)
        self.exclude = ['ddt','data','luogo_destinazione']
        for elem in self.exclude:
            self.viewList.pop(elem)
        
        #settare size policy per tutti elementi
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.font = QtGui.QFont()
        self.font.setPointSize(9)
        self.listaInput = {}
        for a in self.viewList:
            if(a != "commessa"):
                #Crea il label del campo
                self.AddLabel(self.traduzione[a])
            
                #Crea il campo per la modifica
                self.listaInput[a] = self.AddField(self.chiamata[a])

        #Aggiunge il pulsante per la modifica
        self.pushButton = self.AddSubmitButton("Modifica")
        self.pushButton.clicked.connect(self.Modify)

    #Aggiunge il campo di inserimento e ritona i suoi valori
    def AddField(self,text):
        textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.sizePolicy.setHeightForWidth(textEdit_2.sizePolicy().hasHeightForWidth())
        textEdit_2.setSizePolicy(self.sizePolicy)
        textEdit_2.setMinimumSize(QtCore.QSize(300, 0))
        textEdit_2.setMaximumSize(QtCore.QSize(500, 30))
        textEdit_2.setFont(self.font)
        textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        textEdit_2.setObjectName("textEdit")
        self.horizontalLayout.addWidget(textEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self._translate = QtCore.QCoreApplication.translate
        textEdit_2.setText(self._translate("ModificaWindow", "  "+str(text)))
        return textEdit_2
    
    #Aggiunge un label descrittivo
    def AddLabel(self,text):
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sizePolicy.setHeightForWidth(label_3.sizePolicy().hasHeightForWidth())
        label_3.setSizePolicy(self.sizePolicy)
        label_3.setMinimumSize(QtCore.QSize(300, 0))
        label_3.setMaximumSize(QtCore.QSize(325, 28))
        label_3.setFont(self.font)
        label_3.setText("")
        label_3.setObjectName("label_3")
        label_3.setText(self._translate("ModificaWindow", "  "+str(text)))
        self.horizontalLayout.addWidget(label_3)

    #Operazione di modifica in seguito alla conferma
    def Modify(self):
        for a in self.listaInput:
            input = self.listaInput[a].toPlainText().replace('  ', '')
            if(input != '' and input != 'None'):
                self.body[a] = input
        self.risultato = self.controller.Update(self.body)
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
            self.OpenLista = cont.Ui_listaContabile()
            self.OpenLista.show()
            self.close()

    #Aggiunge il label titolo della finestra
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
        self.label.setText(self._translate("ModificaWindow", text))


    #aggiunge un scroll area alla finestra
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

    #questa funzione aggiunge un etichetta alla finestra
    def AddInsertHint(self,text): 
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
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
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_2.setText(self._translate("ModificaWindow", text))

    #questa funzione aggiunge una pulsante d'azione
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
        pushButton.setText(self._translate("ModificaWindow", text))
        self.verticalLayout_2.addWidget(pushButton, 0, QtCore.Qt.AlignHCenter)
        return pushButton
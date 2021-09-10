from SuddivisioneLavoro.Controller.SuddivisioneLavoroC import SuddivisioneLavoroC
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.QtWidgets import QComboBox, QMessageBox, QWidget
import copy

class Ui_InsertLavoro(QWidget):
    def __init__(self, parent=None):
        super(Ui_InsertLavoro, self).__init__(parent)
        self._translate = QtCore.QCoreApplication.translate
        
        self.controller = SuddivisioneLavoroC()
        InsertWindow = self
        InsertWindow.setWindowTitle(self._translate("InserisciCliente", "Inserisci un nuovo suddivisione lavoro"))
        InsertWindow.setObjectName("Inserisci un nuovo lavoro")
        InsertWindow.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(InsertWindow)
        self.verticalLayout.setObjectName("verticalLayout")

        self.AddLabelTitolo("Inserisci una nuova commessa")
        
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
            'commessa':'N.commessa',
            'quantita_assegnata':'quantita\'',
            'dipendente':'diendente'
        }
        self.body = {
            'commessa':None,
            'quantita_assegnata':None,
            'dipendente':None
        }

        self.AllDipendenti = self.controller.GetAllDip()
        self.DipendentiDict = {k['nome_cognome']:k['CF'] for k in self.AllDipendenti}

        self.sizePolicyTextEdit = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicyTextEdit.setHorizontalStretch(0)
        self.sizePolicyTextEdit.setVerticalStretch(0)
        self.textEditfont = QtGui.QFont()
        self.textEditfont.setPointSize(9)
        for a in self.traduzione:
            
            self.AddLabelCampo(self.traduzione[a])
            if(a == 'dipendente'):
                self.listaInput[a] = self.AddDropDown(contentList = list(self.DipendentiDict.keys()),name='dipendente')
            else:
                self.listaInput[a] = self.AddEdit()


        self.AddButton("Inserisci",self.Insert)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        QtCore.QMetaObject.connectSlotsByName(InsertWindow)

    def AddDropDown(self,text=None,contentList=[],name=None):
        
        DropDownSelect = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.sizePolicy.setHeightForWidth(DropDownSelect.sizePolicy().hasHeightForWidth())
        DropDownSelect.setSizePolicy(self.sizePolicy)
        DropDownSelect.setMinimumSize(QtCore.QSize(300, 30))
        DropDownSelect.setMaximumSize(QtCore.QSize(500, 30))
        DropDownSelect.setFont(self.font)
        DropDownSelect.setStyleSheet("background-color: rgb(255, 255, 255);")
        DropDownSelect.setObjectName(name)
        self.horizontalLayout.addWidget(DropDownSelect)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self._translate = QtCore.QCoreApplication.translate
        
        for i in range(len(contentList)):

            DropDownSelect.addItem(contentList[i])
            if(text == contentList[i]):
                DropDownSelect.setCurrentIndex(i)
        
        return DropDownSelect
    
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
        self.pushButton.setText(self._translate("InsertWindow", text))
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

    #aggiunge il calendario
    def AddCalendar(self,name=None):
        CalendarSelect = QtWidgets.QDateEdit(self.scrollAreaWidgetContents,calendarPopup=True)
        self.sizePolicy.setHeightForWidth(CalendarSelect.sizePolicy().hasHeightForWidth())
        CalendarSelect.setSizePolicy(self.sizePolicy)
        CalendarSelect.setMinimumSize(QtCore.QSize(300, 30))
        CalendarSelect.setMaximumSize(QtCore.QSize(500, 30))
        CalendarSelect.setFont(self.font)
        CalendarSelect.setStyleSheet("QDateEdit{background-color: white;}"
                                     "QCalendarWidget QWidget{ alternate-background-color: rgb(128, 128, 128); }"
                                     "QCalendarWidget QAbstractItemView:enabled{ color:black; }"
                                     "QCalendarWidget QAbstractItemView:disabled{ color:rgb(50, 50, 50); }"
                                    )
        CalendarSelect.calendarWidget().setLocale(QtCore.QLocale(QtCore.QLocale.English))
        CalendarSelect.setObjectName(name)
        self.horizontalLayout.addWidget(CalendarSelect)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        CalendarSelect.setDate(QtCore.QDate.currentDate())
        return CalendarSelect
    
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
        self.label_3.setText(self._translate("InsertWindow", "  "+str(text)))
    
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
        self.label_2.setText(self._translate("InsertWindow",text))
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
            print(self.listaInput[a].objectName())
            if(self.listaInput[a].objectName() == 'dipendente'):
                input = self.DipendentiDict[self.listaInput[a].currentText()]
            else:
                input = self.listaInput[a].toPlainText()
            if(input != '' and input!='None'):
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
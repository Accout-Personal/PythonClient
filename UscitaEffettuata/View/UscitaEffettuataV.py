from UscitaEffettuata.View.VisualizzaUscita import Ui_VistaUscita
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
from UscitaEffettuata.Controller.UscitaEffettuataC import UscitaEffettuataC


class Ui_ListaUscita(QWidget):
    def __init__(self, parent=None):
        super(Ui_ListaUscita, self).__init__(parent)
        self._translate = QtCore.QCoreApplication.translate
        ListaUscita = self
        self.controller = UscitaEffettuataC()
        self.key = 'id_transazione'
        self.chiamata = self.controller.GetAll()
        ListaUscita.setObjectName("ListaUscita")
        ListaUscita.resize(800, 600)
        ListaUscita.setWindowTitle(self._translate("ListaUscita", "ListaUscita"))
        self.verticalLayout = QtWidgets.QVBoxLayout(ListaUscita)
        self.verticalLayout.setObjectName("verticalLayout")



        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.AddLabelTitolo("Lista delle uscite")



        self.AddScrollArea()

        self.traduzione = {
        'id_transazione':'Id',
        'data_esecuzione':'data esecuzione',
        'importo_effettuato':'importo effettuato',
        }

        self.listAttr = ['id_transazione','data_esecuzione','importo_effettuato']
        #le dimensioni delle colonne
        sizes = [50,100,80]
        for attr in range(len(self.listAttr)):
            
            #Aggiunge l'intestazione della tabella
            self.AddTableHeader(self.traduzione[self.listAttr[attr]],attr,sizes[attr])

            #aggiunge elemento nella tabella
            for a in range(0,len(self.chiamata)):
                self.AddTableContent(attr,a+1,self.chiamata[a][self.listAttr[attr]],sizes[attr])

        #Aggiunge pulsante delle operazioni
        self.OperationButtons=[
            {
                "name":"Visualizza Elemento",
                "StyleSheet":"background-color: rgb(0, 255, 0);\n color: rgb(255, 255, 255);",
                "function":self.Visualizza
            },
            {
                "name":"Cancella Elemento",
                "StyleSheet":"background-color: rgb(255, 0, 0);\n color: rgb(255, 255, 255);",
                "function":self.deleteConfirm
            },
            {
                "name":"Modifica Elemento",
                "StyleSheet":"background-color: rgb(0, 0, 255);\n color: rgb(255, 255, 255);",
                "function":self.Modify
            }
        ]

        X_offset = len(self.listAttr)
        for i in range(0,len(self.OperationButtons)):
            for a in range(0,len(self.chiamata)):
                #print(i)
                self.OperationButtons[i]
                self.AddOperationButton(X_offset+i,a,self.OperationButtons[i],lambda state,b=a,c=i: self.OperationButtons[c]["function"](self.chiamata[b]))
                            

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        QtCore.QMetaObject.connectSlotsByName(ListaUscita)

    #chiamata alla funzione per la cancellazione di un elemento
    def deleteConfirm(self,uscita):

        msg = QMessageBox()
        msg.setWindowTitle('Conferma')
        msg.setText('sei sicuro di voler cancellare l\' uscita '+str(uscita['id_transazione']) + '?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        okButton = msg.button(QMessageBox.Yes)
        noButton = msg.button(QMessageBox.No)
        okButton.setText('si')
        retval = msg.exec_()
        if(msg.clickedButton() == okButton):
            print('cancellazione confermata')
            postbody = {self.key:uscita[self.key]}
            res = self.controller.Delete(postbody)
            print(res)
            self.RefreshLista = Ui_ListaUscita()
            self.RefreshLista.show()
            self.close()
        else:
            print('cancellazione annullata')   
    #Viene chiamata la funzione per visualizzare i dettagli di quell'elemento
    def Visualizza(self,elem):
        print(elem)
        self.Dettaglio = Ui_VistaUscita(str(elem[self.key]))
        self.Dettaglio.show()

    #Viene settata l'intestazione della finestra
    def AddTableHeader(self,text,pos,width):
        self.header1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sizePolicy.setHeightForWidth(self.header1.sizePolicy().hasHeightForWidth())
        self.header1.setSizePolicy(self.sizePolicy)
        self.header1.setMinimumSize(QtCore.QSize(width, 30))
        self.header1.setObjectName("header1")
        self.header1.setText(self._translate("ListaUscita",text))
        self.gridLayout.addWidget(self.header1, 0, pos, 1, 1)
    
    #Questa funzione aggiunge le label alla finestra
    def AddTableContent(self,x,y,content,width):
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(self.sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(width, 30))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_3.setText(self._translate("ListaUscita","   "+ str(content)))
        self.gridLayout.addWidget(self.label_3, y, x, 1, 1)

    #Questa funzione aggiunge un bottone a cui viene collegata una particolare funzione, da attivare quando 
    # il bottone viene premuto
    def AddOperationButton(self,x,y,buttonDict,function):
        OperationButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        OperationButton.setStyleSheet(buttonDict["StyleSheet"])
        OperationButton.setObjectName("OperationButton")
        OperationButton.setText(self._translate("ListaUscita", buttonDict["name"]))        
        OperationButton.clicked.connect(function)
        self.gridLayout.addWidget(OperationButton, y+1, x, 1, 1)
        return OperationButton

    def Modify(self,elem):
        print (elem[self.key])
        self.modificaview = Ui_ModificaEntrata(elem[self.key])
        self.modificaview.show()
    
    #Questa funzione aggiunge una scroll area
    def AddScrollArea(self):
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setStyleSheet("background-color: rgb(109, 109, 109);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 524))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

    # In questa funzione viene impostata la label che si trova sopra la lista
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
        self.label.setText(self._translate("Listauscita", text))
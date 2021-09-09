
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget

from Commessa.View.VistaListaCommesse import Ui_ListaCommesse
from Ddt.View.VistaListaDDT import Ui_ListaDDT
from Ddt.View.VistaInserisciDDT import Ui_InsertDDT

class VistaLavorazione(QWidget):
    def __init__(self, parent=None,fakeparent=None):
        super(VistaLavorazione, self).__init__(parent)
        self.fakeparent = fakeparent
        self._translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        HomeClass = self
        HomeClass.setObjectName("VistaLavorazione")
        HomeClass.resize(756, 585)
        HomeClass.setWindowTitle(_translate("HomeClass", "HomeClass"))
        self.verticalLayout = QtWidgets.QVBoxLayout(HomeClass)
        self.verticalLayout.setObjectName("verticalLayout")

        self.AddScrollArea()

        self.AddLabelTitolo("Vista Lavorazione")

        self.AddSectionLabel(1,"Commessse")
        self.horizontalLayout = self.AddHorizontalLayout(0,2)
        self.AddButtonInLayout(self.horizontalLayout,"Lista commesse",self.Go_ListaCommesse)     
        self.AddButtonInLayout(self.horizontalLayout,"Inserisci una commessa",self.Go_NewCommesse)   

        self.AddSectionLabel(3,"Documento di Trasporto (DDT)")
        self.horizontalLayout_2 = self.AddHorizontalLayout(0,4)
        self.AddButtonInLayout(self.horizontalLayout_2,"Lista DDT",self.Go_ListaDDT)     
        self.AddButtonInLayout(self.horizontalLayout_2,"Inserisci un DDT",self.Go_NewDDT)     

        self.AddSectionLabel(5,"Suddivisione Lavoro")
        self.horizontalLayout_3 = self.AddHorizontalLayout(0,6)
        self.AddButtonInLayout(self.horizontalLayout_3,"Lista lavoro",self.Go_ListaLavoro)     
        self.AddButtonInLayout(self.horizontalLayout_3,"Assegna un lavoro",self.Go_NewLavoro)     


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        QtCore.QMetaObject.connectSlotsByName(HomeClass)

    def AddScrollArea(self):

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setMinimumSize(QtCore.QSize(400, 200))
        self.scrollArea.setStyleSheet("background-color: rgb(109, 109, 109);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 732, 561))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

    def AddButtonInLayout(self,layout,text,function):
        Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        Button.setMinimumSize(QtCore.QSize(300, 50))
        Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        Button.setFont(font)
        Button.setObjectName("ListaPrezzo")
        Button.setText(self._translate("HomeClass", text))
        Button.clicked.connect(function)
        Button.setStyleSheet("background-color: rgb(85, 255, 255);")
        layout.addWidget(Button)
        return Button

    def AddSectionLabel(self,y,text):
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, y, 0, 1, 1)
        self.label_3.setText(self._translate("HomeClass", text))

    def AddHorizontalLayout(self,x,y):
        Layout = QtWidgets.QHBoxLayout()
        Layout.setContentsMargins(20, -1, 20, -1)
        Layout.setSpacing(20)
        Layout.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(Layout, y, x, 1, 1)
        return Layout
        
    def AddLabelTitolo(self,text):
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n""color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label.setText(self._translate("HomeClass", text))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

    def closeEvent(self, event):
        self.fakeparent.show()
        event.accept()


    def Go_ListaCommesse(self):
        self.ListaCommesse = Ui_ListaCommesse()
        self.ListaCommesse.show()

    def Go_NewCommesse(self):
        print('Go New Commesse')

    def Go_ListaDDT(self):
        print('go lista DDT')
        self.Ui_ListaDDT = Ui_ListaDDT()
        self.Ui_ListaDDT.show()

    def Go_NewDDT(self):
        self.NewDDT = Ui_InsertDDT()
        self.NewDDT.show()

    def Go_ListaLavorazione(self):
        print('go lista lavorazione')
        #self.ListaLavorazione = Ui_ListaListaLavorazione()
        #self.ListaLavorazione.show()

    def Go_ListaLavoro(self):
        print('go lista lavoro')
        #self.InserisciDipendente = Ui_InserisciDip()
        #self.InserisciDipendente.show()
    
    def Go_NewLavoro(self):
        print('Go new lavoro')
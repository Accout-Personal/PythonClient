from VistaFinanziari.VistaFinanziari import VistaFinanziari
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget


class Ui_HomeContabile(QWidget):
    def __init__(self, parent=None):
        super(Ui_HomeContabile, self).__init__(parent)
        _translate = QtCore.QCoreApplication.translate
        HomeContabile = self
        HomeContabile.setObjectName("HomeContabile")
        HomeContabile.resize(800, 600)
        self.handClose = 1
        self.verticalLayout = QtWidgets.QVBoxLayout(HomeContabile)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(HomeContabile)
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
        self.pushButton.setText(_translate("HomeContabile", "Vista Dati Finanziari"))
        self.pushButton.clicked.connect(self.GoVistaStrategiche)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        QtCore.QMetaObject.connectSlotsByName(HomeContabile)    
        HomeContabile.setWindowTitle(_translate("HomeContabile", "HomeContabile"))
        self.label.setText(_translate("HomeContabile", "Welcome Home"))     

    def GoVistaStrategiche(self):
        self.Anagrafica = VistaFinanziari(fakeparent=self)
        self.Anagrafica.show()
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
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QAbstractItemView, QWidget


class ui_test03(QWidget):
    def __init__(self, parent=None):
        super(ui_test03, self).__init__(parent)
        prova03 = self
        prova03.setObjectName("prova03")
        prova03.setEnabled(False)
        prova03.resize(800, 600)
        prova03.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.scrollArea = QtWidgets.QScrollArea(prova03)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 671, 401))
        self.scrollArea.setWidgetResizable(True) #prova
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(70, 20, 181, 101))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 150, 75, 23))
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #lista di prova
    
        self.lista = self.crealista()
        print(self.lista)
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(380, 20, 251, 271))
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)#prova simo
        self.listWidget.verticalScrollBar().setSingleStep(10)# altra prova
        self.listWidget.verticalScrollBar().setSingleStep(10)#altra prova
        #self.listWidget.setResizeMode()
        self.listWidget.setStyleSheet("font: 19pt \"MS Sans Serif\";")
        self.listWidget.setObjectName("listWidget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.listWidget.addItems(self.lista)
        #self.listWidget.addScrollBarWidget(Qt.ScrollBarAlwaysOn)
        self.retranslateUi(prova03)
        QtCore.QMetaObject.connectSlotsByName(prova03)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(610, 20, 20, 271))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def retranslateUi(self, prova03):
        _translate = QtCore.QCoreApplication.translate
        prova03.setWindowTitle(_translate("prova03", "prova03"))
        self.pushButton.setText(_translate("prova03", "PushButton"))
        self.pushButton_2.setText(_translate("prova03", "PushButton"))

    def crealista(self):
        a = 0
        b = []
        for a in range(100):
            b.append(str(a))
        return b

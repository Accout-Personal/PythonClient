# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_UIwindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_UIwindow, self).__init__(parent)
        UIwindow = self
        UIwindow.setObjectName("UIwindow")
        UIwindow.resize(222, 209)
        self.scrollArea = QtWidgets.QScrollArea(UIwindow)
        self.scrollArea.setGeometry(QtCore.QRect(30, 30, 141, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 139, 139))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 100, 80, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 60, 80, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 140, 80, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 190, 80, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(UIwindow)
        QtCore.QMetaObject.connectSlotsByName(UIwindow)

    def retranslateUi(self, UIwindow):
        _translate = QtCore.QCoreApplication.translate
        UIwindow.setWindowTitle(_translate("UIwindow", "UIwindow"))
        self.pushButton.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_2.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_3.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_4.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_5.setText(_translate("UIwindow", "PushButton"))


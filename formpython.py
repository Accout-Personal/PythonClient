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
        UIwindow.resize(323, 292)
        self.scrollArea = QtWidgets.QScrollArea(UIwindow)
        self.scrollArea.setGeometry(QtCore.QRect(30, 20, 251, 251))
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -54, 232, 303))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(UIwindow)
        QtCore.QMetaObject.connectSlotsByName(UIwindow)

    def retranslateUi(self, UIwindow):
        _translate = QtCore.QCoreApplication.translate
        UIwindow.setWindowTitle(_translate("UIwindow", "UIwindow"))
        self.pushButton.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_3.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_2.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_8.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_7.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_9.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_6.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_4.setText(_translate("UIwindow", "PushButton"))
        self.pushButton_5.setText(_translate("UIwindow", "PushButton"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestClass(object):
    def setupUi(self, TestClass):
        TestClass.setObjectName("TestClass")
        TestClass.resize(717, 524)
        self.pushButton = QtWidgets.QPushButton(TestClass)
        self.pushButton.setGeometry(QtCore.QRect(70, 60, 231, 121))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 10, 14);\n"
"background-image: url(:/img/img.jpg);\n"
"color: rgb(7, 255, 44);")
        self.pushButton.setLocale(QtCore.QLocale(QtCore.QLocale.Italian, QtCore.QLocale.Italy))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(TestClass)
        self.lineEdit.setGeometry(QtCore.QRect(380, 20, 171, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(TestClass)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 200, 251, 91))
        self.pushButton_2.setStyleSheet("background-color: rgb(11, 27, 255);\n"
"color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(TestClass)
        QtCore.QMetaObject.connectSlotsByName(TestClass)

    def retranslateUi(self, TestClass):
        _translate = QtCore.QCoreApplication.translate
        TestClass.setWindowTitle(_translate("TestClass", "TestClass"))
        self.pushButton.setText(_translate("TestClass", "PushButton"))
        self.pushButton_2.setText(_translate("TestClass", "PushButton"))


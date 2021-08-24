# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import copy

class Ui_UIwindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_UIwindow, self).__init__(parent)
        self.pushButton = []
        UIwindow = self
        UIwindow.setObjectName("UIwindow")
        UIwindow.resize(312, 362)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UIwindow.sizePolicy().hasHeightForWidth())
        UIwindow.setSizePolicy(sizePolicy)
        self.formLayout = QtWidgets.QFormLayout(UIwindow)
        self.formLayout.setObjectName("formLayout")
        self.scrollArea = QtWidgets.QScrollArea(UIwindow)
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 102, 303))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        _translate = QtCore.QCoreApplication.translate

        #UIwindow
        for i in range(20):
            #print(i)
            self.pushButton.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
            self.pushButton[i].setObjectName("pushButton"+str(i))
            self.gridLayout_2.addWidget(self.pushButton[i], i, 0, 1, 1)
            self.pushButton[i].setText(_translate("UIwindow", "PushButton"+str(i)))
            self.pushButton[i].clicked.connect(lambda state,a=i: self.printbutton(a))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.scrollArea)
        QtCore.QMetaObject.connectSlotsByName(UIwindow)

    def printbutton(self,i):
        print(i)
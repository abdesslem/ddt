# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sat Oct 11 23:04:33 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(620, 413)
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(10, 10, 91, 51))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(10, 80, 91, 51))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(10, 150, 91, 51))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 10, 431, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 380, 591, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.lcdNumber = QtGui.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 350, 64, 23))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(100, 10, 61, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(110, 150, 501, 221))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "DDT", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Dialog", "démarrer", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Dialog", "pause", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("Dialog", "stop", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("Dialog", "URL", None, QtGui.QApplication.UnicodeUTF8))


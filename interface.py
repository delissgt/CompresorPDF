# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(487, 289)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.bComprimir = QtGui.QPushButton(self.centralwidget)
        self.bComprimir.setObjectName(_fromUtf8("bComprimir"))
        self.verticalLayout.addWidget(self.bComprimir)
        self.bBorrar = QtGui.QPushButton(self.centralwidget)
        self.bBorrar.setObjectName(_fromUtf8("bBorrar"))
        self.verticalLayout.addWidget(self.bBorrar)
        self.bBorrarTodo = QtGui.QPushButton(self.centralwidget)
        self.bBorrarTodo.setObjectName(_fromUtf8("bBorrarTodo"))
        self.verticalLayout.addWidget(self.bBorrarTodo)
        self.bAgregar = QtGui.QPushButton(self.centralwidget)
        self.bAgregar.setObjectName(_fromUtf8("bAgregar"))
        self.verticalLayout.addWidget(self.bAgregar)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bComprimir.setText(_translate("MainWindow", "Comprimir", None))
        self.bBorrar.setText(_translate("MainWindow", "Borrar", None))
        self.bBorrarTodo.setText(_translate("MainWindow", "Borrar Todo", None))
        self.bAgregar.setText(_translate("MainWindow", "Agregar", None))


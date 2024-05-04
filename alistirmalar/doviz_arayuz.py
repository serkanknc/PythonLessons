# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doviz.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 199)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.lineDoviz = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDoviz.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.lineDoviz.setObjectName("lineDoviz")
        self.pushHesapla = QtWidgets.QPushButton(self.centralwidget)
        self.pushHesapla.setGeometry(QtCore.QRect(180, 10, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setBold(False)
        font.setWeight(50)
        self.pushHesapla.setFont(font)
        self.pushHesapla.setObjectName("pushHesapla")
        self.radioUSD = QtWidgets.QRadioButton(self.centralwidget)
        self.radioUSD.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioUSD.setObjectName("radioUSD")
        self.pushAltinBilgi = QtWidgets.QPushButton(self.centralwidget)
        self.pushAltinBilgi.setGeometry(QtCore.QRect(10, 110, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setBold(True)
        font.setWeight(75)
        self.pushAltinBilgi.setFont(font)
        self.pushAltinBilgi.setObjectName("pushAltinBilgi")
        self.labelAltin = QtWidgets.QLabel(self.centralwidget)
        self.labelAltin.setGeometry(QtCore.QRect(10, 150, 161, 21))
        self.labelAltin.setText("")
        self.labelAltin.setObjectName("labelAltin")
        self.radioEuro = QtWidgets.QRadioButton(self.centralwidget)
        self.radioEuro.setGeometry(QtCore.QRect(90, 40, 82, 17))
        self.radioEuro.setObjectName("radioEuro")
        self.radioSterlin = QtWidgets.QRadioButton(self.centralwidget)
        self.radioSterlin.setGeometry(QtCore.QRect(40, 70, 82, 17))
        self.radioSterlin.setObjectName("radioSterlin")
        self.labelDovizSonuc = QtWidgets.QLabel(self.centralwidget)
        self.labelDovizSonuc.setGeometry(QtCore.QRect(180, 40, 171, 61))
        self.labelDovizSonuc.setText("")
        self.labelDovizSonuc.setObjectName("labelDovizSonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Döviz Çeviri"))
        self.label.setText(_translate("MainWindow", "Döviz :"))
        self.pushHesapla.setText(_translate("MainWindow", "Hesapla"))
        self.radioUSD.setText(_translate("MainWindow", "USD"))
        self.pushAltinBilgi.setText(_translate("MainWindow", "Altın Bilgisi İçin Tıklayın"))
        self.radioEuro.setText(_translate("MainWindow", "EURO"))
        self.radioSterlin.setText(_translate("MainWindow", "STERLIN"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remote_ac.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.powerButton = QtWidgets.QPushButton(self.centralwidget)
        self.powerButton.setGeometry(QtCore.QRect(150, 50, 100, 40))
        self.powerButton.setObjectName("powerButton")
        self.tempUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempUpButton.setGeometry(QtCore.QRect(150, 100, 100, 40))
        self.tempUpButton.setObjectName("tempUpButton")
        self.tempDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempDownButton.setGeometry(QtCore.QRect(150, 150, 100, 40))
        self.tempDownButton.setObjectName("tempDownButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote AC"))
        self.powerButton.setText(_translate("MainWindow", "Power"))
        self.tempUpButton.setText(_translate("MainWindow", "Temp Up"))
        self.tempDownButton.setText(_translate("MainWindow", "Temp Down"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

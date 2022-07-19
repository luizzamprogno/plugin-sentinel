# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sentinel_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SentinelDialogBase(object):
    def setupUi(self, SentinelDialogBase):
        SentinelDialogBase.setObjectName("SentinelDialogBase")
        SentinelDialogBase.resize(412, 281)
        self.pushButton = QtWidgets.QPushButton(SentinelDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(SentinelDialogBase)
        self.label.setGeometry(QtCore.QRect(160, 90, 101, 41))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(SentinelDialogBase)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 40, 80, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(SentinelDialogBase)
        self.calendarWidget.setGeometry(QtCore.QRect(70, 100, 280, 156))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(SentinelDialogBase)
        QtCore.QMetaObject.connectSlotsByName(SentinelDialogBase)

    def retranslateUi(self, SentinelDialogBase):
        _translate = QtCore.QCoreApplication.translate
        SentinelDialogBase.setWindowTitle(_translate("SentinelDialogBase", "sentinel_images"))
        self.pushButton.setText(_translate("SentinelDialogBase", "PushButton"))
        self.label.setText(_translate("SentinelDialogBase", "Teste"))
        self.pushButton_2.setText(_translate("SentinelDialogBase", "Calendar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SentinelDialogBase = QtWidgets.QDialog()
    ui = Ui_SentinelDialogBase()
    ui.setupUi(SentinelDialogBase)
    SentinelDialogBase.show()
    sys.exit(app.exec_())


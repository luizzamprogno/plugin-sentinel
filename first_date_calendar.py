# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_date_calendar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        data_maxima = QDate.currentDate()

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setMaximumDate(QDate(data_maxima))
        self.calendarWidget.setGridVisible(True)

        self.calendarWidget.clicked.connect(lambda dateval:print(dateval.toString()))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Sentinel
                                 A QGIS plugin
 download sentinel images
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-01
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Zampronio
        email                : lpzampronio@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog
from qgis.gui import QgsMapToolEmitPoint
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate

# Initialize Qt resources from file resources.py
from .resources import *

# Import the code for the dialog
from .sentinel_dialog import SentinelDialog, FirstDateCalendar
import os.path
import ee
import geemap
import os
from os.path import expanduser


class Sentinel():
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Sentinel_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Download Bandas Sentinel')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        return QCoreApplication.translate('Sentinel', message)

    def add_action(
            self,
            icon_path,
            text,
            callback,
            enabled_flag=True,
            add_to_menu=True,
            add_to_toolbar=True,
            status_tip=None,
            whats_this=None,
            parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToRasterMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/sentinel/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Download Sentinel'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginRasterMenu(
                self.tr(u'&sentinel_images'),
                action)
            self.iface.removeToolBarIcon(action)

    def firstCalendar(self):

        data_maxima = QDate.currentDate()

        self.cal = FirstDateCalendar()
        self.cal.setWindowTitle('Data Inicial')
        self.cal.calendar.setGridVisible(True)
        self.cal.calendar.setObjectName("calendarWidget")
        self.cal.calendar.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.cal.calendar.setMaximumDate(QDate(data_maxima))
        self.cal.calendar.setGridVisible(True)

        self.cal.calendar.clicked.connect(self.firstDateConverter)
        self.cal.okButton.clicked.connect(lambda cal: self.cal.close())

        self.cal.show()
        self.cal.exec_()

    def firstDateConverter(self, qDate):
        date = '{0}-{1}-{2}'.format(qDate.year(), qDate.month(), qDate.day())
        self.dlg.firstDateText.setText(str(date))

    def secondCalendar(self):

        data_maxima = QDate.currentDate()

        self.cal = FirstDateCalendar()
        self.cal.setWindowTitle('Data Inicial')
        self.cal.calendar.setGridVisible(True)
        self.cal.calendar.setObjectName("calendarWidget")
        self.cal.calendar.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.cal.calendar.setMaximumDate(QDate(data_maxima))
        self.cal.calendar.setGridVisible(True)

        self.cal.calendar.clicked.connect(self.secondDateConverter)
        self.cal.okButton.clicked.connect(lambda cal: self.cal.close())

        self.cal.show()
        self.cal.exec_()

    def secondDateConverter(self, qDate):
        date = '{0}-{1}-{2}'.format(qDate.year(), qDate.month(), qDate.day())
        self.dlg.lastDateText.setText(str(date))

    def getBands(self):

        b1 = self.dlg.B1.isChecked()
        b2 = self.dlg.B2.isChecked()
        b3 = self.dlg.B3.isChecked()
        b4 = self.dlg.B4.isChecked()
        b5 = self.dlg.B5.isChecked()
        b6 = self.dlg.B6.isChecked()
        b7 = self.dlg.B7.isChecked()
        b8 = self.dlg.B8.isChecked()
        b8a = self.dlg.B8A.isChecked()
        b9 = self.dlg.B9.isChecked()
        b11 = self.dlg.B11.isChecked()
        b12 = self.dlg.B12.isChecked()
        allBands = self.dlg.All.isChecked()

        self.bandas = []

        if b1 == True:
            self.bandas.append('B1')

        if b2 == True:
            self.bandas.append('B2')

        if b3 == True:
            self.bandas.append('B3')

        if b4 == True:
            self.bandas.append('B4')

        if b5 == True:
            self.bandas.append('B5')

        if b6 == True:
            self.bandas.append('B6')

        if b7 == True:
            self.bandas.append('B7')

        if b8 == True:
            self.bandas.append('B8')

        if b8a == True:
            self.bandas.append('B8A')

        if b9 == True:
            self.bandas.append('B9')

        if b11 == True:
            self.bandas.append('B11')

        if b12 == True:
            self.bandas.append('B12')


        return self.bandas

    def selectAll(self, state):

        self.checkBoxes = [self.dlg.B1, self.dlg.B2, self.dlg.B3, self.dlg.B4,
                           self.dlg.B5, self.dlg.B6, self.dlg.B7, self.dlg.B8,
                           self.dlg.B8A, self.dlg.B9, self.dlg.B11, self.dlg.B12]

        for checkBox in self.checkBoxes:
            checkBox.setCheckState(state)

    def cancelButton(self):

        self.checkBoxes = [self.dlg.B1, self.dlg.B2, self.dlg.B3, self.dlg.B4,
                           self.dlg.B5, self.dlg.B6, self.dlg.B7, self.dlg.B8,
                           self.dlg.B8A, self.dlg.B9, self.dlg.B11, self.dlg.B12]

        for checkBox in self.checkBoxes:
            checkBox.setCheckState(False)

        self.dlg.firstDateText.clear()
        self.dlg.lastDateText.clear()
        self.dlg.spinBox.setValue(0)
        self.dlg.All.setCheckState(False)
        self.dlg.saveText.clear()

        self.dlg.close()

    def choose_directory(self):
        input_dir = QFileDialog.getExistingDirectory(
            None, 'Selecione a pasta:', expanduser("~"))
        self.dlg.saveText.setText(input_dir)

    def exec_function(self):

        ee.Initialize()

        start = ee.Date(str(self.dlg.firstDateText.text()))
        finish = ee.Date(str(self.dlg.lastDateText.text()))

        longitude = self.dlg.spbLong.value()
        latitude = self.dlg.spbLat.value()


        loc = ee.Geometry.Point(longitude, latitude)
        out_dir = self.dlg.saveText.text()

        bandNames = self.bandas

        colletionNames = []
        cloudPercentage = self.dlg.spinBox.value()

        def collection_sat():

            for bands in bandNames:
                collection = ee.ImageCollection('COPERNICUS/S2_SR')\
                    .filterBounds(loc)\
                    .filterDate(start, finish)\
                    .select(bands)\
                    .filter(ee.Filter.lte('CLOUDY_PIXEL_PERCENTAGE', cloudPercentage))

                colletionNames.append(collection)

        def exportCol():

            mc = self.canvas

            listRec = []

            xMin = mc.extent().xMinimum()
            listRec.append(xMin)
            yMin = mc.extent().yMinimum()
            listRec.append(yMin)
            xMax = mc.extent().xMaximum()
            listRec.append(xMax)
            yMax = mc.extent().yMaximum()
            listRec.append(yMax)

            rect = ee.Geometry.Rectangle(listRec)

            for export in colletionNames:
                n = export.size().getInfo()

                for i in range(n):

                    colList = export.toList(5000)
                    img = ee.Image(colList.get(i))
                    band = img.bandNames().getInfo()
                    date = ee.Date(img.get('system:time_start')).format(
                        "Y '_' M '_' d").getInfo()
                    filename = os.path.join(out_dir,
                                            str(band) + '_' + str(date) + '.tif')

                    geemap.ee_export_image(img, filename=filename, region=rect, scale=10)

        collection_sat()
        exportCol()

    def run(self):
        if self.first_start == True:
            self.first_start = False
            self.dlg = SentinelDialog()
            self.dlg.setWindowTitle('Download de imagens Sentinel - MSI_SR')

            self.dlg.firstDateButton.clicked.connect(self.firstCalendar)
            self.dlg.lastDateButton.clicked.connect(self.secondCalendar)

            self.dlg.B1.stateChanged.connect(self.getBands)
            self.dlg.B2.stateChanged.connect(self.getBands)
            self.dlg.B3.stateChanged.connect(self.getBands)
            self.dlg.B4.stateChanged.connect(self.getBands)
            self.dlg.B5.stateChanged.connect(self.getBands)
            self.dlg.B6.stateChanged.connect(self.getBands)
            self.dlg.B7.stateChanged.connect(self.getBands)
            self.dlg.B8.stateChanged.connect(self.getBands)
            self.dlg.B8A.stateChanged.connect(self.getBands)
            self.dlg.B9.stateChanged.connect(self.getBands)
            self.dlg.B11.stateChanged.connect(self.getBands)
            self.dlg.B12.stateChanged.connect(self.getBands)
            self.dlg.All.stateChanged.connect(self.selectAll)

            self.dlg.runButton.clicked.connect(self.exec_function)
            self.dlg.saveButton.clicked.connect(self.choose_directory)

            self.dlg.cancelButton.clicked.connect(self.cancelButton)

        mc = self.iface.mapCanvas()
        self.dlg.spbLat.setValue(mc.center().y())
        self.dlg.spbLong.setValue(mc.center().x())

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            pass

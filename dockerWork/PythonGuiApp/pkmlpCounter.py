#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QSlider

intCounter = 0
intSchrittweite = 1
intMaximum = 9
intMinimum = 0

class PkmlpCounter(QtWidgets.QMainWindow):

    def __init__(self):
        super(PkmlpCounter, self).__init__()
        #
        #
        #
        # Laden des im Qt-Designer erstellten GUI
        #
        uic.loadUi('pkmlpCounterGui.ui', self)
        #
        #
        #
        # Liste mit der Auswahl für die Counter-Wertebereiche erstellen
        # und die Auswahl der Counter-Wertebereiche in die ComboBox laden
        #
        self.stellen = [' 1-stellig (0-9) ',
                        ' 2-stellig (0-99) ',
                        ' 3-stellig (0-999) ']
        self.comboBox.addItems(self.stellen)
        #
        #
        #
        # Anzeigen und Konfigurieren des Slider für die Counter-Schrittweite
        #

        self.horsliderSteps.setTickPosition(QtWidgets.QSlider.TicksBelow)


        self.horsliderSteps.setMinimum(1)
        self.horsliderSteps.setMaximum(5)
        self.horsliderSteps.setTickInterval(1)
        self.horsliderSteps.setSingleStep(1)
        #
        #
        #
        # Nach Aubereitung des GUI dieses anzeigen
        #
        self.setAnzeige()
        self.statusBar.setStyleSheet("QStatusBar {background:lightgray}")
        self.statusBar.showMessage(u'Bereit')
        self.show()
        #
        #
        #
        # Aufrufen der entsprechenden Funktion, wenn
        # der jeweilige Counter-Button gedrückt wird
        #
        self.btnAdd.clicked.connect(self.addieren)
        self.btnReset.clicked.connect(self.reseten)
        self.btnSubtract.clicked.connect(self.subtrahieren)
        #
        #
        #
        # Aufrufen der Funktion wenn Slider verändert wurde
        #
        self.horsliderSteps.valueChanged.connect(self.schrittweite)
        #
        #
        #
        # Aufrufen der Funktion wenn ComboBox verändert wurde
        #
        self.comboBox.currentIndexChanged.connect(self.bereich)
        #
        #
        #
        # Aufrufen der Funktion wenn RadioButton verändert wurde
        #
        self.radioButtonRollover.clicked.connect(self.rollover)
        self.radioButtonStopping.clicked.connect(self.stopping)
        #
        #
        #
        # Dem Exit-Menu die entsprechende Aktion zuweisen
        #
        self.actionExit.triggered.connect(self.exit)
        #
        #
        #
        # Dem About-Menu die entsprechende Aktion zuweisen
        #
        self.actionAbout.triggered.connect(self.about)
        #
        #
        #
        # Den  restlichen Menu-Punkten die entsprechende Aktion zuweisen
        #
        self.actionAdd.triggered.connect(self.addieren)
        self.actionReset.triggered.connect(self.reseten)
        self.actionSubtract.triggered.connect(self.subtrahieren)
        self.actionRollover.triggered.connect(self.rollover)
        self.actionStopping.triggered.connect(self.stopping)
        self.action_1_stellig.triggered.connect(self.menuBereich1)
        self.action_2_stellig.triggered.connect(self.menuBereich2)
        self.action_3_stellig.triggered.connect(self.menuBereich3)
        self.action_1.triggered.connect(self.stepSize1)
        self.action_2.triggered.connect(self.stepSize2)
        self.action_3.triggered.connect(self.stepSize3)
        self.action_4.triggered.connect(self.stepSize4)
        self.action_5.triggered.connect(self.stepSize5)



    def addieren(self):
        global intCounter, intSchrittweite, intMaximum, intMinimum
        if intCounter + intSchrittweite <= intMaximum:
            intCounter += intSchrittweite
        elif self.radioButtonStopping.isChecked():
            intCounter = intMaximum
        else:
            intCounter = intCounter + intSchrittweite - intMaximum - 1
        self.setAnzeige()
        self.statusBar.showMessage(u'Zähler erhöht')


    def reseten(self):
        global intCounter, intMinimum
        intCounter = intMinimum
        self.setAnzeige()
        self.statusBar.showMessage(u'Zähler zurückgestellt')


    def subtrahieren(self):
        global intCounter, intSchrittweite, intMaximum, intMinimum
        if intCounter - intSchrittweite >= intMinimum:
            intCounter -= intSchrittweite
        elif self.radioButtonStopping.isChecked():
            intCounter = intMinimum
        else:
            intCounter = intCounter + intMaximum - intSchrittweite + 1
        self.setAnzeige()
        self.statusBar.showMessage(u'Zähler vermindert')


    def schrittweite(self):
        global intSchrittweite
        intSchrittweite = self.horsliderSteps.value()
        self.statusBar.showMessage(u'Schrittweite geändert')


    def stepSize1(self):
        global intSchrittweite
        intSchrittweite = 1
        self.horsliderSteps.setValue(intSchrittweite)
        self.statusBar.showMessage(u'Schrittweite geändert')


    def stepSize2(self):
        global intSchrittweite
        intSchrittweite = 2
        self.horsliderSteps.setValue(intSchrittweite)
        self.statusBar.showMessage(u'Schrittweite geändert')


    def stepSize3(self):
        global intSchrittweite
        intSchrittweite = 3
        self.horsliderSteps.setValue(intSchrittweite)
        self.statusBar.showMessage(u'Schrittweite geändert')


    def stepSize4(self):
        global intSchrittweite
        intSchrittweite = 4
        self.horsliderSteps.setValue(intSchrittweite)
        self.statusBar.showMessage(u'Schrittweite geändert')


    def stepSize5(self):
        global intSchrittweite
        intSchrittweite = 5
        self.horsliderSteps.setValue(intSchrittweite)
        self.statusBar.showMessage(u'Schrittweite geändert')


    def bereich(self):
        global intMaximum, intCounter
        #
        if str(self.comboBox.currentText()) == " 1-stellig (0-9) ":
            intMaximum = 9
        elif str(self.comboBox.currentText()) == " 2-stellig (0-99) ":
            intMaximum = 99
        else:
            intMaximum = 999
        #
        if intCounter > intMaximum:
            intCounter = intMaximum
        self.setAnzeige()
        self.statusBar.showMessage(u'Stellen geändert')
        #
        #
        # Damit das Hauptfenster wieder auf die Tastatur reagiert
        #
        app.activeWindow().setFocus()


    def menuBereich1(self):
        global intCounter,intMaximum
        intMaximum = 9
        self.comboBox.setCurrentIndex(0)
        if intCounter > intMaximum:
            intCounter = intMaximum
        self.setAnzeige()
        self.statusBar.showMessage(u'Stellen geändert')


    def menuBereich2(self):
        global intCounter,intMaximum
        intMaximum = 99
        self.comboBox.setCurrentIndex(1)
        if intCounter > intMaximum:
            intCounter = intMaximum
        self.setAnzeige()
        self.statusBar.showMessage(u'Stellen geändert')


    def menuBereich3(self):
        global intCounter,intMaximum
        intMaximum = 999
        self.comboBox.setCurrentIndex(2)
        if intCounter > intMaximum:
            intCounter = intMaximum
        self.setAnzeige()
        self.statusBar.showMessage(u'Stellen geändert')


    def rollover(self):
        self.radioButtonRollover.setChecked(True)
        self.statusBar.showMessage(u'Type geändert')


    def stopping(self):
        self.radioButtonStopping.setChecked(True)
        self.statusBar.showMessage(u'Type geändert')


    def exit(self):
        self.close()


    def setAnzeige(self):
        global intCounter, intMaximum, intMinimum
        self.lcdNumberCounter.display(intCounter)
        self.progressBarCounter.setMinimum(intMinimum)
        self.progressBarCounter.setMaximum(intMaximum)
        self.progressBarCounter.setValue(intCounter)


    def about(self):
        QtWidgets.QMessageBox.about(self,
                          "\n\nAbout TallyCounter",
                          "PyQt-Demoprogramm\n\n   (c) www.pkmlp.ch")


    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = PkmlpCounter()
    win.show()
    app.exec_()

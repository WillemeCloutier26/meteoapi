import requests
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QTextEdit, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QToolTip, QLineEdit, QLabel, QCheckBox, QComboBox, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from textjouer import stringToucher, meteoallo

list_retour = meteoallo("Vendredi")


"""
Willème Cloutier
Ceci est un projet d'approfondissement afin d'améliorer mes capacités avec python et la gestion de donné. 
l'importation de "requests" va me permettre d'utiliser une api afin de pouvoir faciliter l'utilisation d'un satelite personnel établie dans le périmetre de Victoriaville.
le "requests" va me retouner des données de l'api et ensuite avec des outils implémenter dans python je vais le mettre en json pour faciliter la compréhension.
Cette partie fait en sorte qu'on aille la prévision météorologique de cinq jours dans le futurs et en plus aujourd'hui.
On va aussi demander la journée qu'on désire avoir la prévision météorologique.
"""
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Application Météo"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        buttonWindow1 = QPushButton('Météo dans les jours à suivre', self)
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        self.lineEdit1 = QLineEdit("Écrire la journée que vous désirer (Maximum = 6 jours dans la prévision)", self)
        buttonWindow1.setGeometry(50, 150, 200, 40)
        self.lineEdit1.setGeometry(250, 150, 400, 40)

        buttonWindow3 = QPushButton('Météo immédiatement', self)
        buttonWindow3.clicked.connect(self.buttonWindow3_onClick)
        buttonWindow3.setGeometry(50, 300, 200, 40)
        self.show()

    @pyqtSlot()
    def buttonWindow1_onClick(self):
        self.statusBar().showMessage("Changer pour Météo à venir")
        search_day = stringToucher(self.lineEdit1.text())
        global list_retour 
        list_retour = meteoallo(self.lineEdit1.text())
        print(list_retour)
        self.cams = Window1(self.lineEdit1.text())
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonWindow3_onClick(self):
        self.statusBar().showMessage("Changer pour Météo Maintenant")
        self.cams = Window3(list_retour[0])
        self.cams.show()
        self.close()

print(list_retour)
class Window1(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Météo Prévision')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))
        label1 = QLabel(value)
        labelnarative = QLabel(list_retour[1])
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(QIcon(list_retour[3]))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet(
            'background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(labelnarative)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

class Window3(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window3')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(QIcon(list_retour[4]))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet(
            'background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

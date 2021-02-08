import requests
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QTextEdit, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QToolTip, QLineEdit, QLabel, QCheckBox, QComboBox, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
Willème Cloutier
Ceci est un projet d'approfondissement afin d'améliorer mes capacités avec python et la gestion de donné. 
l'importation de "requests" va me permettre d'utiliser une api afin de pouvoir faciliter l'utilisation d'un satelite personnel établie dans le périmetre de Victoriaville.
le "requests" va me retouner des données de l'api et ensuite avec des outils implémenter dans python je vais le mettre en json pour faciliter la compréhension.
Cette partie fait en sorte qu'on aille la prévision météorologique de cinq jours dans le futurs et en plus aujourd'hui.
On va aussi demander la journée qu'on désire avoir la prévision météorologique.
"""

urlsjour = requests.get(
    'https://api.weather.com/v3/wx/forecast/daily/5day?geocode=46.05,-71.96&format=json&units=m&language=fr-CA&apiKey=21553e0235304f40953e0235300f4055').json()
print(urlsjour["dayOfWeek"])
search_day = input("Donner la journée voulu : ")
search_day_number = 0
day_number_part = search_day_number


dayInWeek = len(urlsjour["dayOfWeek"])
for day in range(dayInWeek):
    if urlsjour["dayOfWeek"][day] == search_day:
        search_day_number = day
        break

if search_day_number == 0:
    day_number_part = 0
elif search_day_number == 1:
    day_number_part = 2
elif search_day_number == 2:
    day_number_part = 4
elif search_day_number == 3:
    day_number_part = 6
elif search_day_number == 4:
    day_number_part = 8
elif search_day_number == 5:
    day_number_part = 10


#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################

urlshistorique = requests.get(
    'https://api.weather.com/v2/pws/observations/hourly/7day?stationId=IVICTORI1625&format=json&units=m&apiKey=21553e0235304f40953e0235300f4055').json()

hoursInWeek = len(urlshistorique["observations"])
"""
for day in range(hoursInWeek):
    print(urlshistorique["observations"][day]["obsTimeLocal"],
          urlshistorique["observations"][day]["metric"])
"""
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################

ulrsmaintenant = requests.get(
    'https://api.weather.com/v2/pws/observations/current?stationId=IVICTORI1625&format=json&units=m&apiKey=21553e0235304f40953e0235300f4055').json()

string_maintenant = ""
string_maintenant = str(ulrsmaintenant["observations"][0]["metric"]["temp"])
string_prevision = ""
string_prevision = str(ulrsmaintenant["observations"][search_day_number]["metric"]["temp"])


#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################


image_jour = (urlsjour["daypart"][0]["wxPhraseLong"][0])
img = ""

if image_jour == "Pluie / Neige" and ulrsmaintenant["observations"][0]["metric"]["temp"] <0 :
    img = "Neige.png"
elif image_jour == "Chutes de neige":
    img = "Neige.png"
elif image_jour == "Peu nuageux":
    img = "Nuage.png"
elif image_jour == "Plutôt ensoleillé":
    img = "Soleil.png"
elif image_jour == "Ensoleillé":
    img = "Soleil.png"
elif image_jour == "Nuageux":
    img = "Nuage.png"
elif image_jour == "Chutes de neige dans l’après-midi":
    img = "Neige.png"
elif image_jour == "Chutes de neige dans la matinée":
    img = "Neige.png"
elif image_jour == "Pluie / Neige" and ulrsmaintenant["observations"][0]["metric"]["temp"] >0:
    img = "Pluie.png"
elif image_jour == "Précipitations hivernales":
    img = "Neige.png"
elif image_jour == "Pluie verglaçante devenant neige":
    img = "Pluie.png"
elif image_jour == "Plutôt ensoleillé":
    img = "Soleil.png"

image_prévision = (urlsjour["daypart"][day_number_part]["wxPhraseLong"][0])
img_prévision = ""

if image_jour == "Pluie / Neige" and ulrsmaintenant["observations"][0]["metric"]["temp"] <0 :
    img_prévision = "Neige.png"
elif image_jour == "Chutes de neige":
    img_prévision = "Neige.png"
elif image_jour == "Peu nuageux":
    img_prévision = "Nuage.png"
elif image_jour == "Plutôt ensoleillé":
    img_prévision = "Soleil.png"
elif image_jour == "Ensoleillé":
    img_prévision = "Soleil.png"
elif image_jour == "Nuageux":
    img_prévision = "Nuage.png"
elif image_jour == "Chutes de neige dans l’après-midi":
    img_prévision = "Neige.png"
elif image_jour == "Chutes de neige dans la matinée":
    img_prévision = "Neige.png"
elif image_jour == "Pluie / Neige" and ulrsmaintenant["observations"][0]["metric"]["temp"] >0:
    img_prévision = "Pluie.png"
elif image_jour == "Précipitations hivernales":
    img_prévision = "Neige.png"


#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "App"
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
        self.lineEdit1 = QLineEdit("Écrire la journée que vous désirer", self)
        buttonWindow1.setGeometry(100, 100, 200, 40) 
        self.lineEdit1.setGeometry(400, 100, 200, 40) 

        buttonWindow2 = QPushButton('Historique de Météo', self)
        buttonWindow2.clicked.connect(self.buttonWindow2_onClick)
        self.lineEdit2 = QLineEdit("Type here what you want to transfer for [Window1].", self) ########
        buttonWindow2.setGeometry(100, 200, 200, 40)
        self.lineEdit2.setGeometry(400, 200, 200, 40)  ########

        buttonWindow3 = QPushButton('Météo immédiatement', self)
        buttonWindow3.clicked.connect(self.buttonWindow3_onClick)
        buttonWindow3.setGeometry(100, 300, 200, 40) 
        self.show()

    @pyqtSlot()
    def buttonWindow1_onClick(self):
        self.statusBar().showMessage("Changer pour Météo à venir")
        self.cams = Window1(self.lineEdit1.text()) 
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonWindow2_onClick(self):
        self.statusBar().showMessage("Changer pour l'historique")
        self.cams = Window2(self.lineEdit2.text()) 
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonWindow3_onClick(self):
        self.statusBar().showMessage("Changer pour Météo Maintenant")
        self.cams = Window3(string_maintenant) 
        self.cams.show()
        self.close()

class Window1(QDialog):
    def __init__(self,value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Météo Prévision')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(QIcon(img_prévision))
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


class Window2(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Historique Météo')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
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

class Window3(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window3')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(QIcon(img))
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

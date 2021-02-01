"""
Willème Cloutier
Ceci est un projet d'approfondissement afin d'améliorer mes capacités avec python et la gestion de donné. 
l'importation de "requests" va me permettre d'utiliser une api afin de pouvoir faciliter l'utilisation d'un satelite personnel établie dans le périmetre de Victoriaville.
le "requests" va me retouner des données de l'api et ensuite avec des outils implémenter dans python je vais le mettre en json pour faciliter la compréhension.
Cette partie fait en sorte qu'on aille la météo maintenant. 
"""

import requests

data = requests.get('https://api.weather.com/v2/pws/observations/current?stationId=IVICTORI1625&format=json&units=m&apiKey=21553e0235304f40953e0235300f4055').json()

print (data["observations"][0]["metric"])



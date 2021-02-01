"""
Willème Cloutier
Ceci est un projet d'approfondissement afin d'améliorer mes capacités avec python et la gestion de donné. 
l'importation de "requests" va me permettre d'utiliser une api afin de pouvoir faciliter l'utilisation d'un satelite personnel établie dans le périmetre de Victoriaville.
le "requests" va me retouner des données de l'api et ensuite avec des outils implémenter dans python je vais le mettre en json pour faciliter la compréhension.
Cette partie fait en sorte qu'on aille l'historique météorologique de six jours dans le passé et en plus aujourd'hui.
On va aussi demander la journée et l'heure qu'on désire avoir l'historique météorologique.
"""

import requests

urls = requests.get('https://api.weather.com/v2/pws/observations/hourly/7day?stationId=IVICTORI1625&format=json&units=m&apiKey=21553e0235304f40953e0235300f4055').json()

hoursInWeek = len(urls["observations"])

for day in range(hoursInWeek):
   print(urls["observations"][day]["obsTimeLocal"] , urls["observations"][day]["metric"])

"""
Willème Cloutier
Ceci est un projet d'approfondissement afin d'améliorer mes capacités avec python et la gestion de donné. 
l'importation de "requests" va me permettre d'utiliser une api afin de pouvoir faciliter l'utilisation d'un satelite personnel établie dans le périmetre de Victoriaville.
le "requests" va me retouner des données de l'api et ensuite avec des outils implémenter dans python je vais le mettre en json pour faciliter la compréhension.
Cette partie fait en sorte qu'on aille la prévision météorologique de cinq jours dans le futurs et en plus aujourd'hui.
On va aussi demander la journée qu'on désire avoir la prévision météorologique.
"""

import requests

urls = requests.get('https://api.weather.com/v3/wx/forecast/daily/5day?geocode=46.05,-71.96&format=json&units=m&language=fr-CA&apiKey=21553e0235304f40953e0235300f4055').json()   
print(urls["dayOfWeek"])
search_day = input("Donner la journée voulu : ")
search_day_number = 0


dayInWeek = len(urls["dayOfWeek"])
for day in range(dayInWeek):
    if urls["dayOfWeek"][day] == search_day:
        search_day_number = day
        break

print (urls["narrative"][search_day_number])
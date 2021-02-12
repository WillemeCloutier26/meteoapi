import requests
import sys

def stringToucher(lestring):
    global x 
    x = lestring

    return x

"""
 Va utiliser la valeur de la journée entrer dans le lineedit pour avoir différent champs utilisé dans l'application
Puis sélectionne les images nécessaires. 
"""

def meteoallo(value):
    
    urlsjour = requests.get(
        'https://api.weather.com/v3/wx/forecast/daily/5day?geocode=46.05,-71.96&format=json&units=m&language=fr-CA&apiKey=21553e0235304f40953e0235300f4055').json()
    search_day = value
    search_day_number = 0
    day_number_part = search_day_number

    dayInWeek = len(urlsjour["dayOfWeek"])
    for day in range(dayInWeek):
        if urlsjour["dayOfWeek"][day] == value:
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

    ulrsmaintenant = requests.get(
        'https://api.weather.com/v2/pws/observations/current?stationId=IVICTORI1625&format=json&units=m&apiKey=21553e0235304f40953e0235300f4055').json()

    string_maintenant = ""
    string_maintenant = str(ulrsmaintenant["observations"][0]["metric"]["temp"])

    #######################################################################################################################################################
    #######################################################################################################################################################
    #######################################################################################################################################################


    image_jour = (urlsjour["daypart"][0]["wxPhraseLong"][0])
    img = ""

    if image_jour == "Pluie / Neige" and ulrsmaintenant["observations"][0]["metric"]["temp"] < 0:
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
    elif image_jour == "Pluie / Neige" and ulrsmaintenant["observations"][0]["metric"]["temp"] > 0:
        img = "Pluie.png"
    elif image_jour == "Précipitations hivernales":
        img = "Neige.png"
    elif image_jour == "Pluie verglaçante devenant neige":
        img = "Pluie.png"
    elif image_jour == "Plutôt ensoleillé":
        img = "Soleil.png"
    elif image_jour == 'Légères chutes de neige':
        img = "Neige.png"


    image_prévision = (urlsjour["daypart"][0]["wxPhraseLong"][day_number_part])
    img_prévision = ""

    if image_prévision == "Pluie / Neige" and ulrsmaintenant["observations"][0]["metric"]["temp"] < 0:
        img_prévision = "Neige.png"
    elif image_prévision == "Chutes de neige":
        img_prévision = "Neige.png"
    elif image_prévision == "Peu nuageux":
        img_prévision = "Nuage.png"
    elif image_prévision == "Plutôt ensoleillé":
        img_prévision = "Soleil.png"
    elif image_prévision == "Ensoleillé":
        img_prévision = "Soleil.png"
    elif image_prévision == "Nuageux":
        img_prévision = "Nuage.png"
    elif image_prévision == "Chutes de neige dans l’après-midi":
        img_prévision = "Neige.png"
    elif image_prévision == "Chutes de neige dans la matinée":
        img_prévision = "Neige.png"
    elif image_prévision == "Pluie / Neige" and ulrsmaintenant["observations"][0]["metric"]["temp"] > 0:
        img_prévision = "Pluie.png"
    elif image_prévision == "Précipitations hivernales":
        img_prévision = "Neige.png"
    elif image_jour == 'Légères chutes de neige':
        img = "Neige.png"


    retourne_value = [string_maintenant,urlsjour["narrative"][search_day_number],ulrsmaintenant["observations"][0]["metric"],img_prévision,img,search_day,search_day_number,day_number_part]
    return retourne_value
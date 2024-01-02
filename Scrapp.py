import requests
import json
import time

def Scrapp(keyword):
    url = "https://vinted3.p.rapidapi.com/getSearch"

    querystring = {"country": "fr", "page": "1", "order": "newest_first", "keyword": keyword}

    headers = {
        "X-RapidAPI-Key": "5a22e8e6d5mshcd4ee045b787ecdp1b121ejsnb37ffe9b63a4",
        "X-RapidAPI-Host": "vinted3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = []

    for articles in response.json():
        titre = articles['title']
        image = articles['image']
        taille = articles['size']
        prix = articles['price']["totalAmount"]
        url = articles['url']
        seller = articles['seller']['username']
        result.append({"titre": titre, "image": image, "taille": taille, "prix": prix, "url": url, "seller": seller})

    return result

with open("filtres.json", 'r') as fichier:
    data = json.load(fichier)

Nike = data['filtres']['filtres1']
Addidas = data['filtres']['filtres2']
Ralph = data['filtres']['filtres3']
Lacoste = data['filtres']['filtres4']
Jordan = data['filtres']['filtres5']

filtres = [Nike, Addidas, Ralph, Lacoste, Jordan]

for i, filtre in enumerate(filtres):
    items = Scrapp(filtre)

    for item in items:
        titre = item['titre']
        image = item['image']
        taille = item['taille']
        if taille:
            taille = taille
        else:
            taille = "Aucune Taille"
        prix = item['prix']
        url = item['url']
        seler = item['seller']
        with open(f"Seler_0.txt", "w+", encoding="utf-8") as f:
            f.write(seler + "\n")
        with open(f"Tire_0.txt", "w+", encoding="utf-8") as f:
            f.write(titre + "\n")
        with open(f"Image_0.txt", "w+", encoding="utf-8") as f:
            f.write(image + "\n")
        with open(f"Taille_0.txt", "w+", encoding="utf-8") as f:
            f.write(taille + "\n")
        with open(f"Prix_0.txt", "w+", encoding="utf-8") as f:
            f.write(str(prix) + "\n")
        with open(f"Url_0.txt", "w+", encoding="utf-8") as f:
            f.write(url + "\n")

        time.sleep(10)

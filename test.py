import markdown
import requests

def trad(id):
    states={}
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    statistique = response.json()
    if len(statistique["types"])==1:
        for elt in statistique["types"]:
            states["type"]=elt["type"] #ça affiche que 1 des deux types si y'en a 2
            response=requests.get(states["type"]["url"])
            traduction= response.json()
        for elt in traduction["names"]:
            if elt["language"]["name"] == "fr":
                states["typenom"] = (elt["name"])
    else:
        states["type"] = [elt["type"] for elt in statistique["types"]]
    return states



print(trad(50))
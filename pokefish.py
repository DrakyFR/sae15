import markdown
import requests
import argparse
import webbrowser

parser = argparse.ArgumentParser()
parser.add_argument("ID", help="Entrez l'ID d'un pokémon", type=int)
args = parser.parse_args()

# Faire une requête à l'API Pokémon pour obtenir les données de Pikachu

response = requests.get("https://pokeapi.co/api/v2/pokemon/")
data = response.json()

def download_poke(id:int)->dict:
    states={}
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    statistique = response.json()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{id}")
    form = response.json()
    image = form["sprites"]
    states["nom"]=requests.get(statistique["species"]["url"]).json()["names"][4]["name"]
    states["height"]=statistique["height"]
    states["weight"]=statistique["weight"]

    nb=1
    for elt in statistique["types"]:
        states["type "+str(nb)]=requests.get(elt["type"]["url"]).json()["names"][3]["name"]
        nb+=1

    for elt in statistique["stats"]:
        if elt["stat"]["name"] == "hp":
            states["hp"]=elt["base_stat"]
        elif elt["stat"]["name"] == "attack":
            states["attack"]=elt["base_stat"]
        elif elt["stat"]["name"] == "defense":
            states["defense"]=elt["base_stat"]
        elif elt["stat"]["name"] == "special-attack":
            states["special-attack"]=elt["base_stat"]
        elif elt["stat"]["name"] == "special-defense":
            states["special-defense"]=elt["base_stat"]
        elif elt["stat"]["name"] == "speed":
            states["speed"]=elt["base_stat"]
    url=image["front_default"]
    states["image"]=url
    return states     



def poke_to_md(download_poke):
    with open("mon_fichier.md", "w") as mon_pokedex:
        #Il faut créer un fichier marldown "mon_fichier"
        mon_pokedex.write("# Presentation de "+str(download_poke["nom"]))
        mon_pokedex.write("\n### - Point de vitesse : "+str(download_poke["hp"]))
        mon_pokedex.write("\n### - Point d'attaque : "+str(download_poke["attack"]))
        mon_pokedex.write("\n### - Point de defense : "+str(download_poke["defense"]))
        mon_pokedex.write("\n### - Point d'attaque special : "+str(download_poke["special-attack"]))
        mon_pokedex.write("\n### - Point de defense special : "+str(download_poke["special-defense"]))
        mon_pokedex.write("\n### - Point de vitesse : "+str(download_poke["speed"]))
        mon_pokedex.write("\n### - Type 1 : "+str(download_poke["type 1"]))
        if 'type 2' in download_poke:
            mon_pokedex.write("\n### - Type 2 : "+str(download_poke["type 2"]))
        mon_pokedex.write("\n### - taille : "+str(download_poke["height"]))
        mon_pokedex.write("\n### - Poids : "+str(download_poke["weight"]))
        
        mon_pokedex.write("\n ![alt text]("+download_poke["image"]+")")
    with open("mon_fichier.md", "r") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    with open("some_file.html","w") as pokedex_html:
        pokedex_html.write(html)
        
# Il faut créer les fichiers "mon_fichier.md" et "some_file.html"


poke_to_md(download_poke(args.ID))


webbrowser.open("some_file.html")

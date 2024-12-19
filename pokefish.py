import markdown
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ID", help="Entrez l'ID d'un pokémon", type=int)
args = parser.parse_args()

# Faire une requête à l'API Pokémon pour obtenir les données de Pikachu

response = requests.get("https://pokeapi.co/api/v2/pokemon/")
data = response.json()

def pokemon(id):
    states={}
    resultat=""
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    statistique = response.json()
    name=statistique["name"]
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{id}")
    form = response.json()
    image = form["sprites"]
    nom="statistique of",name
    states["nom"]=statistique["name"]
    states["height"]=statistique["height"]
    states["weight"]=statistique["weight"]
    nb=1
    for elt in statistique["types"]:
        states["type "+str(nb)]=elt["type"]["name"]
        nb=nb+1
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



def markdowne(pokemon):
    with open("mon_fichier.md", "w") as mon_pokedex:
        #Il faut créer un fichier marldown "mon_fichier"
        mon_pokedex.write("# Presentation de "+str(pokemon["nom"]))
        mon_pokedex.write("\n ### - Point d'attaque : "+str(pokemon["attack"]))
        mon_pokedex.write("\n ### - Point de defense : "+str(pokemon["defense"]))
        mon_pokedex.write("\n ### - Point d'attaque special : "+str(pokemon["special-attack"]))
        mon_pokedex.write("\n ### - Point de defense special : "+str(pokemon["special-defense"]))
        mon_pokedex.write("\n ### - Point de vitesse : "+str(pokemon["speed"]))
        mon_pokedex.write("\n ![alt text]("+pokemon["image"]+")")
    with open("mon_fichier.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    with open("some_file.html","w") as pokedex_html:
        pokedex_html.write(html)
        




print(markdowne(pokemon(args.ID)))
print(pokemon(25))

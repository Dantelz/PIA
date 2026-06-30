import json
import hash_map
import time
from classpokemon import Pokemon

with open("el verdadero\\pokemon_data.json", "r", encoding="utf-8") as f:
    pokemondata = json.load(f)

def menu_pokedex():
    while True:
        
        pokedex = hash_map.HashMap()
        for i in pokemondata:
            hash = pokedex.hash(i["id"]) 
            pokedex.agregar(i["id"], i["nombre"])

        time.sleep(1.3)
        print("1 >>> Ver Pokedex")
        print("2 >>> Buscar Pokemon")
        print("3 >>> Volver al menu principal")

        try:
                op = int(input("Que necesitas: "))
        except ValueError:
                print("Error, por favor ingresar un numero")
                continue 

        if op == 1:
            pokedex.mostrar()

        elif op == 2:
            id_buscado = int(input("Ingrese ID del Pokémon que queres capturar: "))

            for p in pokemondata:
                if p["id"] == id_buscado:
                    pokemon_buscado = Pokemon(
                        p["id"],
                        p["nombre"],
                        p["tipo"],
                        p["poder_combate"]
                    )
                    break
            
            if pokemon_buscado.id not in range(1, 152):
                print("No existe un Pokémon con ese ID")
                return
            
            else:
                 print(f"Este es el pokemon de ID {id_buscado}")
                 print({pokemon_buscado})

        elif op == 3:
            break
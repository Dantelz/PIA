import json
import hash_map
import time
from classpokemon import Pokemon
import os

with open("el verdadero\\pokemon_data.json", "r", encoding="utf-8") as f:
    pokemondata = json.load(f)

def espera():
    while True:
        esp=input("\nPara volver al menu presione enter: ")
        if esp=="":
            break

def menu_pokedex():
    while True:
        
        pokedex = hash_map.HashMap()
        for i in pokemondata:
            hash = pokedex.hash(i["id"]) 
            pokedex.agregar(i["id"], i["nombre"])

        time.sleep(1.3)
        os.system("cls")
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
            espera()

        elif op == 2:
            try:
                id_buscado = int(input("Ingrese ID del Pokemon que queres buscar: "))
            except ValueError:
                print("Ingresa un numero")
                continue

            resultado = busqueda_binaria(pokemondata, id_buscado)

            if resultado is None:
                print("No existe un Pokemon con ese ID")

            else:
                pokemon_buscado = Pokemon(
                    resultado["id"],
                    resultado["nombre"],
                    resultado["tipo"],
                    resultado["poder_combate"]
                )

                print(f"Este es el pokemon de ID {id_buscado}")
                print(f"{pokemon_buscado.nombre} | Tipo: {pokemon_buscado.tipo} | PC: {pokemon_buscado.poder_combate}")
                espera()

        elif op == 3:
            break

def busqueda_binaria(lista, id_buscado):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        pokemon = lista[medio]

        if pokemon["id"] == id_buscado:
            return pokemon

        elif pokemon["id"] < id_buscado:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return 
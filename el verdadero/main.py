import os
import sys
import hash_map
import hash_set  
import json
from classpokemon import Pokemon
from gyms import set_medals, select_gym, start_medals
from teamandpc import mostrar_equipo, menu_pc, equipo, buscar_pokemon
from captura import capturar_pokemon
from medico import centro_pokemon
from pokedexmenu import menu_pokedex
import time

with open("el verdadero\\medallas.json", "r", encoding="utf-8") as f:
    medallas = json.load(f)

with open("el verdadero\\pokemon_data.json", "r", encoding="utf-8") as f:
    pokemondata = json.load(f)

def main():
    os.system("cls")
    print("Bienvenido al Verdadero Juego de Pokémon")
    starters()
    menu()

def espera():
    while True:
        esp=input("\nPara volver al menu presione enter: ")
        if esp=="":
            break

def menu():
    start_medals(medallas)

    
    while True:
        os.system("cls")

        print("1 >>> Pokédex")
        print("2 >>> Ver Equipo Principal")
        print("3 >>> PC")
        print("4 >>> Capturar nuevo Pokémon")
        print("5 >>> Ver Medallas")
        print("6 >>> Buscar Pokémon en Equipo/PC")
        print("7 >>> Enviar Pokémon al Centro Pokémon")
        print("8 >>> Transferir Pokémon al Profesor Oak")
        print("9 >>> Deshacer última transferencia")
        print("10 >>> Desafiar Líder de Gimnasio")
        print("11 >>> Salir del sistema")


        try:
                eleccion = int(input("Cual sera tu proximo movimiento: "))
        except ValueError:
                print("Error, por favor ingresar un numero")
                continue 
               
        if eleccion == 1:
            menu_pokedex()

        elif eleccion == 2:
            mostrar_equipo()

        elif eleccion == 3:
            menu_pc()

        elif eleccion == 4:
            capturar_pokemon(pokemondata)

        elif eleccion == 5:
            for medalla in medallas:
                if set_medals.buscar(medalla["nombre"]):
                    print(f"{medalla['id']} - {medalla['nombre']}")
                else:
                    print(f"{medalla['id']} - No obtenida")
            espera()
            
        elif eleccion == 6:
            buscar_pokemon()

        elif eleccion == 7:
            centro_pokemon()

        elif eleccion == 10:
            select_gym(medallas)
        
        elif eleccion == 11:
            print("Saliendo del sistema...Gracias por jugar")
            sys.exit()
        else:  
            print("No es una opcion")
            espera()

def starters():
    print("Elige tu Pokémon inicial:")
    print("Bulbasaur")
    print("Charmander")
    print("Squirtle")
    print("Mudkip")


    eleccion = input("Quien sera tu compañero para el resto de tu aventura: ")

    if eleccion.lower() == "bulbasaur":
        pokemon_inicial = Pokemon(1, "Bulbasaur", "Planta/Veneno", 318)
    elif eleccion.lower() == "charmander":
        pokemon_inicial = Pokemon(4, "Charmander", "Fuego", 314)
    elif eleccion.lower() == "squirtle":
        pokemon_inicial = Pokemon(7, "Squirtle", "Agua", 309)
    elif eleccion.lower() == "mudkip":
        pokemon_inicial = Pokemon(258, "Mudkip", "Agua", 320)
    else:
        print("No esta entre las opciones. Intenta de nuevo.")
        return starters()

    equipo.append(pokemon_inicial)
    print(f"Has elegido a {pokemon_inicial.nombre} como tu Pokémon inicial.")
    time.sleep(1)
    print("Configurando Panel de Elecciones...")
    time.sleep(1.5)

main()

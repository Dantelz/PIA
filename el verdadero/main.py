import os
import sys
import time
import hash_table
import hash_set  
import json
from modulo1 import Pokemon
from gyms import set_medals, select_gym, start_medals
from teamandpc import capturar_pokemon, mostrar_equipo, mostrar_pc


with open("el verdadero\\pokemon_data.json", "r") as f:
    pokemondata = json.load(f)

with open("el verdadero\\medallas.json", "r", encoding="utf-8") as f:
    medallas = json.load(f)


def main():
    os.system("cls")
    print("Bienvenido a el Verdadero Juego de Pokémon")
    time.sleep(2)
    menu()



def menu():
    start_medals(medallas)

    
    while True:
        time.sleep(0)
        instance = hash_table.hash_table()
        for i in pokemondata:
            hash = instance.function_hash(i["id"], i["nombre"]) 
            instance.insert(i["id"], i["nombre"])

        print("1 >>> Ver Pokédex")
        print("2 >>> Ver Equipo Principal")
        print("3 >>> Ver PC")
        print("4 >>> Capturar nuevo Pokémon")
        print("5 >>> Ver Medallas")
        print("6 >>> Buscar Pokémon en Equipo")
        print("7 >>> Enviar Pokémon al Centro Pokémon")
        print("8 >>> Transferir Pokémon al Profesor Oak")
        print("9 >>> Deshacer última transferencia")
        print("10 >>> Desafiar Líder de Gimnasio")
        print("11 >>> Salir del sistema")


        eleccion= int(input("Cual sera tu proximo movimiento: "))
        
        if eleccion == 1:
            for clave, valor in instance.table.items():
                print(f"{clave}: {valor}")

        elif eleccion == 2:
            mostrar_equipo()

        elif eleccion == 3:
            mostrar_pc()

        elif eleccion == 4:
            capturar_pokemon(pokemondata)

        elif eleccion == 5:
            for medalla in medallas:
                if set_medals.contains(medalla["nombre"]):
                    print(f"{medalla['id']} - {medalla['nombre']}")
                else:
                    print(f"{medalla['id']} - No obtenida")
        elif eleccion == 10:
            select_gym(medallas)
        
        elif eleccion == 11:
            print("Saliendo del sistema...Gracias por jugar")
            time.sleep(1)
            sys.exit()
        else:  
            print("No es una opcion")
            time.sleep(2)

menu()

    
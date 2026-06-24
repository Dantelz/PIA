import os
import sys
import time
import hash_table 
import json

with open("C:\\Users\\Usuario\\Downloads\\Zurlo\\PIA\\el verdadero\\pokemon_data.json", "r") as f:
    pokemondata = json.load(f)

def menu():
    while True:
        
        instance = hash_table.hash_table()
        for i in pokemondata:
            hash = instance.function_hash(i["id"], i["nombre"]) 
            instance.insert(i["id"], i["nombre"])
        

        print("1 >>> Ver Pokédex")
        print("2 >>> Ver Equipo Principal")
        print("3 >>> Ver PC")
        print("4 >>> Capturar nuevo Pokémon")
        print("5 >>> Ordenar PC")
        print("6 >>> Buscar Pokémon en Equipo")
        print("7 >>> Enviar Pokémon al Centro Pokémon")
        print("8 >>> Transferir Pokémon al Profesor Oak")
        print("9 >>> Deshacer última transferencia")
        print("10 >>> Desafiar Líder de Gimnasio")
        print("11 >>> Salir del sistema")


        eleccion= int(input("Ingrese la opcion que desea "))
        
        if eleccion == 1:
            print(instance.table)

        elif eleccion == 2:
            print("Gracias por jugar")
            time.sleep(2)
            return

        else:  
            print("Error! Ingreso incorrecto.")
            time.sleep(2)

menu()
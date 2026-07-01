import time
import os
from sorts import quick_sort_poder, selection_sort_tipo, bubble_sort_nombre


def espera():
    while True:
        esp=input("\nPara volver al menu presione enter: ")
        if esp=="":
            break

class Nodo:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.siguiente = None


class Llinkedlist:
    def __init__(self):
        self.head = None

    def agregar(self, pokemon):
        nuevo = Nodo(pokemon)

        if self.head is None:
            self.head = nuevo
            return

        actual = self.head
        while actual.siguiente: # si no existe otro pokemon frena el while
            actual = actual.siguiente

        actual.siguiente = nuevo

    def mostrar(self):
        actual = self.head

        if self.head is None:
            print("La PC está vacía")
            return

        while actual:
            Pkm = actual.pokemon
            print(f"{Pkm.id} - {Pkm.nombre} - {Pkm.tipo} - {Pkm.poder_combate}")
            actual = actual.siguiente

    def listapc(self):
        lista = []
        actual = self.head

        while actual:
            lista.append(actual.pokemon)
            actual = actual.siguiente

        return lista
    
    def buscar_nombre(self, nombre):
        actual = self.head

        while actual:
            if actual.pokemon.nombre.lower() == nombre.lower():
                return actual.pokemon
            actual = actual.siguiente

        return None

def menu_pc():
    while True:
        os.system("cls")
        print("1 >>> Ver PC")
        print("2 >>> Ordenar PC")
        print("3 >>> Volver al menu principal")

        try:
                op = int(input("Que necesitas: "))
        except ValueError:
                print("Error, por favor ingresar un numero")
                continue 

        if op == 1:
            mostrar_pc()
            espera()

        elif op == 2:
            ordenar_pc()

        elif op == 3:
            break


def ordenar_pc():
    while True:
        time.sleep(1.3)
        os.system("cls")
        print("1 >>> Orden alfabetico")
        print("2 >>> Orden por tipo")
        print("3 >>> Orden competitivo")
        print("4 >>> Volver")

        try:
                op = int(input("Que necesitas: "))
        except ValueError:
                print("Error, por favor ingresar un numero")
                continue 

        lista = pc.listapc()

        if op == 1:
            lista = bubble_sort_nombre(lista)
            for pokemon in lista:
                print(f"{pokemon.id} - {pokemon.nombre} - {pokemon.tipo} - {pokemon.poder_combate}")
            espera()

        elif op == 2:
            lista = selection_sort_tipo(lista)
            for pokemon in lista:
                print(f"{pokemon.id} - {pokemon.nombre} - {pokemon.tipo} - {pokemon.poder_combate}")
            espera()

        elif op == 3:
            lista = quick_sort_poder(lista)
            for pokemon in lista:
                print(f"{pokemon.id} - {pokemon.nombre} - {pokemon.tipo} - {pokemon.poder_combate}")
            espera()

        elif op == 4:
            break


equipo = []
pc = Llinkedlist()

def mostrar_equipo():
    if len(equipo) == 0:
        print("El equipo esta vacio")
        return
    else:
        for pokemon in equipo:
            print(f"{pokemon.id} - {pokemon.nombre} - {pokemon.tipo} - {pokemon.poder_combate}")


def mostrar_pc():
    pc.mostrar()


def buscar_pokemon():
    nombre_pokemon = input("Ingrese Nombre del Pokemon: ")
    print("Buscando estre sus Pokemomes...")

    for pokemon in equipo:
        if pokemon.nombre.lower() == nombre_pokemon.lower():
            time.sleep(1)
            print("Ese Pokemon esta en el equipo titular")
            print(f"{pokemon.nombre} | {pokemon.tipo} | {pokemon.poder_combate}")
            espera()
            return
        
    pokemon_pc = pc.buscar_nombre(nombre_pokemon)

    if pokemon_pc:
        time.sleep(1)
        print("Ese Pokemon esta en la PC")
        print(f"{pokemon_pc.nombre} | {pokemon_pc.tipo} | {pokemon_pc.poder_combate}")
    else:
        time.sleep(1)
        print("Ese Pokemon no fue encontrado ni en el Equipo ni en la PC")
    
    espera()
from modulo1 import Pokemon
import time

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
        while actual.siguiente:
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

equipo = []
pc = Llinkedlist()


def capturar_pokemon(pokemondata):
    id_buscado = int(input("Ingrese ID del Pokémon a capturar: "))

    for p in pokemondata:
        if p["id"] == id_buscado:
            pokemon_encontrado = Pokemon(
                p["id"],
                p["nombre"],
                p["tipo"],
                p["poder_combate"]
            )
            break

    if pokemon_encontrado.id > 151:
        print("No existe un Pokémon con ese ID")
        return

    if len(equipo) < 6:
        equipo.append(pokemon_encontrado)
        print(f"{pokemon_encontrado.nombre} fue agregado al equipo")
    else:
        pc.agregar(pokemon_encontrado)
        print(f"{pokemon_encontrado.nombre} fue enviado a la PC")


def mostrar_equipo():
    if len(equipo) == 0:
        print("El equipo esta vacio")
        return

    for pokemon in equipo:
        print(f"{pokemon.id} - {pokemon.nombre} - {pokemon.tipo} - {pokemon.poder_combate}")


def mostrar_pc():
    pc.mostrar()
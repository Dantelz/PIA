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
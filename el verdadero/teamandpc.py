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

    def listapc(self):
        lista = []
        actual = self.head

        while actual:
            lista.append(actual.pokemon)
            actual = actual.siguiente

        return lista

def menu_pc():
    while True:
        time.sleep(1.3)
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

        elif op == 2:
            ordenar_pc()

        elif op == 3:
            break

def bubble_sort_nombre(lista):
        n = len(lista)

        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j].nombre > lista[j + 1].nombre:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista

def selection_sort_tipo(lista):
    n = len(lista)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if lista[j].tipo < lista[min_idx].tipo:
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]

    return lista

def quick_sort_poder(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2].poder_combate

    mayores = [x for x in lista if x.poder_combate > pivot]
    iguales = [x for x in lista if x.poder_combate == pivot]
    menores = [x for x in lista if x.poder_combate < pivot]

    return quick_sort_poder(mayores) + iguales + quick_sort_poder(menores)


def ordenar_pc():
    while True:
        time.sleep(1.3)
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

        elif op == 2:
            lista = selection_sort_tipo(lista)
            for pokemon in lista:
                print(f"{pokemon.id} - {pokemon.nombre} - {pokemon.tipo} - {pokemon.poder_combate}")

        elif op == 3:
            lista = quick_sort_poder(lista)
            for pokemon in lista:
                print(f"{pokemon.id} - {pokemon.nombre} - {pokemon.tipo} - {pokemon.poder_combate}")

        elif op == 4:
            menu_pc()


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
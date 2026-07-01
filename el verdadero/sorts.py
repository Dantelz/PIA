def quick_sort_poder(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2].poder_combate

    mayores = [x for x in lista if x.poder_combate > pivot]
    iguales = [x for x in lista if x.poder_combate == pivot]
    menores = [x for x in lista if x.poder_combate < pivot]

    return quick_sort_poder(mayores) + iguales + quick_sort_poder(menores)

def selection_sort_tipo(lista):
    n = len(lista)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if lista[j].tipo < lista[min_idx].tipo:
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]

    return lista

def bubble_sort_nombre(lista):
        n = len(lista)

        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j].nombre > lista[j + 1].nombre:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista

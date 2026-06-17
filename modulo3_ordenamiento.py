# modulo3_ordenamiento.py
# Módulo 3: Algoritmos de Ordenamiento para la PC
#   - Bubble Sort   → por nombre (A-Z)
#   - Insertion Sort → por tipo (agrupado A-Z)
#   - Quick Sort    → por poder_combate (mayor a menor)

from modulo1_pokedex import Pokemon


# ─────────────────────────────────────────────────────────────────────────────
# Bubble Sort – Ordenar por nombre (A-Z)
# Complejidad: O(n²) promedio y peor caso
# ─────────────────────────────────────────────────────────────────────────────

def bubble_sort_por_nombre(lista: list[Pokemon]) -> list[Pokemon]:
    """
    Ordena una lista de Pokémon alfabéticamente por nombre (A→Z)
    usando Bubble Sort in-place.
    """
    n = len(lista)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if lista[j].nombre.lower() > lista[j + 1].nombre.lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:  # optimización: si no hubo intercambios, ya está ordenado
            break
    return lista


# ─────────────────────────────────────────────────────────────────────────────
# Insertion Sort – Ordenar por tipo (A-Z)
# Complejidad: O(n²) promedio y peor caso
# ─────────────────────────────────────────────────────────────────────────────

def insertion_sort_por_tipo(lista: list[Pokemon]) -> list[Pokemon]:
    """
    Ordena una lista de Pokémon por tipo (A→Z) usando Insertion Sort in-place.
    Pokémon del mismo tipo quedan agrupados.
    """
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j].tipo.lower() > clave.tipo.lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


# ─────────────────────────────────────────────────────────────────────────────
# Quick Sort – Ordenar por poder_combate (mayor a menor)
# Complejidad: O(n log n) promedio; O(n²) peor caso (lista ya ordenada + pivot malo)
# ─────────────────────────────────────────────────────────────────────────────

def quick_sort_por_pc(lista: list[Pokemon], izq: int = 0, der: int = -1) -> list[Pokemon]:
    """
    Ordena una lista de Pokémon por poder_combate de mayor a menor
    usando Quick Sort in-place (recursivo).
    """
    if der == -1:
        der = len(lista) - 1

    if izq >= der:
        return lista

    pivot_idx = _particionar(lista, izq, der)
    quick_sort_por_pc(lista, izq, pivot_idx - 1)
    quick_sort_por_pc(lista, pivot_idx + 1, der)
    return lista


def _particionar(lista: list[Pokemon], izq: int, der: int) -> int:
    """
    Selecciona el último elemento como pivote y reorganiza la lista:
    elementos con PC > pivote quedan a la izquierda (orden descendente).
    """
    pivot = lista[der].poder_combate
    i = izq - 1
    for j in range(izq, der):
        if lista[j].poder_combate >= pivot:  # >= para orden descendente
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[der] = lista[der], lista[i + 1]
    return i + 1


# ─────────────────────────────────────────────────────────────────────────────
# Función utilitaria: mostrar lista ordenada
# ─────────────────────────────────────────────────────────────────────────────

def mostrar_lista(lista: list[Pokemon]) -> None:
    if not lista:
        print("  (Lista vacía)")
        return
    for i, p in enumerate(lista, 1):
        print(f"  [{i:>3}] {p}")

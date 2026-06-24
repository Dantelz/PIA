# modulo4_busquedas.py
# Módulo 4: Búsquedas
#   - Búsqueda Lineal: recorre el equipo principal por nombre
#   - Búsqueda Binaria: consulta la Pokédex por ID

from modulo1_pokedex import Pokemon, Pokedex


# ─────────────────────────────────────────────────────────────────────────────
# Búsqueda Lineal – Inspección del Equipo
# Complejidad: O(n)
# ─────────────────────────────────────────────────────────────────────────────

def busqueda_lineal_equipo(equipo: list[Pokemon], nombre: str) -> Pokemon | None:
    """
    Recorre el equipo lineal (array) buscando un Pokémon por nombre.
    Devuelve la instancia si la encuentra, o None si no está.
    Complejidad: O(n) – revisa hasta todos los elementos.
    """
    for pokemon in equipo:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    return None


# ─────────────────────────────────────────────────────────────────────────────
# Búsqueda Binaria – Consulta en Pokédex
# Complejidad: O(log n)
# ─────────────────────────────────────────────────────────────────────────────

def busqueda_binaria_pokedex(pokedex: Pokedex, id_buscado: int) -> Pokemon | None:
    """
    Realiza una búsqueda binaria sobre la lista de IDs ordenados de la Pokédex.
    Devuelve el Pokémon si lo encuentra, o None si el ID no existe.
    Complejidad: O(log n) – divide el espacio de búsqueda a la mitad en cada paso.
    """
    ids = pokedex.ids_ordenados()   # lista de IDs ya ordenados
    izq, der = 0, len(ids) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if ids[medio] == id_buscado:
            return pokedex.obtener(id_buscado)
        elif ids[medio] < id_buscado:
            izq = medio + 1
        else:
            der = medio - 1

    return None   # ID no encontrado

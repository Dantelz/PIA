

import os
import sys

from ej.modulo1_pokedex import Pokemon, Pokedex
from ej.modulo2_entrenador import Entrenador
from ej.modulo3_ordenamiento import (
    bubble_sort_por_nombre,
    insertion_sort_por_tipo,
    quick_sort_por_pc,
    mostrar_lista,
)
from ej.modulo4_busquedas import busqueda_lineal_equipo, busqueda_binaria_pokedex

ARCHIVO_JSON = os.path.join(os.path.dirname(__file__), "pokemon_data.json")

def limpiar() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def separador(char: str = "─", ancho: int = 54) -> None:
    print(char * ancho)


def pausar() -> None:
    input("\n  [Presioná ENTER para continuar]")


def pedir_nombre_pokemon(pokedex: Pokedex) -> Pokemon | None:
    """Permite capturar un Pokémon eligiéndolo de la Pokédex."""
    print("\n  ── Pokémon disponibles en la Pokédex ──")
    pokedex.mostrar()
    entrada = input("  Ingresá el ID del Pokémon a capturar (0 para cancelar): ").strip()
    if entrada == "0":
        return None
    if not entrada.isdigit():
        print("  ✗ ID inválido.")
        return None
    pokemon = pokedex.obtener(int(entrada))
    if pokemon is None:
        print(f"  ✗ No existe un Pokémon con ID {entrada} en la Pokédex.")
    return pokemon


def menu_ordenar_pc(entrenador: Entrenador) -> None:
    """Submenú para ordenar los Pokémon de la PC."""
    while True:
        print("\n  ── ORDENAR PC ──")
        print("  [1] Ordenar alfabéticamente (Bubble Sort)")
        print("  [2] Ordenar por tipo       (Insertion Sort)")
        print("  [3] Ordenar por PC         (Quick Sort – mayor a menor)")
        print("  [0] Volver")
        opcion = input("  > ").strip()

        if opcion == "0":
            break

        # Paso 1: copia temporal a lista de Python
        lista_temp = entrenador.pc.a_lista()

        if not lista_temp:
            print("  ✗ La PC está vacía, no hay nada que ordenar.")
            pausar()
            continue

        if opcion == "1":
            bubble_sort_por_nombre(lista_temp)
            print("\n  ✔ PC ordenada alfabéticamente:")
        elif opcion == "2":
            insertion_sort_por_tipo(lista_temp)
            print("\n  ✔ PC ordenada por tipo:")
        elif opcion == "3":
            quick_sort_por_pc(lista_temp)
            print("\n  ✔ PC ordenada por Poder de Combate (mayor → menor):")
        else:
            print("  ✗ Opción inválida.")
            continue

        mostrar_lista(lista_temp)

        # Paso 2: reconstruir la lista enlazada con el nuevo orden
        entrenador.pc.desde_lista(lista_temp)
        pausar()


def main() -> None:
    limpiar()
    separador("═", 90)

    nombre_entrenador = input("\n  ¡Bienvenido! ¿Cuál es tu nombre, entrenador? ").strip()
    if not nombre_entrenador:
        nombre_entrenador = "Ash"

    # ── Inicialización ─────────────────────────────────────────────────────
    pokedex = Pokedex()
    pokedex.cargar_desde_json(ARCHIVO_JSON)

    entrenador = Entrenador(nombre_entrenador)

    # Dar 3 Pokémon iniciales al entrenador (starters clásicos)
    for starter_id in [4, 7, 25]:  # Charmander, Squirtle, Pikachu
        starter = pokedex.obtener(starter_id)
        if starter:
            entrenador.capturar(starter)

    print(f"\n  ¡Hola, {nombre_entrenador}! Tu aventura en Huergo comienza ahora.")
    pausar()

    # ── Menú Principal ────────────────────────────────────────────────────
    OPCIONES = [
        "Ver Pokédex",
        "Ver Equipo Principal",
        "Ver PC",
        "Capturar nuevo Pokémon",
        "Ordenar PC",
        "Buscar Pokémon en Equipo",
        "Enviar Pokémon al Centro Pokémon",
        "Transferir Pokémon al Profesor Oak",
        "Deshacer última transferencia",
        "Desafiar Líder de Gimnasio",
        "Ver Medallas",
        "Salir del sistema",
    ]

    while True:
        limpiar()
        print(f"\n  ══ MENÚ PRINCIPAL ─ Entrenador: {entrenador.nombre} ══")
        separador()
        for i, op in enumerate(OPCIONES, 1):
            print(f"  [{i:>2}] {op}")
        separador()
        opcion = input("  Elegí una opción: ").strip()

        if not opcion.isdigit() or not (1 <= int(opcion) <= len(OPCIONES)):
            print("  ✗ Opción inválida.")
            pausar()
            continue

        opcion = int(opcion)

        # ── 1: Ver Pokédex ─────────────────────────────────────────────────
        if opcion == 1:
            pokedex.mostrar()
            pausar()

        # ── 2: Ver Equipo ──────────────────────────────────────────────────
        elif opcion == 2:
            entrenador.mostrar_equipo()
            pausar()

        # ── 3: Ver PC ──────────────────────────────────────────────────────
        elif opcion == 3:
            entrenador.mostrar_pc()
            pausar()

        # ── 4: Capturar Pokémon ────────────────────────────────────────────
        elif opcion == 4:
            pokemon = pedir_nombre_pokemon(pokedex)
            if pokemon:
                entrenador.capturar(pokemon)
            pausar()

        # ── 5: Ordenar PC ──────────────────────────────────────────────────
        elif opcion == 5:
            menu_ordenar_pc(entrenador)

        # ── 6: Buscar en Equipo ────────────────────────────────────────────
        elif opcion == 6:
            nombre = input("  Ingresá el nombre del Pokémon a buscar: ").strip()
            resultado = busqueda_lineal_equipo(entrenador.equipo, nombre)
            if resultado:
                print(f"  ✔ ¡{resultado.nombre} está en tu equipo!")
                print(f"     {resultado}")
            else:
                print(f"  ✗ '{nombre}' no se encuentra en tu equipo actual.")
            pausar()

        # ── 7: Centro Pokémon ──────────────────────────────────────────────
        elif opcion == 7:
            entrenador.enviar_al_centro()
            pausar()

        # ── 8: Transferir al Prof. Oak ─────────────────────────────────────
        elif opcion == 8:
            entrenador.mostrar_pc()
            if entrenador.pc.esta_vacia():
                pausar()
                continue
            nombre = input("  Ingresá el nombre del Pokémon a transferir: ").strip()
            entrenador.transferir_a_oak(nombre)
            pausar()

        # ── 9: Deshacer transferencia ──────────────────────────────────────
        elif opcion == 9:
            entrenador.pila_transferencias.mostrar()
            entrenador.deshacer_transferencia()
            pausar()

        # ── 10: Desafiar Gimnasio ──────────────────────────────────────────
        elif opcion == 10:
            entrenador.desafiar_gimnasio()
            pausar()

        # ── 11: Ver Medallas ───────────────────────────────────────────────
        elif opcion == 11:
            entrenador.mostrar_medallas()
            pausar()

        # ── 12: Salir ──────────────────────────────────────────────────────
        elif opcion == 12:
            print(f"\n  ¡Hasta pronto, {entrenador.nombre}! ¡Seguí atrapándolos a todos!")
            separador("═", 54)
            sys.exit(0)


if __name__ == "__main__":
    main()

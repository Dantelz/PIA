import time
from teamandpc import equipo

def centro_pokemon():
    if len(equipo) == 0:
        print("No tenes pokemon en tu equipo")
        return

    print("Que pokemon queres mandar al Centro Pokemon?")
    
    for i, pokemon in enumerate(equipo):
        print(f"{i + 1} - {pokemon.nombre}")

    try:
        opcion = int(input("Elegi un pokemon: "))
    except ValueError:
        print("Tenes que ingresar un numero")
        return

    if opcion < 1 or opcion > len(equipo):
        print("Opcion invalida")
        return

    pokemon = equipo[opcion - 1]

    print(f"{pokemon.nombre} esta siendo curado...")
    print("Espera su rehabilitacion...")
    
    time.sleep(1)

    print(f"Listo. El proceso de curacion de {pokemon.nombre} se completo con exito.")
    print(f"{pokemon.nombre} esta listo para combatir.")
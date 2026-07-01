from classpokemon import Pokemon
from teamandpc import equipo, pc
import time

def espera():
    while True:
        esp=input("\nPara volver al menu presione enter: ")
        if esp=="":
            break

def capturar_pokemon(pokemondata):
    id_buscado = int(input("Ingrese ID del Pokémon que queres capturar: "))

    for p in pokemondata:
        if p["id"] == id_buscado:
            pokemon_encontrado = Pokemon(
                p["id"],
                p["nombre"],
                p["tipo"],
                p["poder_combate"]
            )
            break

    if id_buscado not in range(1, 152):
        print("No existe un Pokémon con ese ID")
        espera()
        return
    
    else:
        time.sleep(1)
        print(f"Ha aparecido un {pokemon_encontrado.nombre} salvaje (PC: {pokemon_encontrado.poder_combate})")
        time.sleep(1)
        print(f"Has capturado a {pokemon_encontrado.nombre}")

        if len(equipo) < 6:
            equipo.append(pokemon_encontrado)
            time.sleep(1)
            print(f"{pokemon_encontrado.nombre} fue agregado al equipo")
        else:
            pc.agregar(pokemon_encontrado)
            time.sleep(1)
            print(f"{pokemon_encontrado.nombre} fue enviado a la PC")
        
    espera()

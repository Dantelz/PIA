from classpokemon import Pokemon
from teamandpc import equipo, pc



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

    if pokemon_encontrado.id not in range(1, 152):
        print("No existe un Pokémon con ese ID")
        return
        
    if len(equipo) < 6:
        equipo.append(pokemon_encontrado)
        print(f"{pokemon_encontrado.nombre} fue agregado al equipo")
    else:
        pc.agregar(pokemon_encontrado)
        print(f"{pokemon_encontrado.nombre} fue enviado a la PC")

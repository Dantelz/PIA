import random
def battle(medal):
    print("¡Bienvenido a la batalla Pokémon!")
    ops = ["Ganaste", "Perdiste"]
    resultado = random.choice(ops)
    print(f"Resultado de la batalla: {resultado}")
    return resultado

def select_gym():
    id = int(input("Ingrese el ID del líder de gimnasio que desea desafiar (1-8): "))
    if id in range(1, 9):
        res = battle(id)
    else:
        print("invalido")
        select_gym()
    if res == "Ganaste":
        new_medal
    
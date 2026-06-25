import random
import hash_set
set_medals = hash_set.hash_set()

def battle():
    ops = ["Ganaste", "Perdiste","Ganaste", "Perdiste", "Ganaste", "Perdiste", "Ganaste"]
    return random.choice(ops)

def select_gym(medallas):
    id = int(input("Ingrese ID del gimnasio (1-8): "))

    if id not in range(1, 9):
        print("id inválido")
        return

    medal = medallas[id - 1]
    medal_name = medal["nombre"]

    if set_medals.contains(medal_name):
        print(f"Ya tenés la {medal_name}")
        return

    resultado = battle()
    print(resultado)

    if resultado == "Ganaste":
        set_medals.insert(medal_name)
        print(f"Ganaste la {medal_name}")
    else:
        print("Perdiste")

def start_medals(medallas):
    cant = 0
    while cant < 2:
        id = random.randint(1,8)
        medal = medallas[id - 1]
        medal_name = medal["nombre"]
        if set_medals.contains(medal_name):
            print(f"Ya tenés la {medal_name}")
        else:
            set_medals.insert(medal_name)
            cant += 1
    return
import random
import hash_set
import time
set_medals = hash_set.HashSet()

def battle():
    ops = ["Ganaste", "Perdiste","Ganaste", "Perdiste", "Ganaste", "Perdiste", "Ganaste"]
    return random.choice(ops)

def select_gym(medallas):
    id = int(input("Ingrese ID del gimnasio: "))

    if id not in range(1, 9):
        print("id inválido")
        return

    medal = medallas[id - 1]
    medal_name = medal["nombre"]

    if set_medals.buscar(medal_name):
        print(f"Ya tenés la {medal_name}")
        return

    resultado = battle()
    time.sleep(1)
    print(resultado)

    if resultado == "Ganaste":
        set_medals.agregar(medal_name)
        time.sleep(1)
        print(f"Ganaste la {medal_name}")
    else:
        time.sleep(1)
        print("Perdiste")

def start_medals(medallas):
    cant = 0
    while cant < 2:
        id = random.randint(1,8)
        medal = medallas[id - 1]
        medal_name = medal["nombre"]
        if set_medals.buscar(medal_name):
            print(f"Ya tenés la {medal_name}")
        else:
            set_medals.agregar(medal_name)
            cant += 1
    return
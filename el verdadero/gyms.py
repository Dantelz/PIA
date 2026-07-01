import random
import hash_set
import time
set_medals = hash_set.HashSet()

def espera():
    while True:
        esp=input("\nPara volver al menu presione enter: ")
        if esp=="":
            break

def battle():
    ops = ["Ganaste", "Perdiste","Ganaste", "Perdiste", "Ganaste", "Perdiste", "Ganaste"]
    return random.choice(ops)

def select_gym(medallas):
    id = int(input("1 >>> Gimnasio Roca - Brock 🧱"
                    "2 >>> Gimnasio Agua - Misty 💧"
                    "3 >>> Gimnasio Electrico - Lt. Surge ⚡"
                    "4 >>> Gimnasio Planta - Erika 🌿"
                    "5 >>> Gimnasio Veneno - Koga ☠️"
                    "6 >>> Gimnasio Psiquico - Sabrina 🔮"
                    "7 >>> Gimnasio Fuego - Blaine 🔥"
                    "8 >>> Gimnasio Tierra - Giovanni 🌎"
                    "Ingrese ID del gimnasio contra el que desea luchar: "))

    if id not in range(1, 9):
        print("id invalido")
        return

    medal = medallas[id - 1]
    medal_name = medal["nombre"]

    if set_medals.buscar(medal_name):
        print(f"Ya tenes la {medal_name}")
        return

    resultado = battle()
    print(resultado)

    if resultado == "Ganaste":
        print(f"Has derrotado al lider, Conseguiste la {medal_name}")
        set_medals.agregar(medal_name)
    else:
        print("Has sido derrotado por el lider, mejor suerte la proxima")
    espera()

def start_medals(medallas):
    cant = 0
    while cant < 2:
        id = random.randint(1,8)
        medal = medallas[id - 1]
        medal_name = medal["nombre"]
        if set_medals.buscar(medal_name):
            print(f"Ya tenes la {medal_name}")
        else:
            set_medals.agregar(medal_name)
            cant += 1
    return
from queuestack import Stack
from teamandpc import equipo, pc
import time

stack_transfers = Stack()

def espera():
    while True:
        esp=input("\nPara volver al menu presione enter: ")
        if esp=="":
            break

def menu_transfers():
    while True:
        print("1 >>> Transferir Pokemon")
        print("2 >>> Deshacer ultima transferencia")
        print("3 >>> Volver")

        try:
            op = int(input("Que necesitas: "))
        except ValueError:
            print("Ingresa un numero")
            continue

        if op == 1:
            transferir()

        elif op == 2:
            deshacer_transferencia()

        elif op == 3:
            break

def transferir():
    if len(equipo) == 1:
        print("No tenes suficientes pokemones en tu equipo para transferir")
        return

    elif len(equipo) == 0:
        print("No tenes ningun pokemon en tu equipo")
        return

    print("Pokemones en tu equipo:")
    for i, pokemon_transfer in enumerate(equipo):
        print(f"{i + 1} - {pokemon_transfer.nombre}")

    try:
        op = int(input("Que pokemon queres transferir: "))
    except ValueError:
        print("Ingresa un numero")
        return

    if op < 1 or op > len(equipo):
        print("Opcion invalida")
        return

    pokemon_transfer = equipo.pop(op - 1)
    stack_transfers.push(pokemon_transfer)

    print(f"tranfiriendo a {pokemon_transfer.nombre} al Profesor Oak...")
    time.sleep(1.5)
    print(f"{pokemon_transfer.nombre} fue transferido al Profesor Oak")
    espera()

def deshacer_transferencia():
    ultimo = stack_transfers.peek()

    if ultimo is None:
        print("No hay transferencias para deshacer")
        return

    print(f"Ultimo pokemon transferido: {ultimo.nombre}")

    try:
        op = input("Queres recuperarlo? (1>>>Si/2>>>No): ")
    except ValueError:
        print("Ingresar un numero")
        return

    if op != "1" and op != "2":
        print("Opcion invalida")

    if op == "1":
        pokemon_transfer = stack_transfers.pop()
        if len(equipo) < 6:
            equipo.append(pokemon_transfer)
            print(f"Deshaciendo transferencia, Recuperando a {pokemon_transfer.nombre}...")
            time.sleep(1.5)
            print(f"{pokemon_transfer.nombre} fue Recuperado y agregado al Equipo Titular")
        else:
            pc.agregar(pokemon_transfer)
            print(f"Deshaciendo transferencia, Recuperando a {pokemon_transfer.nombre}...")
            time.sleep(1)
            print(f"{pokemon_transfer.nombre} fue Recuperado y agregado al PC")
        espera()
    
    if op == "2":
        print("No se recupero el pokemon")
        espera()

    
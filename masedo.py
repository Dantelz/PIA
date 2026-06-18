import random, os, time
#Ciclo para que se hagan peleas hasta que muera: para eso usamos personaje

personaje = {}

mago = {'nombre':'Mago',
        'vida':400,
        'atk':200,
        'enrg':100,
        'max_enrg':100,
        'max_vida':400,
        'chance_crit': 9,
        'crit_mult': 1.5,

        'habilidad_1':{
        'nombre': 'Voidstrike',
        'atk':300,
        'gastoenrg':50
        }
    }
guerrero = {'nombre':'Guerrero',
        'vida':600,
        'atk':100,
        'enrg':100,
        'max_enrg':100,
        'max_vida':600,
        'chance_crit': 9,
        'crit_mult': 1.5,

        'habilidad_1':{
        'nombre': 'Mirrorshield',
        'atk': 300 ,
        'gastoenrg':50
        }
    }
mafioso = {'nombre':'Mafioso',
        'vida':500,
        'atk':135,
        'enrg':100,
        'max_enrg':100,
        'max_vida':500,
        'chance_crit': 9,
        'crit_mult': 1.5,

        'habilidad_1':{
        'nombre': 'Lifesteal',
        'atk': 250,
        'gastoenrg':50
        }
    }

roles = [mago, guerrero, mafioso]
monstruo = {}

dragon = {'nombre':'Dragon',
            'vida':700,
            'atk':100 + random.randint(40,120),
            'chance_crit':9,
            'crit_mult': 1.5}
orco = {'nombre':'Orco',
            'vida':850,
            'atk':100 + random.randint(20,80),
            'chance_crit':9,
            'crit_mult': 1.5}
minotauro = {'nombre':'Minotauro',
            'vida':800,
            'atk':100 + random.randint(35,110),
            'chance_crit':9,
            'crit_mult': 1.5}
hydra =  {'nombre':'Hydra',
            'vida':900,
            'atk':100 + random.randint(30,100),
            'chance_crit':9,
            'crit_mult': 1.5}
ciclope =  {'nombre':'Ciclope',
            'vida':900,
            'atk':100 + random.randint(20,80),
            'chance_crit':9,
            'crit_mult': 1.5}
kraken =  {'nombre':'Kraken',
            'vida':950,
            'atk':100 + random.randint(30,100),
            'chance_crit':9,
            'crit_mult': 1.5}
quimera =  {'nombre':'Quimera',
            'vida':700,
            'atk':100 + random.randint(40,120),
            'chance_crit':9,
            'crit_mult': 1.5}
monstruos = [dragon, orco, minotauro, hydra, ciclope, kraken, quimera]

def menu():
    while True:
        os.system("cls")
        print("1) Jugar")
        print("2) Salir")

        eleccion= int(input("Ingrese la opcion que desea "))
        
        if eleccion == 1:
            jugar()

        elif eleccion == 2:
            print("Gracias por jugar")
            time.sleep(2)
            return

        else:  
            print("Error! Ingreso incorrecto.")
            time.sleep(2)

def intro_1():
    print()

def jugar():
    # Defino personaje
    crear_personaje()
    
    # Presento la escena / pelea
    intro_1()

    # Definir monstruo
    while personaje["vida"] > 0:
        personaje['vida'] = personaje['max_vida']
        personaje['enrg'] = personaje['max_enrg']
        crear_monstruo()
        empezar_pelea()
    else:
        print('perdiste')

def atacar():
    
    ataque = menu_ataque()
    atacado = False
    # Calculo de daño
    while not atacado:
        if ataque == 1:
            print(f"{personaje['nombre']} se prepara para golpear a {monstruo['nombre']}")
            time.sleep(1)
            #ejecutamos el ataque normal
            daño_base = personaje['atk']
            if random.randint(1,100) < personaje['chance_crit']:
                daño_total = daño_base * personaje['crit_mult']
                print(f"{personaje['nombre']} impactó en {monstruo['nombre']} causando {daño_total} puntos de daño CRITICO!")
            else:
                daño_total = daño_base
                print(f"{personaje['nombre']} impactó en {monstruo['nombre']} causando {daño_total} puntos de atk.")
            atacado = True
        elif ataque == 2:
                if personaje['enrg'] >= personaje["habilidad_1"]["gastoenrg"]:
                    print (f"{personaje['nombre']} esta apunto de usar su habilidad especial")
                    time.sleep(1)
                    personaje['enrg'] -= personaje['habilidad_1']["gastoenrg"]
                    print (f"este ataque le bajo 50 de energia, le quedan {personaje['enrg']}")
                    daño_total = personaje['habilidad_1']['atk']
                    atacado = True
                else: 
                    print(f"No valido energia: {personaje['enrg']}")
                    return atacar()
    
    time.sleep(2)
    
    # Restar vida
    monstruo['vida'] -= daño_total
    if monstruo['vida'] < 0:
        monstruo['vida'] = 0
        time.sleep(1)
    print(f"{monstruo['nombre']} quedó en {monstruo['vida']} puntos de vida.")
    time.sleep(1)


def atacar_ia():
    print('Te atacan!')
    time.sleep(1.5)
    print(f"Te hace {monstruo['atk']} de daño")
    personaje['vida'] -= monstruo['atk']
    time.sleep(2)
    print(f"Te quedan {personaje['vida']}")


def jugar_turno_ia():
    print(f"Turno de: {monstruo['nombre']}")
    time.sleep(1)
    print(f"el monstruo esta listo para atacar")
    atacar_ia()

def jugar_turno():
    # Mostrar stats
    print(f"Turno de: {personaje['nombre']}")
    time.sleep(1)
    print(f"Vida: {personaje['vida']}")
    print(f"Energia: {personaje['enrg']}")

    # Mostrar menu de acciones
    atacar()
    

def empezar_pelea():
    os.system("cls")
    print(f"El combate entre {personaje['nombre']} y {monstruo['nombre']} está por comenzar!")

    while personaje['vida'] > 0 and monstruo['vida'] > 0:
    # Jugar turno del personaje
        jugar_turno()
    # Jugar turno del monstru
        if monstruo['vida'] > 0:
            jugar_turno_ia()

    


def crear_monstruo():
    global monstruos
    global monstruo
    monstruo_elegido = random.choice(monstruos)
    monstruo = monstruo_elegido
    monstruos.remove(monstruo_elegido)

def mostrar_lista(lista):
    for num, elemento in enumerate(lista, 1):
        print(f"{num}- {elemento['nombre']}")

def crear_personaje():
    global personaje
    global roles

    # Actualizar mi personaje: NOMBRE
    nombre = input('Ingrese su nombre de usuario ')
    

    print(); time.sleep(1)

    # Actualizar mi personaje: ROL
    while True:
        mostrar_lista(roles)
        eleccion = input("Ingrese opcion deseada: ")
        
        if eleccion == "1":
            personaje = mago.copy()
            personaje.update({"rol": "mago"})
            personaje.update({"nombre": nombre })
            return
        elif eleccion == "2":
            personaje = guerrero.copy()
            personaje.update({"rol": "guerrero"})
            personaje.update({"nombre": nombre })
            return
        elif eleccion == "3":
            personaje = mafioso.copy()
            personaje.update({"rol": "mafioso"})
            personaje.update({"nombre": nombre })
            return
        else:
            print("Error! Ingreso invalido")
            time.sleep(2)

def menu_ataque():
    while True:
        print ("estas son tus opciones para atacar")
        time.sleep(1)
        print (f"1. Ataque normal hace {personaje['atk']} puntos de daño")
        time.sleep(1)
        print (f"2. Ataque especial {personaje['habilidad_1']['nombre']}")
        print ("hace",personaje['habilidad_1']['atk'],"puntos de daño")
        print ("gasta",personaje['habilidad_1']['gastoenrg'],"puntos de energia")
        time.sleep(1)
        ataque = int(input('ingrese el nombre de la opcion con la que quiere atacar '))
        if ataque in [1,2]:
            break
        else:
            print('Opcion invalida')
    return ataque



menu() 
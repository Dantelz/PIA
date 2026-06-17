# modulo2_entrenador.py
# Módulo 2: Gestión del Entrenador
#   - Equipo Principal (array/lista Python, máx 6)
#   - PC (Lista Enlazada Simple)
#   - Centro Pokémon (Queue)
#   - Deshacer Transferencia (Stack, máx 5)
#   - Desafío a Líder de Gimnasio

import random
import time
from modulo1_pokedex import Pokemon, RegistroMedallas

MAXIMO_EQUIPO = 6
MAXIMO_STACK_TRANSFERENCIAS = 5

# ─────────────────────────────────────────────────────────────────────────────
# Lista Enlazada Simple para la PC
# ─────────────────────────────────────────────────────────────────────────────

class Nodo:
    """Nodo de la Lista Enlazada Simple."""

    def __init__(self, pokemon: Pokemon):
        self.pokemon: Pokemon = pokemon
        self.siguiente: "Nodo | None" = None


class ListaEnlazada:
    """
    Lista Enlazada Simple que representa las Cajas de la PC.
    Sin límite de espacio. Inserción al inicio en O(1).
    """

    def __init__(self):
        self.cabeza: Nodo | None = None
        self._tamaño: int = 0

    def insertar_al_inicio(self, pokemon: Pokemon) -> None:
        nuevo = Nodo(pokemon)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self._tamaño += 1

    def eliminar_por_nombre(self, nombre: str) -> Pokemon | None:
        """Elimina y devuelve el primer Pokémon con ese nombre."""
        anterior = None
        actual = self.cabeza
        while actual:
            if actual.pokemon.nombre.lower() == nombre.lower():
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                self._tamaño -= 1
                return actual.pokemon
            anterior = actual
            actual = actual.siguiente
        return None

    def a_lista(self) -> list[Pokemon]:
        """Convierte la lista enlazada a lista de Python (para ordenamientos)."""
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.pokemon)
            actual = actual.siguiente
        return resultado

    def desde_lista(self, lista: list[Pokemon]) -> None:
        """Reconstruye la lista enlazada desde una lista de Python."""
        self.cabeza = None
        self._tamaño = 0
        # Insertar en orden inverso para que el primero de la lista quede al inicio
        for pokemon in reversed(lista):
            self.insertar_al_inicio(pokemon)

    def mostrar(self) -> None:
        if not self.cabeza:
            print("  (PC vacía)")
            return
        actual = self.cabeza
        i = 1
        while actual:
            print(f"  [{i}] {actual.pokemon}")
            actual = actual.siguiente
            i += 1

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def __len__(self):
        return self._tamaño


# ─────────────────────────────────────────────────────────────────────────────
# Queue para el Centro Pokémon
# ─────────────────────────────────────────────────────────────────────────────

class ColaCentroPokemon:
    """
    Queue (FIFO) que simula el Centro Pokémon.
    Implementada sobre una lista de Python (append al final, pop desde inicio).
    """

    def __init__(self):
        self._cola: list[Pokemon] = []

    def encolar(self, pokemon: Pokemon) -> None:
        self._cola.append(pokemon)
        print(f"  → {pokemon.nombre} ingresa a la cola del Centro Pokémon.")

    def procesar(self) -> None:
        """Procesa todos los Pokémon de la cola uno por uno."""
        if not self._cola:
            print("  (La cola del Centro Pokémon está vacía)")
            return
        print("\n  🏥 Enfermera Joy comienza la curación...")
        while self._cola:
            pokemon = self._cola.pop(0)  # dequeue desde el frente
            print(f"  ⏳ Curando a {pokemon.nombre}...", end="", flush=True)
            time.sleep(0.4)
            print(" ¡Listo!")
        print("  ✔ ¡Todos tus Pokémon han sido curados!")

    def esta_vacia(self) -> bool:
        return len(self._cola) == 0

    def __len__(self):
        return len(self._cola)


# ─────────────────────────────────────────────────────────────────────────────
# Stack para Deshacer Transferencias
# ─────────────────────────────────────────────────────────────────────────────

class PilaTransferencias:
    """
    Stack (LIFO) que almacena los últimos 5 Pokémon transferidos al Profesor Oak.
    Permite deshacer la última transferencia.
    """

    def __init__(self):
        self._pila: list[Pokemon] = []

    def apilar(self, pokemon: Pokemon) -> None:
        if len(self._pila) >= MAXIMO_STACK_TRANSFERENCIAS:
            self._pila.pop(0)  # descarta el más antiguo si se llena
        self._pila.append(pokemon)

    def desapilar(self) -> Pokemon | None:
        if not self._pila:
            return None
        return self._pila.pop()

    def esta_vacia(self) -> bool:
        return len(self._pila) == 0

    def mostrar(self) -> None:
        if not self._pila:
            print("  (Sin transferencias recientes)")
        else:
            print("  Últimas transferencias (tope = última):")
            for i, p in enumerate(reversed(self._pila)):
                print(f"    {'→ TOPE' if i == 0 else '      '} {p.nombre} (PC: {p.poder_combate})")


# ─────────────────────────────────────────────────────────────────────────────
# Entrenador
# ─────────────────────────────────────────────────────────────────────────────

GIMNASIOS = {
    "Plateada": "Medalla Roca",
    "Azulona":  "Medalla Cascada",
    "Fucsia":   "Medalla Alma",
    "Celeste":  "Medalla Trueno",
    "Carmín":   "Medalla Arcoíris",
    "Lavanda":  "Medalla Pantano",
    "Morada":   "Medalla Volcán",
    "Viridiana": "Medalla Tierra",
}


class Entrenador:
    """Clase que agrupa todas las estructuras del entrenador."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo: list[Pokemon] = []          # Array (máx 6)
        self.pc = ListaEnlazada()                # Lista Enlazada Simple
        self.centro = ColaCentroPokemon()        # Queue
        self.pila_transferencias = PilaTransferencias()  # Stack
        self.medallas = RegistroMedallas()       # Hash Set
        self.caramelos: int = 0

    # ── Equipo ────────────────────────────────────────────────────────────────

    def capturar(self, pokemon: Pokemon) -> None:
        """
        Agrega al equipo si tiene espacio; si no, deriva a la PC.
        """
        if len(self.equipo) < MAXIMO_EQUIPO:
            self.equipo.append(pokemon)
            print(f"  ✔ ¡{pokemon.nombre} se unió a tu equipo!")
        else:
            self.pc.insertar_al_inicio(pokemon)
            print(
                f"  ⚠ Tu equipo está lleno (máx {MAXIMO_EQUIPO}). "
                f"{pokemon.nombre} fue enviado a la PC."
            )

    def mostrar_equipo(self) -> None:
        print(f"\n══════════ EQUIPO DE {self.nombre.upper()} ══════════")
        if not self.equipo:
            print("  (Equipo vacío)")
        else:
            for i, p in enumerate(self.equipo, 1):
                print(f"  [{i}] {p}")
        print(f"  Espacio: {len(self.equipo)}/{MAXIMO_EQUIPO}")
        print("═" * 42)

    # ── PC ────────────────────────────────────────────────────────────────────

    def mostrar_pc(self) -> None:
        print(f"\n══════════ PC DE {self.nombre.upper()} ══════════")
        self.pc.mostrar()
        print(f"  Total en PC: {len(self.pc)}")
        print("═" * 40)

    # ── Centro Pokémon ────────────────────────────────────────────────────────

    def enviar_al_centro(self) -> None:
        if not self.equipo:
            print("  Tu equipo está vacío.")
            return
        print(f"\n  Enviando {len(self.equipo)} Pokémon al Centro Pokémon...")
        for p in self.equipo:
            self.centro.encolar(p)
        self.centro.procesar()

    # ── Transferencia al Profesor Oak ─────────────────────────────────────────

    def transferir_a_oak(self, nombre: str) -> bool:
        """Transfiere un Pokémon de la PC al Profesor Oak."""
        pokemon = self.pc.eliminar_por_nombre(nombre)
        if pokemon is None:
            print(f"  ✗ No se encontró '{nombre}' en la PC.")
            return False
        self.pila_transferencias.apilar(pokemon)
        self.caramelos += 1
        print(
            f"  ✔ {pokemon.nombre} fue transferido al Prof. Oak. "
            f"Recibiste 1 caramelo (total: {self.caramelos})."
        )
        return True

    def deshacer_transferencia(self) -> bool:
        """Recupera el último Pokémon transferido y lo devuelve a la PC."""
        pokemon = self.pila_transferencias.desapilar()
        if pokemon is None:
            print("  ✗ No hay transferencias que deshacer.")
            return False
        self.pc.insertar_al_inicio(pokemon)
        self.caramelos = max(0, self.caramelos - 1)
        print(
            f"  ✔ ¡{pokemon.nombre} fue recuperado y devuelto a tu PC! "
            f"(caramelos: {self.caramelos})"
        )
        return True

    # ── Desafío a Líder de Gimnasio ───────────────────────────────────────────

    def desafiar_gimnasio(self) -> None:
        print("\n  ══ GIMNASIOS DISPONIBLES ══")
        nombres = list(GIMNASIOS.keys())
        for i, ciudad in enumerate(nombres, 1):
            medalla = GIMNASIOS[ciudad]
            tiene = "✔" if self.medallas.contiene(medalla) else " "
            print(f"  [{i}] {ciudad:<12} → {medalla} [{tiene}]")

        eleccion = input("\n  Elegí el número del gimnasio (0 para cancelar): ").strip()
        if eleccion == "0":
            return
        if not eleccion.isdigit() or not (1 <= int(eleccion) <= len(nombres)):
            print("  ✗ Opción inválida.")
            return

        ciudad = nombres[int(eleccion) - 1]
        medalla = GIMNASIOS[ciudad]

        print(f"\n  ⚔  ¡Desafiás al Líder del Gimnasio de {ciudad}!")
        print("  El combate está en curso", end="", flush=True)
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)
        print()

        gana = random.random() < 0.6  # 60% de probabilidad de ganar
        if gana:
            print(f"  🏆 ¡Ganaste la batalla contra el Líder de {ciudad}!")
            self.medallas.agregar(medalla)
        else:
            print(f"  💀 Perdiste contra el Líder de {ciudad}. ¡Sigue entrenando!")

    # ── Medallas ──────────────────────────────────────────────────────────────

    def mostrar_medallas(self) -> None:
        print(f"\n  ── Medallas de {self.nombre} ({self.medallas.cantidad()}/8) ──")
        self.medallas.mostrar()

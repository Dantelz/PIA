# modulo1_pokedex.py
# Módulo 1: Clase Base, Pokédex (Hash Map) y Registro de Medallas (Hash Set)

import json


class Pokemon:
    """Clase base que representa a un Pokémon."""

    def __init__(self, id: int, nombre: str, tipo: str, poder_combate: int):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate

    def __repr__(self):
        return (
            f"Pokemon(id={self.id}, nombre='{self.nombre}', "
            f"tipo='{self.tipo}', PC={self.poder_combate})"
        )

    def __str__(self):
        return (
            f"  #{self.id:>4} | {self.nombre:<12} | Tipo: {self.tipo:<10} | "
            f"PC: {self.poder_combate}"
        )


# ── Pokédex Nacional ──────────────────────────────────────────────────────────
# Implementada como Hash Map: clave = id (int), valor = instancia Pokemon.
# En Python, dict ya es un hash map de O(1) promedio para inserción/búsqueda.

class Pokedex:
    """Hash Map que actúa como base de datos global de Pokémon."""

    def __init__(self):
        self._mapa: dict[int, Pokemon] = {}

    def cargar_desde_json(self, ruta: str) -> None:
        """Precarga los Pokémon desde un archivo JSON."""
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for d in datos:
            p = Pokemon(d["id"], d["nombre"], d["tipo"], d["poder_combate"])
            self._mapa[p.id] = p
        print(f"[Pokédex] {len(datos)} Pokémon cargados desde '{ruta}'.")

    def registrar(self, pokemon: Pokemon) -> None:
        """Agrega o actualiza un Pokémon en la Pokédex."""
        self._mapa[pokemon.id] = pokemon

    def obtener(self, id: int) -> Pokemon | None:
        """Devuelve el Pokémon con el id dado, o None si no existe."""
        return self._mapa.get(id)

    def ids_ordenados(self) -> list[int]:
        """Devuelve la lista de IDs ordenados (para búsqueda binaria)."""
        return sorted(self._mapa.keys())

    def mostrar(self) -> None:
        """Imprime todos los Pokémon registrados."""
        print("\n══════════════════ POKÉDEX NACIONAL ══════════════════")
        for pokemon in sorted(self._mapa.values(), key=lambda p: p.id):
            print(pokemon)
        print("═" * 54)

    def __len__(self):
        return len(self._mapa)


# ── Registro de Medallas ──────────────────────────────────────────────────────
# Implementado como Hash Set (set de Python).
# Garantiza unicidad: no se puede duplicar una medalla.

class RegistroMedallas:
    """Hash Set que almacena los nombres de medallas obtenidas."""

    def __init__(self):
        self._medallas: set[str] = set()

    def agregar(self, nombre_medalla: str) -> bool:
        """
        Intenta agregar una medalla. Devuelve True si se agregó,
        False si ya existía (previniendo duplicados).
        """
        if nombre_medalla in self._medallas:
            print(f"  ⚠ Ya poseés la '{nombre_medalla}'. ¡No se puede duplicar!")
            return False
        self._medallas.add(nombre_medalla)
        print(f"  ✔ ¡'{nombre_medalla}' añadida a tu colección!")
        return True

    def contiene(self, nombre_medalla: str) -> bool:
        return nombre_medalla in self._medallas

    def mostrar(self) -> None:
        if not self._medallas:
            print("  (Sin medallas aún)")
        else:
            for m in sorted(self._medallas):
                print(f"  🏅 {m}")

    def cantidad(self) -> int:
        return len(self._medallas)

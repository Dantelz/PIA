class HashSet:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.buckets = [[] for _ in range(capacidad)]

    def _hash(self, key):
        return hash(key) % self.capacidad

    def agregar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        if key not in bucket:
            bucket.append(key)
        else:
            print(f"{key} ya existe.")

    def eliminar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        if key in bucket:
            bucket.remove(key)
            print(f"{key} eliminado.")
        else:
            print(f"{key} no encontrado.")

    def buscar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]

        return key in bucket

    def mostrar(self):
        print("HashSet:")
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")





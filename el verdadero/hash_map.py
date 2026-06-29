class HashMap:
    def __init__(self, capacidad=151):
        self.capacidad = capacidad
        self.buckets = [[] for _ in range(capacidad)]

    def hash(self, key):
        return hash(key) % self.capacidad

    def agregar(self, key, value):
        indice = self.hash(key)
        bucket = self.buckets[indice - 1]

        for k, v in bucket:
            if k == key:
                print(f"{key} ya existe")
                return

        bucket.append((key, value))
        

    def buscar(self, key):
        indice = self.hash(key)
        bucket = self.buckets[indice]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def eliminar(self, key):
        indice = self.hash(key)
        bucket = self.buckets[indice]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                print(f"{key} eliminada")
                return

        print(f"{key} no encontrada")

    def modificar(self, key, nuevo_value):
        indice = self.hash(key)
        bucket = self.buckets[indice]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, nuevo_value)
                print(f"{key} modificado {nuevo_value}")
                return

        print(f"{key} no encontrada")

    def mostrar(self):
        for bucket in self.buckets:
            for key, value in bucket:
                print(f"{key} : {value}")
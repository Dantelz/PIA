class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, pokemon):
        self.items.append(pokemon)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def mostrar(self):
        if self.is_empty():
            print("No hay pokemon en espera")
            return

        for pokemon in self.items:
            print(f"{pokemon.nombre}")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, pokemon):
        if len(self.items) >= 5:
            self.items.pop(0)
        self.items.append(pokemon)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]
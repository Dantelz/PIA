class hash_set:
    def __init__(self):
        self.table = set()

    def insert(self, value):
        self.table.add(value)

    def contains(self, value):
        return value in self.table

    def delete(self, value):
        if value in self.table:
            self.table.remove(value)

    def display(self):
        for value in self.table:
            print(value)
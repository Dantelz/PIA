class hash_set:
    def __init__(self):
        self.table = set()

    def contains(self, value):
        return value in self.table

    def insert(self, value):
        if not self.contains(value):
            self.table.add(value)
        else:
            return -1


    def delete(self, value):
        if value in self.table:
            self.table.remove(value)

    def display(self):
        for value in self.table:
            print(value)
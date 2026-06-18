class hash_table:
    def __init__(self, size=151):
        self.table = {}
    
    def function_hash(self, key):
        return hash(key) % 151

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key)
    
    def delete(self, key):
        if key in self.table:
            del self.table[key]

    def display(self):
        for key, value in self.table.items():
            print(f"{key}: {value}")
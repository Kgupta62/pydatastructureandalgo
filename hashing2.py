class HashLinear:

    def __init__(self, M):
        self.M = M
        self.table = [None for i in range(M)]
        self.size = 0

    def hash(self, key):
        sum = 0
        for i in range(len(key)):
            sum += ord(key[i])
        return sum % self.M

    def find(self, key):
        index = self.hash(key)
        while self.table[index] != None and self.table[index] != key:
            index = (index + 1) % self.M
        return index

    def insert(self, key):
        if self.size == self.M:
            raise Exception("Hash table is full")
        index = self.find(key)
        if self.table[index] == None:
            self.table[index] = key
            self.size += 1

    def delete(self, key):
        if self.size == 0:
            raise Exception("Hash table is empty")
        index = self.find(key)
        if self.table[index] == key:
            self.table[index] = None
            self.size -= 1

    def print(self):
        for key in self.table:
            if key != None:
                print(key, end=" ")
        print()


if __name__ == "__main__":
    table = HashLinear(20)
    table.insert("town")
    table.insert("rather")
    table.insert("short")
    table.insert("toward")
    table.insert("employee")
    table.insert("player")
    table.insert("toward")
    table.insert("the")
    table.insert("of")
    table.insert("college")
    table.insert("in")
    table.insert("yes")
    table.insert("billion")
    table.insert("five")
    table.insert("wear")
    table.insert("last")
    table.insert("decade")
    table.insert("first")
    table.insert("training")
    table.insert("friend")

    table.print()

    table.delete("employee")
    table.delete("of")
    table.delete("toward")
    table.delete("in")
    table.delete("player")
    table.delete("town")
    table.delete("toward")
    table.delete("five")
    table.delete("rather")
    table.delete("yes")

    table.print()
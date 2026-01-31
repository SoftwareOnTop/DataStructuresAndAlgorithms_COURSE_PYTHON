class HashLinear:
    def __init__(self, M):
        self.M = M
        self.T = [None] * M

    def print(self):
        for x in self.T:
            if x is None:
                print("F ", end="")
            else:
                print(f"{x} ", end="")
        print()

    def insert(self, data):
        sum = 0
        for char in data:
            sum += ord(char)

        total = sum % self.M

        first_tombstone = None

        for i in range(self.M):
            k = (total + i) % self.M

            if self.T[k] is None:
                if first_tombstone is not None:
                    self.T[first_tombstone] = data
                else:
                    self.T[k] = data
                return

            if self.T[k] == "T" and first_tombstone is None:
                first_tombstone = k
            if self.T[k] == data:
                return

        if first_tombstone is not None:
            self.T[first_tombstone] = data

    def delete(self, data):
        for i in range(self.M):
            if self.T[i] == data:
                self.T[i] = "T"
                break










if __name__ == "__main__":
    table = HashLinear(8)
    table.print()

    table.insert("apple")
    table.insert("orange")
    table.insert("banana")
    table.insert("grapes")
    table.insert("mango")
    table.insert("peach")
    table.insert("apple")
    table.print()

    table.delete("banana")
    table.delete("kiwi")
    table.delete("peach")
    table.print()
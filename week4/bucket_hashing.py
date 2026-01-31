
class HashBucket:
    def __init__(self, M, B):
        self.M = M
        self.B = B
        bucket_size = int(self.M / self.B)
        self.T = [[None] * bucket_size for _ in range(B)]
        self.overflow = []

    def print(self):
        for x in range(len(self.T)):
            for i in range(int(self.M / self.B)):
                if self.T[x][i] is None:
                    print("F ", end="")
                else:
                    print(f"{self.T[x][i]} ", end="")
        if len(self.overflow) > 0:
            for i in self.overflow:
                print(f"{i} ", end="")
        print()

    def insert(self, data):

        sum = 0
        for char in data:
            sum += ord(char)

        total = sum % (self.B)

        if data in self.T[total]:

            return

        for i in range(int(self.M / self.B)):
            if self.T[total][i] is None or self.T[total][i] == "T":
                self.T[total][i] = data
                return

        self.overflow.append(data)

    def delete(self, data):

        for i in range(len(self.T)):
            for j in range(int(self.M / self.B)):
                if data == self.T[i][j]:
                    self.T[i][j] = "T"

        if data in self.overflow:
            self.overflow.remove(data)




        return





if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.print()


    table.insert("apple")
    table.insert("orange")
    table.insert("banana")

    table.print()
    table.delete("banana")


    table.print()
    table.insert("banana")
    table.print()
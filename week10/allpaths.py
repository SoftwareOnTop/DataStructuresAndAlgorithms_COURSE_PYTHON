class Graph:
    def __init__(self, n):
        self.n = n
   
        self.nopath = float('inf')
        
    
        self.weights = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(self.nopath)
            self.weights.append(row)

    def add(self, u, v, w):
        self.weights[u][v] = w

    def remove(self, u, v):
        self.weights[u][v] = self.nopath

    def all_paths(self):
       
        list = []
        for r in range(self.n):

            list.append(self.weights[r][:])

       
        for i in range(self.n):
            list[i][i] = 0

   
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
    
                    if list[i][k] + list[k][j] < list[i][j]:
                        list[i][j] = list[i][k] + list[k][j]


        for i in range(self.n):
            for j in range(self.n):
                if list[i][j] == self.nopath:
                    list[i][j] = -1
        
        return list

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    M = graph.all_paths()
    for weights in M:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = []
        for i in range(n):
            self.adj.append([])

    def add(self, u, v):
      
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

    def remove(self, u, v):
   
        if v in self.adj[u]:
            self.adj[u].remove(v)
        if u in self.adj[v]:
            self.adj[v].remove(u)

    def dft(self, start):
        visited = [False] * self.n

        def dfs(v):
            if visited[v]:
                return
            print(v, end=" ")
            visited[v] = True

            for e in sorted(self.adj[v]):
                dfs(e)

        dfs(start)
        print()


if __name__ == "__main__":
    graph = Graph(6)
    vertices = ((0, 2), (0, 4), (2, 1),
                   (2, 3), (2, 5), (3, 0),
                   (3, 5), (4, 5), (5, 1))
    for u, v in vertices:
        graph.add(u, v)
        
    graph.dft(0)

    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)
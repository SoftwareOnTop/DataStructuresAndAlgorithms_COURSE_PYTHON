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

    def subgraphs(self):
        countti = 0

        visit = [False] * self.n

        for i in range(self.n):
            if not visit[i]:
              
              
                countti += 1
                
               
                stackki = [i]
                visit[i] = True
                
                while stackki:
                    node = stackki.pop()
                    for neighbour in self.adj[node]:
                        if not visit[neighbour]:
                            visit[neighbour] = True
                            stackki.append(neighbour)
        return countti

if __name__ == "__main__":
    graph = Graph(6)

    edges = ((0, 4), (2, 1), (2, 5), (3, 0), (5, 1))
    for u, v in edges:
        graph.add(u, v)
    
    print(graph.subgraphs())
    
    more_edges = ((0, 2), (2, 3), (3, 5), (4, 5))
    for u, v in more_edges:
        graph.add(u, v)

    print(graph.subgraphs())
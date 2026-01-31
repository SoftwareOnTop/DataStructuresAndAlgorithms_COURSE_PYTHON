class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = []
        for i in range(n):
            self.adj.append([])

    def add(self, u, v, w):
        # directed edge
        self.adj[u].append((v, w))

    def shortest_path(self, start, end):
        dist = [float('inf')] * self.n
        prev = [None] * self.n
        visited = [False] * self.n
        dist[start] = 0

        for _ in range(self.n):
            # find next unvisited vertex with minimum distance (simplest greedy)
            u = -1
            for i in range(self.n):
                if not visited[i] and dist[i] < float('inf'):
                    u = i
                    break
            if u == -1:
                break
            visited[u] = True

            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u

    
        path = []
        at = end
        while at is not None:
            path.append(at)
            at = prev[at]
        path.reverse()

        if path[0] != start:
            print(-1)
        else:
            print(' '.join(map(str, path)))


if __name__ == "__main__":
    graph = Graph(10)
    edges = ((0, 1, 25), (0, 2, 6), (1, 3, 10),
             (1, 4, 3), (2, 3, 7), (2, 5, 25),
             (3, 4, 12), (3, 5, 15), (3, 6, 4),
             (3, 7, 15), (3, 8, 20), (4, 7, 2),
             (5, 8, 2), (6, 7, 8), (6, 8, 13),
             (6, 9, 15), (7, 9, 5), (8, 9, 1))
    for u, v, w in edges:
        graph.add(u, v, w)

    graph.shortest_path(0, 9)
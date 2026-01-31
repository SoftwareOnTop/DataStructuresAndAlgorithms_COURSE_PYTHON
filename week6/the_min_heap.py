class MinHeap:
    def __init__(self, A: list):
        self.heap = A
        self.build_heap()  

    def build_heap(self):
        n = len(self.heap)
   
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i, n)

    def heapify(self, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest, n)

    def print(self):
        print(" ".join(str(x) for x in self.heap))

    def push(self, val: int):
        return val

if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()    # 1 4 2 5 8 6 3 
    heap.push(9)
    heap.print()        # 2 4 3 5 8 6 9
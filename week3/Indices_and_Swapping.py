
class Node:
    def __init__(self, data):
        self.data = data
        self.nextone = None

        
        

    

class LinkedList:
    def __init__(self):
       self.first = None

    
    def append(self, data):


     
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            return 
        
        now = self.first
        
        while now.nextone:
            now = now.nextone
        
        now.nextone = new_node
        




    def print(self):
        now = self.first
       
        while now:
            
            print(now.data, end=" -> " if now.nextone else "")
            now = now.nextone
        print()

    def insert(self, data, point):
        new_node = Node(data)
        if point == 0:
            new_node.nextone = self.first
            self.first = new_node  
            return
        
        now = self.first
        for _ in range(point - 1):  
            now = now.nextone
        new_node.nextone = now.nextone
        now.nextone = new_node 

    


    def index(self, data):
        current = self.first
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.nextone
            index += 1
        return -1


    

    def swap(self, i, j):
        
        
        return None
        






    def delete(self, datapoint):
        return datapoint

if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()
    L.delete(0)
    L.print()
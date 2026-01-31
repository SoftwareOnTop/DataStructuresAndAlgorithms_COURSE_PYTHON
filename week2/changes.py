
def changes(A):
    
    luku = 0
    for i in range(1, len(A)):

        
        if A[i] == A[i-1]:
            luku += 1
            A[i] = None
            
            

       

        
        
    return luku



if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))
    print(changes([1, 2, 3, 4, 5]))
    print(changes([1, 1, 1, 1, 1]))

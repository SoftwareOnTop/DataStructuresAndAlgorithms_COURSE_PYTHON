def primes(N):
    if N < 2:
        return
    
    luku = 0
    for i in range(2, N+1):
        alkuluku_on = True
        for j in range(2, i):
            if i % j == 0:
                alkuluku_on = False
                break
        if alkuluku_on:
            luku += 1

    return luku    

        

if __name__ == "__main__":
    print(primes(7))
    print(primes(15))
    print(primes(50))
    
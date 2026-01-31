def triangle(a, b, c):
    lista = sorted([a, b, c])

    # sivut postiviise
    if lista[0] <= 0:
        return False

    # kolmioepäyhtälö
    if lista[0] + lista[1] <= lista[2]:
        return False

    # suorakulnmaisuus
    if lista[2]**2 == lista[0]**2 + lista[1]**2:
        return True

    # tasasivuinen
    if a == b == c:
        return True

    return True


if __name__ == "__main__":
    print(triangle(3, 5, 4))   
    print(triangle(-1, 2, 3))  
    print(triangle(5, 9, 14))   
    print(triangle(30, 12, 29)) 

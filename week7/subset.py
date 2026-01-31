def subsets(n: int) -> list:
    tulos = []
    for i in range(1, n + 1):
        new_subsets = [[i]]  
        for s in tulos:
            new_subsets.append(s + [i])  
        tulos = tulos + new_subsets
    return tulos


if __name__ == "__main__":
    print(subsets(1))
    print(subsets(2))
    print(subsets(3))
    print(subsets(4))

    S = subsets(10)
    print(S[95])
    print(S[254])
    print(S[826])
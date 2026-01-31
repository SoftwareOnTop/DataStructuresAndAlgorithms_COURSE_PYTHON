
def sums(items):
    total = sum(items)
    dp = [False] * (total + 1)
    dp[0] = True  

    for x in items:

        for s in range(total, x - 1, -1):
            if dp[s - x]:
                dp[s] = True

    resultti = sum(dp[1:])
    return resultti


if __name__ == "__main__":
    print(sums([1, 2, 3]))                   
    print(sums([2, 2, 3]))                   
    print(sums([1, 3, 5, 1, 3, 5]))          
    print(sums([1, 15, 5, 23, 100, 55, 2]))
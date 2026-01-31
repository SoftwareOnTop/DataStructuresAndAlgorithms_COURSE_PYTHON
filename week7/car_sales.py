
def sales(cars, customers):
    laskuri = 0
    laskuri2 = 0
    cars_sorted = sorted(cars)
    customers_sorted = sorted(customers)

    for budgetti in customers_sorted:
        while laskuri2 < len(cars_sorted) and cars_sorted[laskuri2] <= budgetti:
            if cars_sorted[laskuri2] <= budgetti:
                laskuri += 1
                laskuri2 += 1
                break

            if laskuri2 >= len(cars_sorted):
                break
    return laskuri


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))
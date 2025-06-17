def get_product(tup):
    result = 1
    for number in tup:
        result = result * number
    return result

tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

print("Product of tup1 is:", get_product(tup1))
print("Product of tup2 is:", get_product(tup2))
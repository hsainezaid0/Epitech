res = 0

for i in range(200, 0, -1):
    nbr = 2 * i - 1
    res = nbr ** 2 / (6 + res)

pi = 3 + res

print(round(pi, 6))

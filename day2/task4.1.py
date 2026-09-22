pi = 0

for i in range(1, 1000000, 4):
    pi += 4 / i
    pi -= 4 / (i + 2)

print(round(pi,4))

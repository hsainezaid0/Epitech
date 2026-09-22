nbr = 123456789
res = 0

while nbr > 0:
    res += nbr % 10
    nbr //= 10

print(res)


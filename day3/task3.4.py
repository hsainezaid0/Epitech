var = input("Enter a string ")

words = var.split()

res = ""

for word in words:
   res = res + word[0]


print(res)

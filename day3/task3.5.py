var = input("Enter a text: ").lower()

letters = {}

for char in var:
    if char.isalpha():
        if char in letters:#.isalpha() vérifie si le caractère est une lettre.
            letters[char] += 1
        else:
            letters[char] = 1

print(letters)

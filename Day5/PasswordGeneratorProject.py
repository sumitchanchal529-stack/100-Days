import random

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
          "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
          "u", "v", "w", "x", "y", "z"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

a = int(input("How many letters do you want? "))
b = int(input("How many numbers do you want? "))
c = int(input("How many symbols do you want? "))

passwordlist = []

for char in range(a):
    passwordlist.append(random.choice(letter))

for char in range(b):
    passwordlist.append(random.choice(numbers))

for char in range(c):
    passwordlist.append(random.choice(symbols))

password = ""

for char in passwordlist:
    password += str(char)

print(f"Your password is: {password}")
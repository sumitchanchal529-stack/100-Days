print("Welcome to the tip calculator")

a = float(input("What is the total bill?\n"))
b = float(input("How much tip would you like to give?\n"))
c = int(input("How many people will split the bill?\n"))

total = a + b
each_person = total / c

print("Each person should pay ",(each_person))
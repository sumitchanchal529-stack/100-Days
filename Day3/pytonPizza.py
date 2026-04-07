print("welcome to python pizza dilivery")
small = 15
medium = 20
large = 25
bill = 0
pizzasize = str(input("what size of pizza do you want s m and l"))
if pizzasize== "s":
    print(f"here is your small size bill cost {small}")
    bill = 15
elif pizzasize == "m":
    print(f"here is your small medium bill cost {medium}")
    bill = 20
elif pizzasize == "l":
    print(f"here is your small size bill cost {large}")
    bill = 25
else:
    print("invalid pizza size")
    exit()
pepperoni = str(input("Do you want pepperoni y or n"))
if pepperoni == "y":
    bill += 2
    print(f"your final bill is {bill}")
extraChess = str(input("do you want extra cheess y or n"))
if extraChess =="y":
    bill += 3
    print(f"you fill bill is{bill}")




print("enter to the rollor coster")
height = int(input("what is your height"))
age = int(input("what is the your age"))
bill =0
if height>=120:
    print("you are eligible for rollor coster")
    if age>45 and age<65:
        print("your bill is 0")
        bill = 0
    elif age >= 18:
        print("your fee is 12 dollor")
        bill = 12
    elif age<12:
            print("your fee is 5 dollor")
            bill = 5
    else:
        print("your fee is 8 dollor")
        bill = 8

    wantPhoto = input("Do you want a photo or not type Y for Yes and N for No?")
    if wantPhoto == "Y" or wantPhoto == "y":
        bill += 3
    print(f"your final ticket price is {bill} ")
else:
    print("you are not eligible for rollor coster")
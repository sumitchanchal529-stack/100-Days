Fruits = ["apple","mango", "banna","pear"]
for Fruit in Fruits:
    print(Fruit)

studentscore =[24,56,35,65,5,6,5,66,33,64,54]
sum = 0
for score in studentscore:
    sum += score
print(sum)

maxscore = 0
for score in studentscore:
    if score>maxscore:
        maxscore = score
print(maxscore)

s=0
for number in range(0,101):
    s += number
print(s)
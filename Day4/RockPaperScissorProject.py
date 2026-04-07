rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

gameimage = [rock, paper, scissor]

print("Welcome to Rock Paper Scissor Game")

guest = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissor: "))

if guest < 0 or guest > 2:
    print("Invalid number, you lose")
else:
    print("You chose:")
    print(gameimage[guest])

    computer = random.randint(0, 2)

    print("Computer chose:")
    print(gameimage[computer])

    if guest == computer:
        print("Draw")
    elif guest == 0 and computer == 2:
        print("You win")
    elif guest == 2 and computer == 0:
        print("Computer wins")
    elif guest > computer:
        print("You win")
    else:
        print("Computer wins")
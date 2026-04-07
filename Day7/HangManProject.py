import random
from HangManLogo import logo
from HangManWordList import wordlist

print("WELCOME TO THE HANGMAN GAME")
print(logo)

STAGES = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',

    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',

    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',

    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',

    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''',

    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''',

    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]

guessword = random.choice(wordlist).lower()

lives = 6
correct_letters = []
guessed_letters = []
gameover = False

display = ""
for _ in guessword:
    display += "_"

print(display)

while not gameover:
    print(f"\n================= You have {lives} lives left =================")

    guesschar = input("Guess a character: ").lower()

    if len(guesschar) != 1:
        print("Please enter only one character.")
        continue

    if guesschar in guessed_letters:
        print(f"You already guessed '{guesschar}'. Try another letter.")
        continue

    guessed_letters.append(guesschar)

    if guesschar in guessword:
        print(f"\n'{guesschar}' is in the word! You saved him for now...")
        correct_letters.append(guesschar)
    else:
        lives -= 1
        print(f"\n'{guesschar}' is not in the word...")
        print("The executioner pulls the rope tighter.")
        print(f"You lose a life. Now you have {lives} lives left.")

    display = ""
    for letter in guessword:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)

    if lives < 6:
        print(STAGES[6 - lives])

    if "_" not in display:
        print("""
🎉 YOU WIN 🎉



The guards stop.
The rope is cut.
The prisoner falls to the ground, breathing heavily.

You saved him.
""")
        print(f"The word was: {guessword}")
        gameover = True

    if lives == 0:
        print(STAGES[6])

        print("""
💀 GAME OVER 💀

The crowd falls silent.

The final knot tightens around the prisoner's neck.
He looks at you one last time, hoping for the answer...

But it is too late.

The floor beneath him drops.
The rope swings slowly in the cold air.

You failed to save him.
""")

        print(f"This was the correct word: {guessword}")
        print("You could not guess it in time.")

        gameover = True
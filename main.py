from time import sleep
import random
from hangmanparts import parts
from words import words


parts(4)

print('Let me think of a word')


# wait time function
def wait():
    for i in range(5):
        print('.', end='')
        sleep(.5)

    print()


wait()

# List of words

word = random.choice(words)
print('Okay,The word has', len(word), 'letters')
for i in range(len(word)):
    print('_', ' ', end='')

print()
right = ['_'] * len(word)
wrong = []


# Prints letters in right with _'s
def add_letter():
    for i in right:
        print(i, ' ', end="")
    print()


# Prints out wrong letters
def wrong_letter():
    print("Wrong letters:", end="")
    for i in wrong:
        print(i, ' ', end="")
    print()


# Main Loop
while True:
    print('=====================')
    guess = input("Guess a letter")
    if guess in word:
        print("Let me check")

        # Handles letter that appear more than once

        index = 0
        for i in word:
            if i == guess:
                right[index] = guess
            index = index + 1

        add_letter()
        wrong_letter()
        parts(len(wrong))

    elif guess not in word:
        print("Let me check")

        if guess in wrong:
            print("You already guessed", guess)
            wrong_letter()
        else:
            print(guess, "is not in my word")
            wrong.append(guess)
            add_letter()
            wrong_letter()
            parts(len(wrong))

    if len(wrong) > 4:
        print("Game Over!")
        print('word was:', word)
        break

    if '_' not in right:
        print("You guessed it correct!")
        break

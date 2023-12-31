import random
words = ['agent', 'sensor', 'actuators', 'artificial']
word = random.choice(words)
guessed_word = ''
chances = 5
print("Guess the characters:")
while chances > 0:
    failed = 0
    for char in word:
        if char in guessed_word:
            print(char, end='')
        else:
            print("_", end='')
            failed += 1
    if failed == 0:
        print('\n')
        print("You Win!")
        print(f"The word is: {word}")
        break
    print('\n')
    guess = input("guess a character: ").lower()
    guessed_word += guess
    if guess not in word:
        chances -= 1
        print(f"You have {chances} chance")
        if chances == 0:
            print("You Lose!")
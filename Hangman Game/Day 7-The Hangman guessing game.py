import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)
chosen_word = random.choice(word_list)
display = ["_" for x in chosen_word]
active = True
lives = 6

while active:
    guess = input('Guess a letter: ').lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = chosen_word[i]

        print("".join(display))
    else:
        print(f'You guessed {guess} that is wrong, you have lost a life')
        lives -= 1

    print(stages[lives])

    if ('_' not in display) and (lives != 0):
        print('Congratulations you have won')
        active = False

    if lives == 0:
        print("You have used up all of your lives")
        print('Game Over!')
        print(stages[0])
        active = False


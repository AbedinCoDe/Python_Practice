import random
import ASCII_ART
import Logo
import word

#Making random choice

chosen_word = random.choice(word.word_list)

print("Welcome To The Hangman Game!")
print(Logo.logo)

# False Statement And live Count VAR
end_of_game = False
lives = 6

list1 = []
word_length = len(chosen_word)

for letter in range(word_length):
    list1 += "_"

while not end_of_game:
    guess = input("Guess Your latter: \n").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            list1[position] = letter
    print(list1)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    if "_" not in list1:
        end_of_game = True
        print("You Win!!")

# For Printing ASCII ART
    print(ASCII_ART.Present_stages[lives])
#Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

print(f"Chosen word is: {chosen_word}")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a latter: \n").lower()

list1 = []
word_length = len(chosen_word)

for letter in range(word_length):
    list1 += "_"


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        list1[position] = letter



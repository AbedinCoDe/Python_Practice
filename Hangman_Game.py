#Step 1

# Hangman art here
Present_stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)

print(f"Chosen word is: {chosen_word}")

end_of_game = False

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

    if "_" not in list1:
        end_of_game = True
        print("You Win!!")



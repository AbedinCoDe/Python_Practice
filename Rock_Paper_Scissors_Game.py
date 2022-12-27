import random

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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Game_Pattern = [rock, paper, scissors]

user_Choice = int(input("What is Your Choice? 0 for Rock, 1 For Paper, 2 for Scissor\n"))

if user_Choice >=3 or user_Choice < 0:
    print("You have entered invalid Number. You Lose.")

else:
    print(f"Your Choice:{user_Choice}")
    print(Game_Pattern[user_Choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer Choice:{computer_choice}")

    print(Game_Pattern[computer_choice])
    if user_Choice == 0 and computer_choice == 1:
        print("You Lose")
    elif user_Choice == 1 and computer_choice == 0:
        print("You Won!")
    elif user_Choice == 1 and computer_choice == 2:
        print("You Lose")
    elif user_Choice == 0 and computer_choice == 2:
        print("You Won!")
    elif user_Choice == 2 and computer_choice == 1:
        print("You Lose")
    elif user_Choice == 2 and computer_choice == 0:
        print("You Lose")
    elif user_Choice == computer_choice:
        print("Match Draw")


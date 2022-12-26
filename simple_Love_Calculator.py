# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine_strint = name1 + name2

lower_strint = combine_strint.lower()

T = lower_strint.count("t")
R = lower_strint.count("r")
U = lower_strint.count("u")
E = lower_strint.count("e")

TRUE = T + R + U + E

L = lower_strint.count("l")
O = lower_strint.count("o")
V = lower_strint.count("v")
E = lower_strint.count("e")

LOVE = L + O + V + E

score = int(str(TRUE) + str(LOVE))

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}")
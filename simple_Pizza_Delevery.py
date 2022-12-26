# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

small_pizza = 15
medium_pizza = 20
Large_pizza = 25

with_pepperoni_small = small_pizza + 2
with_pepperoni_medium = medium_pizza + 3
with_pepperoni_large = Large_pizza + 3

if size == "S":

    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${with_pepperoni_small + 1}.")
    if add_pepperoni == "Y":
        if extra_cheese == "N":
            print(f"Your final bill is: ${with_pepperoni_small}.")
    if add_pepperoni == "N":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${small_pizza + 1}.")

    if add_pepperoni == "N":
        if extra_cheese == "N":
            print(f"Your final bill is: ${small_pizza}.")

if size == "M":

    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${with_pepperoni_medium + 1}.")
    if add_pepperoni == "Y":
        if extra_cheese == "N":
            print(f"Your final bill is: ${with_pepperoni_medium}.")
    if add_pepperoni == "N":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${medium_pizza + 1}.")

    if add_pepperoni == "N":
        if extra_cheese == "N":
            print(f"Your final bill is: ${medium_pizza}.")

if size == "L":

    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${with_pepperoni_large + 1}.")
    if add_pepperoni == "Y":
        if extra_cheese == "N":
            print(f"Your final bill is: ${with_pepperoni_large}.")
    if add_pepperoni == "N":
        if extra_cheese == "Y":
            print(f"Your final bill is: ${Large_pizza + 1}.")

    if add_pepperoni == "N":
        if extra_cheese == "N":
            print(f"Your final bill is: ${Large_pizza}.")





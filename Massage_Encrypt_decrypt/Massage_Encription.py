from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shifting_amount, cipher_direction):
    new_letter = ""
    if cipher_direction == "decode":
        shifting_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shifting_amount
            new_letter += alphabet[new_position]
        else:
            new_letter += letter
    print(f"The {cipher_direction}d text is {new_letter}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(plain_text=text, shifting_amount=shift, cipher_direction=direction)
    user_continue_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if  user_continue_input == "no":
        should_continue = False
        print("GoodBye")



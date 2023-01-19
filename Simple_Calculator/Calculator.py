
from Logo import logo


print(logo)

# Add
def add(n1, n2):
    return n1 + n2

# Subtract

def subtraction(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# division
def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": divide
}
# first calculation
def calculator():
    num1 = int(input("What is Your 1st number? \n"))

    should_continue = True
    while should_continue:
        for operate in operation:
            print(operate)
        operation_symble = input("what is your operation? \n")
        num2 = int(input("What is the next number?\n"))

        calculation_function = operation[operation_symble]
        first_answer = calculation_function(num1, num2)
        print(f"Your answer is: {first_answer}")

        # for second calculation
        check_Input = input(f"If you want to calculte more number with {first_answer} then type 'Y' And stop 'N' \n")

        if check_Input == "N":
            should_continue = False
            calculator()

        elif  check_Input == "Y":
            num1 = first_answer

calculator()




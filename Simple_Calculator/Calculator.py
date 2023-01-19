

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

should_continue = True

while should_continue:
    num1 = int(input("What is Your 1st number? "))
    for operate in operation:
        print(operate)
    operation_symble = input("what is your operation? \n")
    num2 = int(input("What is the next number?\n"))

    calculation_function = operation[operation_symble]
    first_answer = calculation_function(num1, num2)
    print(f"Your answer is: {first_answer}")

    # for second calculation

    if (f"If you want to calculte more number with ")





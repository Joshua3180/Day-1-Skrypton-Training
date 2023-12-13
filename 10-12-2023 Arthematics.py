print("Enter any two integer numbers: ")
a = int(input())
b = int(input())


def perform_operations(a, b):
    # Addition
    addition = a + b
    print("Addition: ", a, "+", b, "=", addition)

    # Subtraction
    subtraction = a - b
    print("Subtraction: ", a, "-",  b, "=", subtraction)

    # Multiplication
    multiplication = a * b
    print("Multiplication: ", a, "*", b, "=", multiplication)

    # Division
    if b != 0:
        division = a / b
        print("Division: ", a, "/", b, "=", division)
    else:
        print(" --X---Division by zero is not Defined---X--")

    # Modulus
    if b != 0:
        modulus = a % b
        print("Modulus: ", a, "%", b, "=", modulus)
    else:
        print(" --X---Modulus by zero is not Defined---X--")

perform_operations(a, b)

    

    
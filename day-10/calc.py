import calc_ascii

calc = calc_ascii.calc_logo
calculator = calc_ascii.calculator_logo
print(calc)
print(calculator)


def add(n1, n2):
    """Addition function. Adds the first input to the second"""
    return n1 + n2


def subtract(n1, n2):
    """Subtraction function. Subtracts the first input from the second"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplication function. Multiplies the first input by the second"""
    return n1 * n2


def divide(n1, n2):
    """Division function. Divides the first input by the second"""
    return n1 / n2


operands = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calc():
    num1 = float(input("\nWhat is the first number?: "))
    for symbol in operands:
        print(f"\n{symbol} {operands[symbol].__doc__}")
    should_continue = True

    while should_continue:
        operation_symbol = input("\nPick an operand: ")
        num2 = float(input("\nWhat is the next number?: "))
        calc_function = operands[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"\n{num1} {operation_symbol} {num2} = {answer}\n")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to begin a new calculation. ") == "y":
            num1 = answer
        elif should_continue == False:
            calc()
        else:
            should_continue = False


calc()

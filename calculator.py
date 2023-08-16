from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# Recursive function
def calculator():
  print(logo)

  num_1 = float(input("Enter the first number: "))

  for operation in operations:
      print(operation)

  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")

    num_2 = float(input("Enter the next number: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num_1, num_2)

    print(f"{num_1} {operation_symbol} {num_2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
        num_1 = answer
    else:
        should_continue = False
        calculator()

calculator()
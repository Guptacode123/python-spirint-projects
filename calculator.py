while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose the operation (+, -, *, /, ^): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif operation == '^':
        result = num1 ** num2
    else:
        result = "Invalid operation!"

    print("Result:", result)

    cont = input("Do you want to continue? (Y/N): ").strip().lower()
    if cont != 'y':
        break
# Singhal@aman1110
while True:

    operation = input("Enter operation (+, -, *, /, %, ** ) or exit : ")

    if operation == "exit":
        break

    num1 = input("Enter the first number = ")

    num2 = input("Enter the second number = ")

    if operation == "+":
        print(float(num1) + float(num2))

    elif operation == "-":
        print(float(num1) - float(num2))

    elif operation == "*":
        print(float(num1) * float(num2))

    elif operation == "/":
        print(float(num1) / float(num2))

    elif operation == "%":
        print(float(num1) % float(num2))

    elif operation == "**":
        print(float(num1) ** float(num2))

    else:
        print("Not defined")
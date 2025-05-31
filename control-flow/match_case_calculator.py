"""Enter the first number: 10
Enter the second number: 5
Choose the operation (+, -, *, /): *
The result is 50."""

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation  = input("Choose the operation (+, -, *, /):")
result = 0

if operation == "+":
    addition = num1 + num2
    result = addition
    print("The result is", result)
elif operation == "-":
    subtract = num1 - num2
    result = subtract
    print("The result is", result)
elif operation == "*":
    multiply = num1 * num2
    result = multiply
    print("The result is", result)
elif operation == "/":
    if num2 != 0:
        divide = num1 / num2
        result = divide
        print("The result is", result)
    else:
        print("Cannot divide by zero.")
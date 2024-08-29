
#Make the user input both num1, num2 and the operator

num1 = float(input("enter num1"))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("enter num2"))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1 / num2)

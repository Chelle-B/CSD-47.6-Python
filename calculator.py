def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def floor_division(x,y):
    if y == 0:
        return "Error!Division by zero."
    return x // y
def remainder(x,y):
    return x % y
def exponent(x,y):
    return x ** y
def percentage(x, y):
    return (x / y) * 100
def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of negative number."
    return x ** 0.5
def cube_root(x):
    if x < 0:
        return -(-x) ** (1/3)
    return x ** (1/3)
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Floor division")
print("6. Remainder")
print("7. Exponent")
print("8. Percentage")
print("9.Square root")
print("10.Cube root")



while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")
    if choice in ['1', '2', '3', '4','5' ,'6','7','8','9','10']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} // {num2} = {floor_division(num1, num2)}")
        elif choice == '6':
            print(f"{num1} % {num2} = {remainder(num1, num2)}")        
        elif choice == '7':
            print(f"{num1} ** {num2} = {exponent(num1, num2)}")    
        elif choice == '8':
            print(f"{num1} % {num2} = {percentage(num1, num2)}")    
        elif choice == '9':
            print(f"Square root of {num1} = {square_root(num1)}")
        elif choice == '10':
            print(f"Cube root of {num1} = {cube_root(num1)}")
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")


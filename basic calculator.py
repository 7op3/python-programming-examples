#this is a program that will expand upon 'add.py'. it will still ask the user for two integer inputs, but it will also ask the user for a mathematical operation, and then it will carry that operation out.

num1 = int(input('Please enter a number.'))

num2 = int(input('Please enter another number.'))

operation = input('Please select a mathematical operator (+, - , * or /)')

if operation == '+':
    print(num1,operation,num2,'=',num1+num2)
elif operation == '-':
    print(num1,operation,num2,'=',num1-num2)
if operation == '*':
    print(num1,operation,num2,'=',num1*num2)
elif operation == '/':
    print(num1,operation,num2,'=',num1/num2)
else:
    print('Please only use the given operations (+, -, * or /)')
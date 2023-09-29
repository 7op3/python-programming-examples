#this is a program that will expand upon 'add.py'. it will still ask the user for two integer inputs, but it will also ask the user for a mathematical operation, and then it will carry that operation out.

#takes two inputs, 'num1' and 'num2'. the user will have to input these themselves.
num1 = int(input('Please enter a number.'))
num2 = int(input('Please enter another number.'))

#takes another input, which is the mathematical operation that will be used.
operation = input('Please select a mathematical operator (+, - , * or /)')

#these 'if' and 'elif' statements check which mathematical operator has been chosen, and then prints out the answer, or provides an error message if an operator isn't provided.
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
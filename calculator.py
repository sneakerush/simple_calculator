print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print("Type 'quit' to exit")
active = True

while active:
    operation = input("Select an operation to perform: ")

    if operation == '1':
        num1 = input('Enter first number: ')
        num2 = input('Enter second number: ')
        num1 = int(num1)
        num2 = int(num2)
        num3 = num1 + num2
        print(f'The answer is {num3}')

    elif operation == '2':
        num4 = input('Enter first number: ')
        num5 = input('Enter second number: ')
        num4 = int(num4)
        num5 = int(num5)
        num6 = num4 - num5
        print(f'The answer is {num6}')

    elif operation == '3':
        num7 = input('Enter first number: ')
        num8 = input('Enter second number: ')
        num7 = int(num7)
        num8 = int(num8)
        num9 = num7 * num8
        print(f'The answer is {num9}')

    elif operation == '4':
        num10 = input('Enter first number: ')
        num11 = input('Enter second number: ')
        num10 = int(num10)
        num11 = int(num11)
        num12 = num10 / num11
        print(f'The answer is {num12}')

    elif operation == 'quit':        
        quit()

    else: 
        print('Invalid Entry!')







#command line interface(CLI) calculator
number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))

print('Choose the operation: ')
print('1.ADDITION')
print('2.SUBTRACTION')
print('3.MULTIPLICATION')
print('4.DIVISION')

choice = input('Enter your choice:')
if choice == '1':
    print (f'Answer: {number1 + number2}')
elif choice == '2':
    print (f'Answer: {number1 - number2}')
elif choice == '3':
    print (f'Answer: {number1 * number2}')
elif choice == '4':
    print (f'Answer: {number1 // number2}')
else:
    print('CHOICE DOESN\'T EXIST!!')


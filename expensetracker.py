print('Helllo  world, first week project')
#DEFINING THE CATEGORIES
categories = ['skincare','food','transport','bills','miscellaneous']

expenses = []

#SHOW THE CATEGORY
print('AVAILABLE CATEGORIES')
for item in categories:
    print('*',item)

#expense function
def expense_status():

    amount = int(input('Enter the amount: '))
    '''category = input('Enter the category: ')
   '''

    while True:
        category = input('Enter the category:')
        if category in categories:
            break
        else :
            print(f'Invalid Category, Choose from {categories}')
     
    # NIGERIA TIMEZONE
    from datetime import datetime, timezone, timedelta
    nigeria_time = timezone(timedelta(hours=1))
    now = datetime.now(nigeria_time)
    date_time = now.strftime('%d/%m/%Y %I:%M %p')

    note = input('Enter the note: ')

     
    expense_dictionary = {
        'amount' : amount,
        'category' : category,
        'note' : note,
        'date' :  date_time
    }
    return expense_dictionary


def view_expenses(): 
    if len(expenses) == 0:
        print('No expenses added yet')
    else:
        print('\nEXPENSE LIST:')
        print('amount, category, date')
        for e  in expenses:
            print('Amount:', e['amount'])
            print('category:', e['category'])
            print('note:', e['note'])
            print('date', e['date'])

def total_expenses():
    total = 0
    for e in expenses:
        total += int(e['amount'])

        
    print('total expense:', total)

def save_to_file():
    with open('expense.txt', 'a') as f:
        for e in expenses:
            f.write(f'{e}\n')
    print('Expenses is added to expense.txt')




while True:     
    
    print('\nMENU')
    print('1. ADD EXPENSE')
    print('2. VIEW EXPENSE')
    print('3. TOTAL EXPENSE')
    print('4. SAVE TO FILE')
    print('5.EXIT PROGRAM')

    choice = input('Enter the choice:')

    if choice == '1':
        new_data = expense_status()
        expenses.append(new_data)
        print('Expense Added')
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        save_to_file()
    elif choice == '5':
        print('Goodbye')
        break
    else:
        print('Invalid choice') 

print('Helllo  world, first week project')
#DEFINING THE CATEGORIES
categories = ['food','groceries','transport','bills','others']
print('AVAILABLE CATEGORIES')

#SHOW THE CATEGORY
for item in categories:
    print('*',item)

while True:
    category = input('Enter the category:').upper()

for category in categories:
    print('CATEGORY ACCEPTED:',category)    
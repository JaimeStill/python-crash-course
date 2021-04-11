cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print()

# checking multilple conditions

age_0 = 22
age_1 = 18
check_1 = age_0 >= 21 or age_1 >= 21
check_2 = age_0 >= 21 and age_1 >= 21

print(check_1)
print(check_2)
print()

# checking whether a value is in a list

requested_toppings = ['mushrooms', 'onions', 'pineapple']
has_mushrooms = 'mushrooms' in requested_toppings
has_pepperoni = 'pepperoni' in requested_toppings
print(has_mushrooms)
print(has_pepperoni)
print()

# checking whether a value is not in a list

banned_users = ['andrew', 'carolina', 'david']

user = 'marie'
if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')
print()

# if elif else

age = 17

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f'Your admission cost is ${price}')
print()

# checking for special items
requested_toppings = [
    'mushrooms',
    'green peppers',
    'extra cheese'
]

missing_toppings = [
    'green peppers',
    'onions',
    'anchovies'
]

for requested_topping in requested_toppings:
    if requested_topping in missing_toppings:
        print(f'Sorry, we are out of {requested_topping} right now.')
    else:
        print(f'Adding {requested_topping}.')
print('Finished making your pizza!\n')

# checking that a list is not empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('Finished making your pizza!\n')
else:
    print('Are you sure you want a plain pizza?\n')

# using multiple lists

available_toppings = [
    'mushrooms',
    'olives',
    'green peppers',
    'pepperoni',
    'pineapple',
    'extra cheese'
]

requested_toppings = [
    'mushrooms',
    'french fries',
    'extra cheese'
]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print('Finished making your pizza!\n')
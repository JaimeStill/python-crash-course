alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])  # green
print(alien_0['points']) # 5

# adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print()

# modifying values in a dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'red'
print(f"The alien is now {alien_0['color']}")
print()

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")
print()

# removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
print()

# a dictionary of similar objects
# modified this exercise to generate a dictionary
# from two distinct lists so I remember zip and
# how to iterate through a dictionary
responses = {}
people = [
    'jen',
    'sarah',
    'edward',
    'phil'
]

languages = [
    'python',
    'c',
    'ruby',
    'python'
]

for person, lang in zip(people, languages):
    responses[person] = lang

for response in responses:
    print(f"{response.title()}'s favorite language is {responses[response].title()}.")
print()

# or
for person, lang in responses.items():
    print(f"{person.title()}'s favorite language is {lang.title()}.")
print()

# using get to access values
alien_0 = {
    'color': 'green',
    'speed': 'slow'
}

print(alien_0.get('color', 'No color value assigned'))
print(alien_0.get('points', 'No points value assigned'))
print()

# looping through all keys in dictionary

for person in responses.keys():
    print(person.title())
print()

# the default behavior for dictionary iteration
# is to loop through the keys:
for person in responses:
    print(person.title())
print()

friends = ['phil', 'sarah']
for person in responses:
    print(f"Hi {person.title()}.")

    if person in friends:
        language = responses[person].title()
        print(f"\t{person.title()}, I see you love {language}!")

if 'aaron' not in responses:
    print('Aaron, please take our poll!')
print()

# looping through keys in a certain order
for person in sorted(responses):
    print(f"{person.title()}, thank you for taking the poll.")
print()

# looping through all values in a dictionary
# set ensures there are no duplicates
print("The following languages have been mentioned:")
for lang in sorted(set(responses.values())):
    print(lang.title())
print()

# sets are like dictionaries, just with no key-value pairs
languages = {'python', 'ruby', 'python', 'c'} # duplicates are removed in a set
print(languages) # {'c', 'python', 'ruby'}
print()

# a list of dictionaries
# predicatable approach
aliens = []
print('predictable aliens:')

for idx in range(1, 31):
    alien = {
        'id': idx,
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }

    aliens.append(alien)

for alien in aliens[:9]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens:
    print(alien)
print()

# random approach
import random

aliens = []
print('random aliens:')

for idx in range(1, 31):
    seed = random.randint(1, 10)
    if seed <= 6:
        alien = {
            'id': idx,
            'seed': seed,
            'color': 'green',
            'points': 5,
            'speed': 'slow'
        }
    elif seed > 6 and seed <= 9:
        alien = {
            'id': idx,
            'seed': seed,
            'color': 'yellow',
            'points': 10,
            'speed': 'medium'
        }
    else:
        alien = {
            'id': idx,
            'seed': seed,
            'color': 'red',
            'points': 15,
            'speed': 'high'
        }

    aliens.append(alien)
    print(alien)
print()

# a list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
print()

favorite_langauges = {
    'jen': ['python', 'ruby'],
    'sarah': ['rust', 'haskell'],
    'edward': ['ruby', 'go'],
    'phil': ['c#', 'typescript', 'python']
}

for name, languages in favorite_langauges.items():
    print(f"{name.title()}'s favorite languages are:")
    for lang in languages:
        print(f"\t{lang.title()}")
print()

# a dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, info in users.items():
    print(f"Username: {username}")
    full_name = f"{info['first']} {info['last']}"
    location = info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
print()
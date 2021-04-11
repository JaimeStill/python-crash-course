# loop through a list
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f'{magician.title()} that was a great trick!')

print('Thank you everyone. That was a great magic show!\n')
print()

# using the range function
for value in range(1,5):
    print(value)

print()

# using range to make a list of numbers

numbers = list(range(1, 6)) # 1 - 5

even_numbers = list(range(2, 11, 2)) # 2 - 11 in steps of 2, so evens 2 - 10

# first 10 square numbers
squares = []
for value in range(1,11):
    square = value**2
    print(square)
    squares.append(square)
print()

# simple statistics with a list of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(f'min: {min(digits)}')
print(f'max: {max(digits)}')
print(f'sum: {sum(digits)}')
print()

# list comprehensions

# generate first 10 square numbers in one line using a list comprehension
squares = [value**2 for value in range(1,11)]

# sum of all numbers 1 - 1,000,000
print(sum(range(1,1_000_001)))
print()

# first 20 fibonacci numbers
fibonacci = [0,1]

for value in range(2,21):
    fibonacci.insert(value, fibonacci[value - 2] + fibonacci[value - 1]);

print(fibonacci)
print()

# cube comprehension
cubes = [value**3 for value in range(1,21)]
print(cubes)
print()

# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3]) # martina, michael

# omit the first index in a slice, python automatically starts at the beginning
print(players[:4]) # charles, martina, michael, florence

# omit the second index in a slice, all remaining elements are included after the starting index
print(players[2:]) # michael, florence, eli

# the third value specifies how many items to skip between items.
# this provides all even players
print(players[1:5:2]) # martina, florence
print()

# looping through a slice
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())
print()

# copying a list

my_foods = ['pizza', 'falafel', 'carrot cake']

# if you don't specify the slice here, friend_foods will be a reference to my_foods
friend_foods = my_foods[:]

my_foods.append('ice cream')
friend_foods.append('cannoli')

print(my_foods)
print(friend_foods)
print()

# defining a tuple, an immutable list
dimensions = (200, 50)
print(f'x:{dimensions[0]}, y:{dimensions[1]}')

# looping through values in a tuple
for dimension in dimensions:
    print(dimension)
print()

# writing over a tuple
dimensions = (400, 100)
print(f'x:{dimensions[0]}, y:{dimensions[1]}')
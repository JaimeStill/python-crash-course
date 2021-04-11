end = '\n\n'
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

trek = bicycles[0].title() # Trek

# negative index values count backwards from the end
# -1 represents the first item a the end, -2 the second, and so on
# think of this as shorthand for bicycles[len(bicycles) - 1]
specialized = bicycles[-1].title() # Specialized

motorcycles = ['honda', 'yamaha', 'suzuki']

# Change an element in a list
motorcycles[0] = 'ducati'

# Add an element to the end of a list
motorcycles.append('honda')

# Insert an element into a list
motorcycles.insert(0, 'polaris')

# Remove an element from a list using del

del motorcycles[0]

# Remove the last element using the pop method

popped = motorcycles.pop()

# Remove an item by value

motorcycles.remove('ducati')

print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']

# Sort a list permanently with the sort method
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sort a list temporarily with sorted
print(sorted(cars))
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

# Reverse a list

cars.reverse()
print(cars)

# Get the length of a list

print(len(cars))
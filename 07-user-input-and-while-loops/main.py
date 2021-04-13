# how the input function works
message = input("Tell me something, and I will repeat it back to you: ")
if message.lower() == 'something':
    print("That's illegal\n")
else:
    print(f"You said: {message}\n")
    
# using int to accept numerical input
# python's ternary syntax:
# (if false, if true)[test]
age = int(input("How old are you? "))
result = ("You are not old enough\n", "You are plenty old enough\n")[age >= 21]
print(result)

# the modulo (%) operator gives the remainder of dividing two numbers
number = int(input("Enter a number to, and I'll tell you if it's even or odd: "))

result = (
    f"{number} is odd\n",
    f"{number} is even\n"
)[number % 2 == 0]

print(result)

# the while loop in action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# letting the user choose when to quit
# without if (message.lower() != 'quit'), quit would be printed
prompt = "Tell me something, and I will repeat it back to you:"\
    "\nEnter 'quit' to end the program. "

message = ""
while message.lower() != 'quit':
    message = input(prompt)
    if (message.lower() != 'quit'):
        print(message)
    print()

# using a flag to exit a while loop
active = True
while active:
    message = input(prompt)

    if message.lower() == 'quit':
        active = False
    else:
        print(message)
print()

# using break to exit a loop
prompt = "Please enter the name of a city you have visited:"\
    "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
print()

# using continue in a loop
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print()

# moving items from one list to another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    print("The following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
    print()

# removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# filling a dictionary with user input
responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
print()
name = "ada lovelace"

print(name.title()) # Ada Lovelace
print(name.upper()) # ADA LOVELACE
print(name.lower()) # ada lovelace

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(f'{message}\n') # Hello, Ada Lovelace!

languages = "Languages:\n\tPython\n\tC\n\tJavaScript"
print(f'{languages}\n')

favorite_language = 'typescript '.rstrip() # strip whitespace from the right side
favorite_language = ' typescript'.lstrip() # strip whitespace from the left side
favorite_language = ' typescript '.strip() # strip whitespace from both sides
print (f'{favorite_language}\n')

apostrophe = 'I am starting to really appreciate Python\'s syntax.\n'
print(apostrophe)

favorite_number = 85
print(f'My favorite number is: {favorite_number}\n')

import this
print(this)
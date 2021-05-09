name = str(input('Whats your complete name? ')).strip()
names = name.split()
print('Your first name is', names[0])
print('Your last name is', names[len(names) - 1])

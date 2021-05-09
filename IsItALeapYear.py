year = int(input('Whats the year you wanna analysis'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é bissexto!'.format(year))
else:
    print('O ano {} não é bissexto!'.format(year))
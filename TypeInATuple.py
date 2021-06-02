tab = ('Notebook', 20, 'Smartphone', 780, 'Laptop', 6700)
print('Product', '.' * 22, 'Price')
print('-' * 35)
for item in tab:
    if type(item) == str:
        print(f'{item:.<30}', end='')
    else:
        print(f'${item:>5.2f}')

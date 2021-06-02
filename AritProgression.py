f = int(input('first: '))
r = int(input('ratio: '))
c = 0
more = 10
while more != 0:
    c = more + c
    while c != 0:
        print('{} -> '.format(f), end='')
        f = f + r
        c = c - 1
    print('\nSTOP')
    more = int(input('How many terms more: '))
print('Finale')
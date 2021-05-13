n1 = int(input('first number: '))
n2 = int(input('second number: '))
c = 0
while c != 5:
    print('What do you want to do?\n'
          '1 -  sum\n'
          '2 - multiply\n'
          '3 - know the higher\n'
          '4 - change the numbers\n'
          '5 - exit')
    c = int(input('- '))
    if c == 1:
        print('The sum is {}'.format(n1 + n2))
    elif c == 2:
        print('The multiplication is {}'.format(n1 * n2))
    elif c == 3:
        if n1 > n2:
            print('The higher number is {}'.format(n1))
        else:
            print('The higher number is {}'.format(n2))
    elif c == 4:
        n1 = int(input('first number: '))
        n2 = int(input('second number: '))
print('Bye bye')

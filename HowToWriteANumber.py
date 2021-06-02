# It can be make with the library 'num2word'
numbers = ('zero', 'one', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine', 'ten')

while True:
    v = int(input('Choose a number between 0 - 10 and see how it is written '))

    if 0 <= v <= 10:
        print(f'{v} - {numbers[v]}')

        sn = str(input('Wanna see more?(y/n) '))
        if sn == 'n':
            break
    else:
        print('Try again. ', end='')

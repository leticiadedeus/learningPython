import random
listEoO = ['e', 'o']
print('Lets play EVEN or ODD')
print('-' * 30)
c = 0
while True:
    eoo = str(input('Are you EVEN or ODD?(e/o): ')).lower()
    print('-' * 30)
    nU = int(input('What number do you want to play? '))
    print('-' * 30)
    eooP = random.choice(listEoO)
    nPc = random.randint(0, 10)
    nf = nU + nPc
    if nf % 2 == 0:
        if eoo == 'e':
            print('USER IS THE WINNER')
            c += 1
        else:
            print(f'PC IS THE WINNER\nGAME OVER - You won {c} times')
            break
    else:
        if eoo == 'o':
            print('USER IS THE WINNER')
            c += 1
        else:
            print(f'PC IS THE WINNER\nGAME OVER - You won {c} times')
            break

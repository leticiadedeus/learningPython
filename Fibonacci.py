hm = int(input('how many terms of Fibonacci do you want to see?: '))
f = 0
s = 1
while hm >= 3:
    print('{} - >'.format(f), end='')
    hm = hm - 1
    while hm >= 2:
        print(' {} -> '.format(s), end='')
        hm = hm - 1
        while hm >= 1:
            t = f + s
            print(' {} -> '.format(t), end='')
            f = s
            s = t
            hm = hm - 1
print(' FIM')

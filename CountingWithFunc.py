def counting(a, b, s):
    if a < b:
        for c in range(a, b + 1, s):
            print(c, end=' ')
        print()
        print('=-' * 10)
    if a > b:
        if s == 0:
            s = 1
        if s < 0:
            s = s * -1
        for c in range(a, b - 1, -s):
            print(c, end=' ')
        print()
        print('=-' * 10)


counting(1, 11, 1)
counting(10, -1, -2)
print('Now you choose. enter:\n'
      'a - start\n'
      'b - finale\n'
      's - space')
aA = int(input('a - '))
bB = int(input('b - '))
sS = int(input('s - '))
counting(aA, bB, sS)

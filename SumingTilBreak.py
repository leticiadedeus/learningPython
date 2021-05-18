c = s = n = 0
while True:
    n = int(input('insert the number you want to sum\n'
                  'if you want to stop, insert 999: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'the sum is {s}')
print(f'you did insert {c} number')

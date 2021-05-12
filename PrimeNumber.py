n = int(input('number: '))
d = 0
for c in range(1, n+1):
    if n % c == 0:
        d = d + 1
if d > 2:
    print('não é primo')
else:
    print('PRIMO')
print(d)

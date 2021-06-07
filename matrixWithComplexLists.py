matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even = []
sumC = 0
for line in range(0, 3):
    for n in range(0, 3):
        matrix[line][n] = int(input(f'Number[{line}, {n}]: '))
for line in range(0, 3):
    for n in range(0, 3):
        print(f'[{matrix[line][n]:^5}]', end='')
    print()
for line in matrix:
    for n in line:
        if n % 2 == 0:
            even.append(n)
    sumC = sumC + line[2]
higherValue = max(matrix[1])
print(f'The even values inserted were: {even}')
print(f'The sum of the third column is {sumC}')
print(f'The higher value on the second line is {higherValue}')

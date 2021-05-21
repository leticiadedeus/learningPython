m = int(input('What value do you want withdraw? '))
n50 = n20 = n10 = n1 = 0
while m - 50 >= 0:
    n50 += 1
    m = m - 50
while m - 20 >= 0:
    n20 += 1
    m = m - 20
while m - 10 >= 0:
    n10 += 1
    m = m - 10
while m - 1 >= 0:
    n1 += 1
    m = m - 1
print(f'{n50} notes of 50\n'
      f'{n20} notes of 20\n'
      f'{n10} notes of 10\n'
      f'{n1} notes of 1')

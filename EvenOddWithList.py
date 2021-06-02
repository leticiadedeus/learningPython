values = []
odd = []
even = []
while True:
    n = (int(input('Insert the value: ')))
    values.append(n)
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
    yn = str(input('Want to continue?(n/y): '))
    if yn == 'n':
        break
print('All the numbers you inserted: ', values)
print('The even numbers you inserted', even)
print('The odd numbers you inserted',  odd)

numbers = [[], []]
while True:
    n = int(input('Tell me the number: '))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)
    yn = str(input('Want to continue?(y/n) ')).lower()
    if yn == 'n':
        break
print(numbers)
numbers[0].sort()
numbers[1].sort()
print(f'even = {numbers[0]}')
print(f'odd = {numbers[1]}')

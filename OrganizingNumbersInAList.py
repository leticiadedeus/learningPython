numbers = []
for c in range(1, 6):
    n = (int(input(f'Insert a number: ')))
    if c == 1 or n > numbers[-1]:
        numbers.append(n)
    else:
        pos = 0
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n)
                break
            pos += 1
print(numbers)

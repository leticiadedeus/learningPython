numbers = []
for c in range(1, 6):
    numbers.append(int(input(f'Insert the {c} number: ')))
h = max(numbers)
posH = numbers.index(h)
s = min(numbers)
posL = numbers.index(s)
print(f'The higher number is {h} that is on the {posH + 1} position,\n'
      f'The smaller number is {s} that is on the {posL + 1} position')


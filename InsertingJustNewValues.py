values = []
while True:
    n = (float(input('Insert the value: ')))
    if n not in values:
        values.append(n)
    yn = str(input('Want to continue?(y/n): ')).lower()
    if yn == 'n':
        break
values.sort()
print(values)

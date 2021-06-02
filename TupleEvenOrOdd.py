numbers = (int(input('Insert the first number: ')),
           int(input('Insert the second number: ')),
           int(input('Insert the third number: ')),
           int(input('Insert the fourth number: ')))
e = o = 0
for c in numbers:
    if c % 2 == 0:
        e += 1
    else:
        o +=1
print(f'You inserted {e} even numbers and {o} odd numbers')

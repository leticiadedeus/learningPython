import random

numbers = list()


def randomizing():
    for c in range(0, 5):
        n = random.randint(0, 10)
        numbers.append(n)
    print(f'The numbers are {numbers}')


def summing():
    sm = 0
    for i in numbers:
        if i % 2 == 0:
            sm = sm + i
    print(f'The sum of even numbers is {sm}')


randomizing()
summing()

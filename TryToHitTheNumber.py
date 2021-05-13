import random
n = random.randrange(0, 10)
# podia ser randint
print('-=-' * 20)
print('What number do you think the computer choose between 0 and 10?')
print('-=-' * 20)
n_user = int(input())
while n_user != n:
    print('try again')
    n_user = int(input())
print('YOU WIN, the number was {}'.format(n))

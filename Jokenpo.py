import random
import time
print('0 - rock \n'
      '1 - paper \n'
      '2 - scissors ')
user = int(input('Choose your fighter: '))
pc = random.randint(0, 2)
print('JO')
time.sleep(0.6)
print('KEN')
time.sleep(0.6)
print('PÔ')
time.sleep(0.6)
if user == pc:
    print('pc and user tied')
elif user == 0 and pc == 2:
    print('User wins, user was rock and pc was scissors')
elif user == 1 and pc == 0:
    print('User wins, user was paper and pc was rock')
elif user == 2 and pc == 1:
    print('User wins, user was scissors and pc was paper')
elif pc == 0 and user == 2:
    print('Pc wins, pc was rock and user was scissors')
elif pc == 1 and user == 0:
    print('Pc wins, pc was paper and user was rock')
elif user == 2 and pc == 1:
    print('Pc wins, pc was scissors and user was paper')

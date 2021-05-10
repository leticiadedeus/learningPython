import time
nUser = int(input('\033[30;107mHow many seconds do you want to count? \033[m'))
n = 1
for c in range(0, nUser):
    print(n)
    n = n + 1
    time.sleep(1)
print('\033[30;107mfinale\033[m')

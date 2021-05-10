n = int(input())
if n % 2 != 0:
    print('Weird')
else:
    if 2 <= n and n <= 5:
        print('Not Weird')
    else:
        if 6 <= n and n <= 20:
            print('Weird')
        else:
            print('Not Weird')

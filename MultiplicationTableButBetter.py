while True:
    t = int(input('insert what multiplication table do you wanna see\n'
                  'if you want to stop, insert a negative number'))
    if t < 0:
        break
    for c in range(0,11):
        print(f'{t} X {c} = {t * c}')

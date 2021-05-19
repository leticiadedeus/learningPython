h18 = m = fl20 = 0
while True:
    yn = str(input('want to insert?(y/n) ')).lower()
    if yn == 'n':
        break
    age = int(input('age: '))
    genre = str(input('genre(m, f, nb): ')).lower()
    if age > 18:
        h18 += 1
    if genre == 'm':
        m += 1
    if genre == 'f':
        if age < 20:
            fl20 += 1
print(f'+18 people = {h18}')
print(f'we had {m} men')
print(f'we had {fl20} women w lower than 20 age')

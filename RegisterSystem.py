person = dict()
people = list()
ages = women = 0

while True:
    person.clear()

    person['name'] = str(input('Name: '))
    person['age'] = int(input('Age: '))
    ages += person['age']
    person['genre'] = str(input('Genre[M/F/N]: ')).upper()

    if person['genre'] not in 'MFN':
        person['genre'] = str(input('Please try again. Genre[M/F/N]: ')).upper()

    if person['genre'] == 'F':
        women += 1
    people.append(person.copy())

    yn = str(input('Want to continue?(Y/N) ')).upper()
    if yn == 'N':
        break

print(f"You registered {len(people)} persons")
print('-=' * 30)
print(f"The average of them all ages is {ages / len(people)}")
print('-=' * 30)
print(f"You registered {women} women")
print('-=' * 30)
print("Persons with age higher than the average: ")
for i in people:
    if i['age'] >= ages / len(people):
        print(f"- {i['name']} with {i['age']} years old")

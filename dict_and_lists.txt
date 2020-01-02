tytuł_filmu = "Sami swoi"
wiek = 35
email = "anna.woznickaaa@gmail.com"
czy_lubie_pizze = True
print(type(tytuł_filmu))
print(type(wiek))
print(type(email))
print(type(czy_lubie_pizze))

print(f'Lubie film {tytuł_filmu}. '
      f'Mam lat {wiek}.Moj email to {email}.'
      f'Czy lubie pizze hawajską  {czy_lubie_pizze}.')

animals = ['dog', 'cat', 'fish']
numbers = [13, 44, 18.4]
print(animals[0])
print(numbers[2])
print(numbers[-1])
animals.append('elephant')
animals.append('monkey')
print(animals)
print(len(animals))
# to jest koment
numbers.append(137)
numbers.append(6.16)
numbers.append(0.02)

print(f'ilosc liczb: {len(numbers)}')
actor = {'name': "Johnny Depp",
         'age': 55,
         'country': "USA",
         'alive': True}

print(actor['name'])
print(actor['age'])
print(actor['country'])

friend = {'name': "Ania",
          'age': 36,
          'hobby': 'podroze'}
friend[email] = "jakiś@email.com"

print(friend)

friend = {'name': "Ania",
          'age': 36,
          'hobby': 'podroze'}

friend1 = {'name': "Basia",
           'age': 42,
           'hobby': 'gotowanie'}

friend2 = {'name': "Jola",
           'age': 45,
           'hobby': 'spanie'}

friends = [friend, friend1, friend2, ]

print(friends[0])  # jak wyciągnąć hobby?
print(friends[0]['hobby'])

temp = 21.5

if temp > 20:
    print("Idziemy na dwor!")
else:
    print('Zostajemy w domu :( ')

    temp = 20

    if temp > 20:
        print("Idziemy na dwor!")

    elif temp == 20:
        print("Robimy grilla!")  # elif stosujemy gdy jest więcej warunków!!

    else:
        print('Zostajemy w domu :( ')  # else musi być na końcu!!!

#brand = 'BMW'

"""if brand = 'BMW':
    print("czerwony")

elif brand = 'Skoda':
    print("zolty")

if brand = 'peugeot':
    print("pink")

else
    print("black")



grade = 4

if grade = 6:
    print("celujący")

elif grade < 6 and grade > 4:
    print("dobry")

elif
    grade < 3 and grade > 4:
    print("ok")

else
print("słabo")"""

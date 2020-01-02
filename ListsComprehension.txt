import math, random


# List comprehension

names = ['Ada', 'Bill', 'Yen', 'Geralt', 'Ksawery', 'Candice', 'Esmeralda']

# imiona

name_lenghts = [len(n) for n in names]     # tworzę listę zawierającą długości imion zawartch w liście "name"
print(name_lenghts)

names_upper = [ n.upper() for n in names]   # tworzę listę zawierającą imiona z listy "name",które są pisane dużymi literami
print(names_upper)



# promienie i pola

radii = [12.1, 33, 9.3, 0.2, 190, 22.5]

circle_areas = [ (math.pi * r**2) for r in radii]   # tworzę listę zawierającą pola kół, o promieniach "r" zawartych w liście "radii"
print(circle_areas)



# zniżki (dla chętnych :D )

discounts = [19, 21, -5.5, 7.8, 13.1, -10.2, -21, 10.1]
another_discounts= [d if d > 0 else 0 for d in discounts]
print(another_discounts)



# Metody
#psi generator

def random_doggo ():
    doggos = ['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']
    dog = random.choice(doggos)
    return dog


dog1 = random_doggo()
print(dog1)

dog2 = random_doggo()
print(dog2)



# matematyka
# metoda greater_of_pair

def greater_of_pair(a,b):
    if a > b:
        return a
    else:
        return b

result1= greater_of_pair(15,4)
print(result1)

result2= greater_of_pair(1,234)
print(result2)



# metoda average_of_3
def average_of_3(a,b,c):
    average = (a+b+c) / 3
    return int(average)

average1= average_of_3(4,5,6)
print(average1)

average2= average_of_3(300,20,415)
print(average2)



# brzegi listy
# metoda margins

def margins(input_list):
        if len(input_list) == 1:
            first_el = input_list[0]
            second_el= None
            return first_el, second_el
        elif len(input_list) == 0:
            first_el = None
            last_el = None
            print("List is empty!")
            return first_el, last_el
        else:
            first_el = input_list[0]
            last_el = input_list[-1]
            return first_el, last_el


names=['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']
print(margins(names))

numbers=[12.1, 33, 9.3, 0.2, 190, 22.5]
print(margins(numbers))

two_numbers=[3, 5]
print(margins(two_numbers))

list1= ['Piłka']
print(margins(list1))

list2=[2,]
print(margins(list2))

list3=[]
print(margins(list3))

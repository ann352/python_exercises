import random
class Player:

    def __init__(self, name, position, age):    # tworzę konstruktor klasy
        self._name = name
        self._position = position
        self._age = age
        self._goals  = 0
        self._field_number = 0
        self._cards = 0
        self._club= None

    @property       # tworzę gettery i settery
    def name(self):
        return self._name   # getter dla imienia i nazwiska

    @name.setter
    def name(self, value):
        self._name = value    # getter dla imienia i nazwiska

    @property
    def age(self):    # getter dla wieku gracza
        return self._age

    @age.setter
    def age(self, value):   # setter dla wieku gracza
        self._age = value

    @property
    def field_number(self):  # getter , nr na koszulce gracza
        return self._field_number

    @field_number.setter
    def field_number(self, value):  # setter, nr na koszulce gracza
        self._field_number = value

    @property
    def cards(self):  # getter dla l. czerwonych kartek gracza
        return self._cards

    @property
    def club(self):  # getter dla clubu gracza
        return self._club

    @property
    def position(self):  # getter dla pozycji gracza
        return self._position



    @property     # ustawiamy getter dla liczby goli
    def goals(self):
        return self._goals



    def score(self):       # funkcja zwiększająca liczbę strzelonych goli o 1, jeżeli zawodnik ma swój klub
        if self._club == None:
            print("Choose your club!")
            return self._goals

        else:
            self._goals += 1
            return self._goals



    def change_position(self, new_position): # funkcja pozwalająca na zmianę pozycji zawodnika (zwiększa też jego wiek o 2 lata po zmianie pozycji)
        self._position = new_position
        self._age += 2
        return self._position


    def transfer(self, club): # funkcja, która pozwala na zmianę klubu, ale ustawia jego dotychczasowe bramki na 0
        self._club = club
        self._goals = 0
        return self._club


    def foul(self): # funkcja, która daje 50% szans na otrzymanie kartki (stąd użycie pseudolosowej f-cji random.randint(0,1) )

        chance_for_card = random.randint(0,1)
        if chance_for_card ==1:
            self._cards += 1
            print("Got a card")
            return int(self._cards)




my_player = Player('Test Player', 'defender', 23)
print(my_player.age)
print(my_player.goals)
my_player.score()
print(my_player.goals)
my_player.transfer('Liverpool FC')
my_player.field_number = 7
my_player.score()
print(my_player.goals)
my_player.change_position('attacker')
print(my_player.age)
print(my_player.position)
my_player.foul()
my_player.foul()
my_player.foul()
print(my_player.cards)


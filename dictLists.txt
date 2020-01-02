import random


female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
lastname = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
country = ['Poland', 'United Kingdom', 'Germany', 'France', 'Italy']

lista_slownikow = []  # inicjuję pustą listę słowników

for i in range(0, 10):  # w pętli generuję wartości mające posłużyć do wypełnienia słownika

    if i % 2 == 0:   # if i <5:  first_name ... itd tak samo (bo 5 pierwszych to będą damskie // i to bylo poprawne
        # ternary operator if a>2 True else False, czyli      firstname = random.choice(male_fnames)  if a>2  else random_firstname = random.choice(male_fnames)
        random_firstname = random.choice(female_fnames)  # jeżeli licznik pętli jest liczbą parzystą losuję imię damskie
    else:
        random_firstname = random.choice(male_fnames)  # jeżeli  liczbą nieparzystą - męskie

    random_lastname = random.choice(lastname)  # losuję nazwisko

    if i % 2 == 0 and random_lastname == lastname[1]:
        random_lastname= 'Kowalski'.replace( 'Kowalski','Kowalska')

    # jeżeli wylosowane imię jest żeńskie i jednocześnie nazwisko  to 'Kowalski" - zmieniam  je na "Kowalska"

    random_country = random.choice(country)  # losuję kraj, czytamt to od prawej

    random_age = random.randint(5, 46)  # generuję wiek , bylo zle powinno byc od 5-45,,


    if random_age >= 18:  # tworzę blok if-else, który na podstawie wylosowanego wieku zadecyduje, czy dana osoba jest dorosła,czy nie
        is_adult = True
    else:
        is_adult = False  # lub   if adult >17    adult = True


    birth_year = 2019 - random_age  # na podstawie wylosowanego wieku obliczam rok urodzenia

    email = f'{random_firstname.lower()}.{random_lastname.lower()}@example.com'  # z wylosowanych danych tworzę pisany małymi literami email, można też zrobić to lower na całym stringu dopiero .lower()

    d = {"firstname": random_firstname, "lastname": random_lastname, "email": email,
         "age": random_age, "country": random_country, "birth_year": birth_year, "adult": is_adult}

    print(d)

    # tworzę słownik, nazywam poszczególne klucze i przypisuję im wylosowane wartości,

    lista_slownikow.append(d)  # za każdym przejściem pętli dołączam do listy_slownikow, kolejny słownik

print(lista_slownikow)  # wypisuję na ekran, otrzymaną w pętli listę słowników

for n in lista_slownikow:  # dla każdego elementu listy, czyli dla każdego słownika, generuję poniższy napis, tu nie korzystamy z range, zeby nie zmieniać danych w przypadku zmiany ilosci generowanych slownikow

    print(f'Hi! I\'m  {n["firstname"]} {n["lastname"]}. I come from {n["country"]} and I was '
          f'born in {n["birth_year"]}. I\'m {n["age"]} years old. '
          f'My email is: {n["email"]}')

    # dobrze rozkminiac to od konca -od momentu tworzenia słownika,

    #tworzymy pojedynczy lista_slownik
    # robimy petle dla 10 slownikow ( for in range (10), lub to co ja zrobilam
    # zle byloby na koncu zrobic petle, bo ona zbierze ostatnią wartosc
    # uwaga tez na wciecia, zeby nie zebralo tylko ostatniej danej

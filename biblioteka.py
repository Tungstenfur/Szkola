import json
try:
    with open('biblioteka.json', 'r') as file:
        ksiazki = json.load(file)
except FileNotFoundError:
    ksiazki = []
while True:
    print("==Menu Biblioteki==")
    print("1. Dodaj książkę")
    print("2. Wyświetl wszystkie książki")
    print("3. Wyszukaj książkę po tytule")
    print("4. Usuń książkę z kataologu")
    print("5. Zakończ program")
    op=input("Wybierz opcję: ")
    if op=="1":
        print("Dodawanie książkę")
        print("Podaj tytuł książki: ")
        tytul=input()
        print("Podaj autora książki: ")
        autor=input()
        print("Podaj rok wydania książki: ")
        rok=input()
        ksiazki.append('Tytuł: '+tytul+'; Autor: '+autor+'; Rok: '+rok)
        print("Książka dodana do katalogu")
        input("Naciśnij Enter aby kontynuować")
    elif op=="2":
        print("Wszystkie książki")
        for ksiazka in ksiazki:
            print(ksiazka)
        input("Naciśnij Enter aby kontynuować")
    elif op=="3":
        print("Wyszukiwanie książki")
        print("Podaj tytuł książki: ")
        tytul=input()
        for ksiazka in ksiazki:
            if tytul in ksiazka:
                print(ksiazka)
        input("Naciśnij Enter aby kontynuować")
    elif op=="4":
        print("Usuwanie książki")
        print("Podaj tytuł książki: ")
        tytul=input()
        for ksiazka in ksiazki:
            if tytul in ksiazka:
                conf=input("Czy na pewno chcesz usunąć książkę? (t/N): ")
                if conf=="t":
                    ksiazki.remove(ksiazka)
                    print("Książka usunięta z katalogu")
        input("Naciśnij Enter aby kontynuować")
    elif op=="5":
        with open('biblioteka.json', 'w') as file:
            json.dump(ksiazki, file)
        print("Katalog zapisany. Zakończenie programu.")
        break
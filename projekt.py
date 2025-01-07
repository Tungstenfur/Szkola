import random
liczba = random.randint(1,50)
zgadniete = False
while not zgadniete:
    odp = input("Podaj liczbę: ")
    if liczba == int(odp):
        print("Zgadłeś!")
        zgadniete = True
    elif liczba < int(odp):
        print("Za dużo!")
    else:
        print("Za mało!")
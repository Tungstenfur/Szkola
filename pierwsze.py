i = int(input("Podaj liczbę: "))
for j in range(2,i):
    if i % j == 0:
        print("Liczba",i,"nie jest liczbą pierwszą")
        exit()
print("Liczba",i,"jest liczbą pierwszą")
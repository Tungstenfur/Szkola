statystyki = {
    "DrużynaA": {"mecze": 0, "wygrane": 0, "remisy": 0, "porazki": 0, "bramki": 0},
    "DrużynaB": {"mecze": 0, "wygrane": 0, "remisy": 0, "porazki": 0, "bramki": 0},
    "DrużynaC": {"mecze": 0, "wygrane": 0, "remisy": 0, "porazki": 0, "bramki": 0},
    "DrużynaD": {"mecze": 0, "wygrane": 0, "remisy": 0, "porazki": 0, "bramki": 0}
}
with open('wyniki.txt', 'r') as file:
    for line in file:
        dane = line.strip().split(',')
        druzyna1, druzyna2, bramki1, bramki2 = dane[0], dane[1], int(dane[2]), int(dane[3])
        
        statystyki[druzyna1]["mecze"] += 1
        statystyki[druzyna2]["mecze"] += 1
        statystyki[druzyna1]["bramki"] += bramki1
        statystyki[druzyna2]["bramki"] += bramki2
        
        if bramki1 > bramki2:
            statystyki[druzyna1]["wygrane"] += 1
            statystyki[druzyna2]["porazki"] += 1
        elif bramki1 < bramki2:
            statystyki[druzyna1]["porazki"] += 1
            statystyki[druzyna2]["wygrane"] += 1
        else:
            statystyki[druzyna1]["remisy"] += 1
            statystyki[druzyna2]["remisy"] += 1

print("Statystyki drużyn:")
for druzyna, statystyka in statystyki.items():
    print(f"{druzyna}: Mecze: {statystyka['mecze']}, Wygrane: {statystyka['wygrane']}, Remisy: {statystyka['remisy']}, Porażki: {statystyka['porazki']}, Bramki: {statystyka['bramki']}")

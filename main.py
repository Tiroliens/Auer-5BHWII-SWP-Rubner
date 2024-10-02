import random
from collections import defaultdict

def lotto_ziehung():
    gezogene_zahlen = random.sample(range(1, 46), 6)
    print("Gezogene Lottozahlen: ", gezogene_zahlen)
    return gezogene_zahlen

def lotto_statistik(anzahl_ziehungen):
    statistik = defaultdict(int)

    for i in range(anzahl_ziehungen):
        gezogene_zahlen = lotto_ziehung()

        for zahl in gezogene_zahlen:
            statistik[zahl] += 1

    print("\nStatistik der Ziehungen:")
    for zahl in range(1, 46):
        print(f"{zahl}: {statistik[zahl]}x gezogen")

lotto_statistik(1000)

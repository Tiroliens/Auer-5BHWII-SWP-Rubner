import random
from collections import Counter

farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
deck = [(wert, farbe) for wert in werte for farbe in farben]

wert_rang = {wert: index for index, wert in enumerate(werte)}

def ziehe_fuenf_karten():
    return random.sample(deck, 5)

def ist_paar(karten):
    werte_der_karten = [karte[0] for karte in karten]
    zaehler = Counter(werte_der_karten)
    return max(zaehler.values()) == 2

def ist_drilling(karten):
    werte_der_karten = [karte[0] for karte in karten]
    zaehler = Counter(werte_der_karten)
    return max(zaehler.values()) == 3

def ist_vierling(karten):
    werte_der_karten = [karte[0] for karte in karten]
    zaehler = Counter(werte_der_karten)
    return max(zaehler.values()) == 4

def ist_full_house(karten):
    werte_der_karten = [karte[0] for karte in karten]
    zaehler = Counter(werte_der_karten).values()
    return sorted(zaehler) == [2, 3]

def ist_flush(karten):
    farben_der_karten = [karte[1] for karte in karten]
    return len(set(farben_der_karten)) == 1

def ist_straight(karten):
    werte_der_karten = sorted([wert_rang[karte[0]] for karte in karten])
    return werte_der_karten == list(range(min(werte_der_karten), min(werte_der_karten) + 5))

def ist_straight_flush(karten):
    return ist_flush(karten) and ist_straight(karten)

def ist_royal_flush(karten):
    werte_der_karten = sorted([karte[0] for karte in karten])
    return ist_straight_flush(karten) and werte_der_karten == ['10', 'Bube', 'Dame', 'König', 'Ass']

def poker_simulation(anzahl_spiele=100000):
    kombinationen_zaehler = {
        'Paar': 0,
        'Drilling': 0,
        'Vierling': 0,
        'Full House': 0,
        'Flush': 0,
        'Straight': 0,
        'Straight Flush': 0,
        'Royal Flush': 0,
    }

    for _ in range(anzahl_spiele):
        karten = ziehe_fuenf_karten()

        if ist_royal_flush(karten):
            kombinationen_zaehler['Royal Flush'] += 1
        elif ist_straight_flush(karten):
            kombinationen_zaehler['Straight Flush'] += 1
        elif ist_vierling(karten):
            kombinationen_zaehler['Vierling'] += 1
        elif ist_full_house(karten):
            kombinationen_zaehler['Full House'] += 1
        elif ist_flush(karten):
            kombinationen_zaehler['Flush'] += 1
        elif ist_straight(karten):
            kombinationen_zaehler['Straight'] += 1
        elif ist_drilling(karten):
            kombinationen_zaehler['Drilling'] += 1
        elif ist_paar(karten):
            kombinationen_zaehler['Paar'] += 1

    for kombination, anzahl in kombinationen_zaehler.items():
        prozent = (anzahl / anzahl_spiele) * 100
        print(f"{kombination}: {anzahl} ({prozent:.2f}%)")

poker_simulation()

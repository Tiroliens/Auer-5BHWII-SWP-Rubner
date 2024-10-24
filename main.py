import random
from collections import Counter

farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
deck = [(wert, farbe) for wert in werte for farbe in farben]

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

def ist_strasse(karten):
    werte_der_karten = [karte[0] for karte in karten]
    werte_rang = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    karten_rang = sorted([werte_rang.index(wert) for wert in werte_der_karten])
    return karten_rang == list(range(min(karten_rang), max(karten_rang) + 1))

def ist_straight_flush(karten):
    return ist_strasse(karten) and ist_flush(karten)

def poker_simulation(anzahl_spiele=100000):
    kombinationen_zaehler = {
        'Paar': 0,
        'Drilling': 0,
        'Vierling': 0,
        'Full House': 0,
        'Flush': 0,
        'Straße': 0,
        'Straight Flush': 0
    }

    for _ in range(anzahl_spiele):
        karten = ziehe_fuenf_karten()

        if ist_straight_flush(karten):
            kombinationen_zaehler['Straight Flush'] += 1
        elif ist_vierling(karten):
            kombinationen_zaehler['Vierling'] += 1
        elif ist_full_house(karten):
            kombinationen_zaehler['Full House'] += 1
        elif ist_flush(karten):
            kombinationen_zaehler['Flush'] += 1
        elif ist_strasse(karten):
            kombinationen_zaehler['Straße'] += 1
        elif ist_drilling(karten):
            kombinationen_zaehler['Drilling'] += 1
        elif ist_paar(karten):
            kombinationen_zaehler['Paar'] += 1

    for kombination, anzahl in kombinationen_zaehler.items():
        prozent = (anzahl / anzahl_spiele) * 100
        print(f"{kombination}: {anzahl} ({prozent:.2f}%)")

poker_simulation()

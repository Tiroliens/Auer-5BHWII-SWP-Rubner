import random
from collections import Counter

def erstelle_deck():
    """Erstellt ein Kartendeck."""
    farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
    werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    return [(werte, farbe) for werte in werte for farbe in farben], {werte: index for index, werte in enumerate(werte)}

def ziehe_fuenf_karten(deck):
    """Zieht fünf zufällige Karten aus dem Deck."""
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

def ist_straight(karten, werte):
    werte_der_karten = sorted([werte[karte[0]] for karte in karten])
    return werte_der_karten == list(range(min(werte_der_karten), min(werte_der_karten) + 5))

def ist_straight_flush(karten, werte):
    return ist_flush(karten) and ist_straight(karten, werte)

def ist_royal_flush(karten, werte):
    werte_der_karten = sorted([karte[0] for karte in karten])
    return ist_straight_flush(karten, werte) and werte_der_karten == ['10', 'Bube', 'Dame', 'König', 'Ass']

def poker_simulation(anzahl_spiele, deck, werte):
    """Simuliert eine Poker-Runde."""
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
        karten = ziehe_fuenf_karten(deck)

        if ist_royal_flush(karten, werte):
            kombinationen_zaehler['Royal Flush'] += 1
        elif ist_straight_flush(karten, werte):
            kombinationen_zaehler['Straight Flush'] += 1
        elif ist_vierling(karten):
            kombinationen_zaehler['Vierling'] += 1
        elif ist_full_house(karten):
            kombinationen_zaehler['Full House'] += 1
        elif ist_flush(karten):
            kombinationen_zaehler['Flush'] += 1
        elif ist_straight(karten, werte):
            kombinationen_zaehler['Straight'] += 1
        elif ist_drilling(karten):
            kombinationen_zaehler['Drilling'] += 1
        elif ist_paar(karten):
            kombinationen_zaehler['Paar'] += 1

    ergebnisse = {}
    for kombination, anzahl in kombinationen_zaehler.items():
        prozent = (anzahl / anzahl_spiele) * 100
        ergebnisse[kombination] = f"{anzahl} ({prozent:.2f}%)"

    return ergebnisse

def main():
    deck, werte = erstelle_deck()
    anzahl_spiele = int(input("Wie viele Spiele sollen simuliert werden? "))
    ergebnisse = poker_simulation(anzahl_spiele, deck, werte)
    for kombination, statistik in ergebnisse.items():
        print(f"{kombination}: {statistik}")

if __name__ == "__main__":
    main()

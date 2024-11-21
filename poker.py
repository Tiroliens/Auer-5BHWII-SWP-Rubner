import random
from collections import Counter

def erstelle_deck():
    """Erstellt ein Kartendeck."""
    farben = ['Herz', 'Karo', 'Pik', 'Kreuz']  # Vier Farben eines Standard-Kartenspiels
    werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']  # Kartenwerte von niedrig bis hoch
    # Kombiniert alle Werte mit allen Farben und erstellt zusätzlich ein Mapping für die Werte
    return [(werte, farbe) for werte in werte for farbe in farben], {werte: index for index, werte in enumerate(werte)}

def ziehe_fuenf_karten(deck):
    """Zieht fünf zufällige Karten aus dem Deck."""
    return random.sample(deck, 5)  # Wählt zufällig fünf Karten aus dem Deck ohne Wiederholung

def ist_paar(karten):
    """Überprüft, ob die Karten ein Paar enthalten."""
    werte_der_karten = [karte[0] for karte in karten]  # Extrahiert die Werte der Karten
    zaehler = Counter(werte_der_karten)  # Zählt die Häufigkeit jedes Wertes
    return max(zaehler.values()) == 2  # Prüft, ob ein Wert genau zweimal vorkommt

def ist_drilling(karten):
    """Überprüft, ob die Karten einen Drilling enthalten."""
    werte_der_karten = [karte[0] for karte in karten]
    zaehler = Counter(werte_der_karten)
    return max(zaehler.values()) == 3  # Prüft, ob ein Wert genau dreimal vorkommt

def ist_vierling(karten):
    """Überprüft, ob die Karten einen Vierling enthalten."""
    werte_der_karten = [karte[0] for karte in karten]
    zaehler = Counter(werte_der_karten)
    return max(zaehler.values()) == 4  # Prüft, ob ein Wert genau viermal vorkommt

def ist_full_house(karten):
    """Überprüft, ob die Karten ein Full House enthalten (ein Drilling und ein Paar)."""
    werte_der_karten = [karte[0] for karte in karten]
    zaehler = Counter(werte_der_karten).values()  # Zählt die Häufigkeiten der Kartenwerte
    return sorted(zaehler) == [2, 3]  # Prüft, ob ein Paar und ein Drilling vorhanden sind

def ist_flush(karten):
    """Überprüft, ob alle Karten die gleiche Farbe haben."""
    farben_der_karten = [karte[1] for karte in karten]  # Extrahiert die Farben der Karten
    return len(set(farben_der_karten)) == 1  # Prüft, ob alle Karten dieselbe Farbe haben

def ist_straight(karten, werte):
    """Überprüft, ob die Karten eine aufeinanderfolgende Reihenfolge bilden."""
    werte_der_karten = sorted([werte[karte[0]] for karte in karten])  # Ordnet die Kartenwerte numerisch
    return werte_der_karten == list(range(min(werte_der_karten), min(werte_der_karten) + 5))  # Prüft, ob die Werte aufeinanderfolgen

def ist_straight_flush(karten, werte):
    """Überprüft, ob die Karten eine Straight Flush bilden (aufeinanderfolgende Reihenfolge und gleiche Farbe)."""
    return ist_flush(karten) and ist_straight(karten, werte)  # Kombination aus Straight und Flush

def ist_royal_flush(karten, werte):
    """Überprüft, ob die Karten eine Royal Flush bilden (10, Bube, Dame, König, Ass in gleicher Farbe)."""
    werte_der_karten = sorted([karte[0] for karte in karten])  # Extrahiert die Werte der Karten
    return ist_straight_flush(karten, werte) and werte_der_karten == ['10', 'Bube', 'Dame', 'König', 'Ass']  # Prüft auf Royal Flush

def poker_simulation(anzahl_spiele, deck, werte):
    """Simuliert eine Poker-Runde."""
    # Initialisiert einen Zähler für alle möglichen Poker-Kombinationen
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

    # Wiederholt die Simulation für die angegebene Anzahl von Spielen
    for _ in range(anzahl_spiele):
        karten = ziehe_fuenf_karten(deck)  # Zieht fünf Karten zufällig

        # Prüft auf alle möglichen Pokerkombinationen, beginnend mit der seltensten
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

    # Berechnet die Ergebnisse in Prozent und gibt sie zurück
    ergebnisse = {}
    for kombination, anzahl in kombinationen_zaehler.items():
        prozent = (anzahl / anzahl_spiele) * 100  # Prozentsatz für jede Kombination
        ergebnisse[kombination] = f"{anzahl} ({prozent:.2f}%)"  # Formatiert die Ergebnisse

    return ergebnisse

def main():
    """Hauptfunktion für die Poker-Simulation."""
    deck, werte = erstelle_deck()  # Erstellt ein Deck und die Werte-Mapping
    anzahl_spiele = int(input("Wie viele Spiele sollen simuliert werden? "))  # Fragt die Anzahl der Simulationen ab
    ergebnisse = poker_simulation(anzahl_spiele, deck, werte)  # Führt die Simulation durch
    for kombination, statistik in ergebnisse.items():
        print(f"{kombination}: {statistik}")  # Gibt die Ergebnisse aus

if __name__ == "__main__":
    main()  # Startet die Hauptfunktion

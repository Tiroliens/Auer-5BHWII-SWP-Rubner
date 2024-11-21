import unittest
from collections import Counter
from unittest.mock import patch
from poker import (  # Importiert die zu testenden Funktionen aus der `poker`-Moduldatei
    erstelle_deck,
    ziehe_fuenf_karten,
    ist_paar,
    ist_drilling,
    ist_vierling,
    ist_full_house,
    ist_flush,
    ist_straight,
    ist_straight_flush,
    ist_royal_flush,
    poker_simulation,
)


class TestPokerFunctions(unittest.TestCase):
    """Testklasse für die Poker-Funktionen."""

    def setUp(self):
        """Setzt gemeinsame Testressourcen wie Deck und Werte-Mapping auf."""
        self.deck, self.wert = erstelle_deck()

    def test_erstelle_deck(self):
        """Testet die Erstellung des Kartendecks."""
        deck, wert = erstelle_deck()
        self.assertEqual(len(deck), 52)  # Überprüft, ob das Deck 52 Karten enthält
        self.assertEqual(len(wert), 13)  # Überprüft, ob 13 Kartenwerte korrekt zugeordnet wurden
        self.assertIn(('Ass', 'Herz'), deck)  # Überprüft, ob eine bestimmte Karte im Deck vorhanden ist

    @patch('random.sample')  # Mockt die Funktion `random.sample`, um vorhersagbare Ergebnisse zu testen
    def test_ziehe_fuenf_karten(self, mock_sample):
        """Testet das Ziehen von fünf Karten."""
        mock_sample.return_value = [  # Definiert die Rückgabewerte des Mock-Objekts
            ('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')
        ]
        karten = ziehe_fuenf_karten(self.deck)
        self.assertEqual(len(karten), 5)  # Überprüft, ob genau fünf Karten gezogen wurden
        self.assertEqual(karten[0], ('2', 'Herz'))  # Überprüft, ob die erste Karte der erwarteten entspricht

    def test_ist_paar(self):
        """Testet die Erkennung eines Paars."""
        karten = [('2', 'Herz'), ('2', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(ist_paar(karten))  # Soll `True` zurückgeben, da ein Paar vorhanden ist
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_paar(karten))  # Soll `False` zurückgeben, da kein Paar vorhanden ist

    def test_ist_drilling(self):
        """Testet die Erkennung eines Drillings."""
        karten = [('2', 'Herz'), ('2', 'Karo'), ('2', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(ist_drilling(karten))  # Soll `True` zurückgeben, da ein Drilling vorhanden ist
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_drilling(karten))  # Soll `False` zurückgeben, da kein Drilling vorhanden ist

    def test_ist_vierling(self):
        """Testet die Erkennung eines Vierlings."""
        karten = [('2', 'Herz'), ('2', 'Karo'), ('2', 'Pik'), ('2', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(ist_vierling(karten))  # Soll `True` zurückgeben, da ein Vierling vorhanden ist
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_vierling(karten))  # Soll `False` zurückgeben, da kein Vierling vorhanden ist

    def test_ist_full_house(self):
        """Testet die Erkennung eines Full House."""
        karten = [('2', 'Herz'), ('2', 'Karo'), ('3', 'Pik'), ('3', 'Kreuz'), ('3', 'Herz')]
        self.assertTrue(ist_full_house(karten))  # Soll `True` zurückgeben, da ein Full House vorhanden ist
        karten = [('2', 'Herz'), ('2', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_full_house(karten))  # Soll `False` zurückgeben, da kein Full House vorhanden ist

    def test_ist_flush(self):
        """Testet die Erkennung eines Flush."""
        karten = [('2', 'Herz'), ('3', 'Herz'), ('4', 'Herz'), ('5', 'Herz'), ('6', 'Herz')]
        self.assertTrue(ist_flush(karten))  # Soll `True` zurückgeben, da alle Karten dieselbe Farbe haben
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_flush(karten))  # Soll `False` zurückgeben, da nicht alle Karten dieselbe Farbe haben

    def test_ist_straight(self):
        """Testet die Erkennung eines Straight."""
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(ist_straight(karten, self.wert))  # Soll `True` zurückgeben, da die Karten aufeinander folgen
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('7', 'Herz')]
        self.assertFalse(ist_straight(karten, self.wert))  # Soll `False` zurückgeben, da keine aufeinanderfolgende Reihenfolge existiert

    def test_ist_straight_flush(self):
        """Testet die Erkennung eines Straight Flush."""
        karten = [('2', 'Herz'), ('3', 'Herz'), ('4', 'Herz'), ('5', 'Herz'), ('6', 'Herz')]
        self.assertTrue(ist_straight_flush(karten, self.wert))  # Soll `True` zurückgeben, da ein Straight Flush vorliegt
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_straight_flush(karten, self.wert))  # Soll `False` zurückgeben, da kein Straight Flush vorliegt

    def test_ist_royal_flush(self):
        """Testet die Erkennung eines Royal Flush."""
        karten = [('10', 'Herz'), ('Bube', 'Herz'), ('Dame', 'Herz'), ('König', 'Herz'), ('Ass', 'Herz')]
        self.assertTrue(ist_royal_flush(karten, self.wert))  # Soll `True` zurückgeben, da ein Royal Flush vorliegt
        karten = [('10', 'Herz'), ('Bube', 'Herz'), ('Dame', 'Herz'), ('König', 'Karo'), ('Ass', 'Herz')]
        self.assertFalse(ist_royal_flush(karten, self.wert))  # Soll `False` zurückgeben, da kein Royal Flush vorliegt

    def test_poker_simulation(self):
        """Testet die Poker-Simulation."""
        ergebnisse = poker_simulation(1000, self.deck, self.wert)  # Führt eine Simulation mit 1000 Spielen durch
        self.assertTrue(isinstance(ergebnisse, dict))  # Überprüft, ob die Ergebnisse ein Dictionary sind
        self.assertIn('Paar', ergebnisse)  # Überprüft, ob "Paar" im Ergebnis enthalten ist


if __name__ == '__main__':
    unittest.main()  # Führt die Tests aus

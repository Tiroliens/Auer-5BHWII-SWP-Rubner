import unittest
from collections import Counter
from unittest.mock import patch
from poker import (
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

    def setUp(self):
        self.deck, self.wert = erstelle_deck()

    def test_erstelle_deck(self):
        deck, wert = erstelle_deck()
        self.assertEqual(len(deck), 52)
        self.assertEqual(len(wert), 13)
        self.assertIn(('Ass', 'Herz'), deck)

    @patch('random.sample')
    def test_ziehe_fuenf_karten(self, mock_sample):
        mock_sample.return_value = [
            ('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')
        ]
        karten = ziehe_fuenf_karten(self.deck)
        self.assertEqual(len(karten), 5)
        self.assertEqual(karten[0], ('2', 'Herz'))

    def test_ist_paar(self):
        karten = [('2', 'Herz'), ('2', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(ist_paar(karten))
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_paar(karten))

    def test_ist_drilling(self):
        karten = [('2', 'Herz'), ('2', 'Karo'), ('2', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(ist_drilling(karten))
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_drilling(karten))

    def test_ist_vierling(self):
        karten = [('2', 'Herz'), ('2', 'Karo'), ('2', 'Pik'), ('2', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(ist_vierling(karten))
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_vierling(karten))

    def test_ist_full_house(self):
        karten = [('2', 'Herz'), ('2', 'Karo'), ('3', 'Pik'), ('3', 'Kreuz'), ('3', 'Herz')]
        self.assertTrue(ist_full_house(karten))
        karten = [('2', 'Herz'), ('2', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_full_house(karten))

    def test_ist_flush(self):
        karten = [('2', 'Herz'), ('3', 'Herz'), ('4', 'Herz'), ('5', 'Herz'), ('6', 'Herz')]
        self.assertTrue(ist_flush(karten))
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_flush(karten))

    def test_ist_straight(self):
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(ist_straight(karten, self.wert))
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('7', 'Herz')]
        self.assertFalse(ist_straight(karten, self.wert))

    def test_ist_straight_flush(self):
        karten = [('2', 'Herz'), ('3', 'Herz'), ('4', 'Herz'), ('5', 'Herz'), ('6', 'Herz')]
        self.assertTrue(ist_straight_flush(karten, self.wert))
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertFalse(ist_straight_flush(karten, self.wert))

    def test_ist_royal_flush(self):
        karten = [('10', 'Herz'), ('Bube', 'Herz'), ('Dame', 'Herz'), ('König', 'Herz'), ('Ass', 'Herz')]
        self.assertTrue(ist_royal_flush(karten, self.wert))
        karten = [('10', 'Herz'), ('Bube', 'Herz'), ('Dame', 'Herz'), ('König', 'Karo'), ('Ass', 'Herz')]
        self.assertFalse(ist_royal_flush(karten, self.wert))

    def test_poker_simulation(self):
        ergebnisse = poker_simulation(1000, self.deck, self.wert)
        self.assertTrue(isinstance(ergebnisse, dict))
        self.assertIn('Paar', ergebnisse)


if __name__ == '__main__':
    unittest.main()

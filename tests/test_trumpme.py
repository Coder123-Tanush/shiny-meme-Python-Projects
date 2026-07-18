import unittest

import trumpme


class TrumpMeTests(unittest.TestCase):
    def test_normalise_attribute_accepts_shortcuts_and_full_names(self):
        mapping = {'M': 'Magic', 'C': 'Cunning', 'CO': 'Courage', 'W': 'Wisdom', 'T': 'Temper'}
        self.assertEqual(trumpme.normalise_attribute('magic', mapping), 'M')
        self.assertEqual(trumpme.normalise_attribute('M', mapping), 'M')
        self.assertEqual(trumpme.normalise_attribute('Cunning', mapping), 'C')

    def test_choose_attribute_returns_a_valid_shortcut(self):
        mapping = {'M': 'Magic', 'C': 'Cunning', 'W': 'Wisdom'}
        chosen = trumpme.choose_attribute(mapping, is_player_turn=False)
        self.assertIn(chosen, mapping)


if __name__ == "__main__":
    unittest.main()

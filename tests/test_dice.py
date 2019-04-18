from random import Random
import unittest

from shadowdice import dice

class TestDice(unittest.TestCase):

    def test_10d6(self):
        target = [1, 5, 2, 4, 2, 1, 5, 3, 6, 2]
        test_dice = dice.Dice(10, 6, random_seed=1974)
        self.assertTrue(test_dice.evaluate() == target)

    def test_0d6(self):
        target = []
        test_dice = dice.Dice(0, 6, random_seed=1974)
        self.assertTrue(test_dice.evaluate() == target)

    def test_10d0(self):
        target = []
        test_dice = dice.Dice(10, 0, random_seed=1974)
        self.assertTrue(test_dice.evaluate() == target)

    def test_0d0(self):
        target = []
        test_dice = dice.Dice(0, 0, random_seed=1974)
        self.assertTrue(test_dice.evaluate() == target)

    def test_negativedice(self):
        target = []
        test_dice = dice.Dice(-1, -1, random_seed=1974)
        self.assertTrue(test_dice.evaluate() == target)

    def test_10d1(self):
        target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        test_dice = dice.Dice(10, 1, random_seed=1974)
        self.assertTrue(test_dice.evaluate() == target)
    
    def test_10d6_override(self):
        target = [1, 5, 8, 128, 8, 1, 5, -5, 6, 8]
        test_dice = dice.Dice(10,
                    6,
                    sides_override={'2': 8,
                                    '3': -5,
                                    '4': 128},
                    random_seed=1974)
        self.assertTrue(test_dice.evaluate() == target)


if __name__ == '__main__':
    unittest.main()

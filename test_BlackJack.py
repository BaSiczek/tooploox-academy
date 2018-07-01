import unittest
import BlackJack

class TestBlackJack(unittest.TestCase):
    def test_getting_str_from_class(self):
        result = str(BlackJack.Player('Bob', 3000))
        self.assertEqual(result, 'Bob Your current balance is: 300')

if __name__ == '__main__':
    unittest.main()

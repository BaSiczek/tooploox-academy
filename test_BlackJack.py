import unittest
import BlackJack

class TestBlackJack(unittest.TestCase):


    def test_getting_str_from_class(self):
        player = BlackJack.Player('Bob', 3000)
        result = str(player)
        self.assertEqual(result, 'Bob your current balance is: 3000')

    def test__boundary_bet_max_check_balance(self):
        player = BlackJack.Player('Bob', 3000)
        player.bet(3000)
        result = player.balance
        self.assertEqual(result, 0)
    def test__boundary_insufficient_balance(self):
        player = BlackJack.Player('Bob', 3000)
        result = player.bet(3001)
        self.assertEqual(result, 'Insufficient balance')


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
import dice

class TestDice(unittest.TestCase):

## test for user losing. set the mock_roll(random int) as 4.
## should return as false
    @patch('dice.roll', return_value=3)
    def test_play_user_wins(self, mock_roll):
        self.assertFalse(dice.play())

## test for user losing. set the mock_roll(random int) as 6.
## should return as true
    @patch('dice.roll', return_value=6)
    def test_play_user_wins(self, mock_roll):
        self.assertTrue(dice.play())

## test for winning print message with the mock_roll set to 6
    @patch('dice.roll', return_value=6)
    @patch('builtins.print')
    def test_main_user_wins(self, mock_print, mock_roll):
        dice.main()
        ## assert print called 'you win'
        mock_print.assert_any_call('You win!')

## test for losing print message with mock_roll set to 4
    @patch('dice.roll', return_value=3)
    @patch('builtins.print')
    def test_main_user_loses(self, mock_print, mock_roll):
        dice.main()
        ## assert any print called you lose
        mock_print.assert_any_call('you Lose!')

## test to make sure roll function works. set mock_roll value to 4
    @patch('random.randint', return_value=4)
    def test_roll(self, mock_random):
        self.assertTrue(4, dice.roll())
import unittest
import logging
from biggestloss import biggest_loss


class TestBiggestLoss(unittest.TestCase):
    logging.info("Unit test started.")

    def test_biggest_loss(self):
        # Given
        empty_list = []
        # If I read correctly, in the given input to the function,
        # index1 < index 2 always.
        sell_greater_than_buy = [23.56, 52.89, 87.45, 3.00, 88.45, 89.46, 43.98, 45.78]
        not_even_price_list = [23.67, 34.45, 67.56]
        single_price = [2.00]
        price_list = [23.56, 52.89, 3.00, 87.45, 88.45, 89.46, 43.98, 45.78]
        price_map = {'sell': 23.56, 'buy': 52.89}

        # When
        given_empty_list = biggest_loss(empty_list)
        given_sell_less_than_buy_prices = biggest_loss(sell_greater_than_buy)
        given_not_even_price_list = biggest_loss(not_even_price_list)
        given_single_price_list = biggest_loss(single_price)
        given_price_list = biggest_loss(price_list)
        given_price_map = biggest_loss(price_map)

        # Then
        # These tests are assuming that you want 0 to be returned instead of an
        # exception thrown
        self.assertEqual(given_empty_list, 0)
        self.assertEqual(given_sell_less_than_buy_prices, 0)
        self.assertEqual(given_not_even_price_list, 0)
        self.assertEqual(given_single_price_list, 0)
        self.assertEqual(given_price_map, 0)
        # Test that the function actually work
        # The biggest lost should be the difference between sell: 3.00 buy: 87.45
        self.assertEqual(given_price_list, 84.45)
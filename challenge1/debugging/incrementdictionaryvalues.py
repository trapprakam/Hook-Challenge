from unittest import TestCase


def increment_dictionary_values(d: dict, i: int) -> dict:
    """
    Increment the integer value stored in the given dictionary
    by the integer value passed to this function
    the function
    :param d: A dictionary with a single key, value entry
    :param i: An integer used to increment the value stored in the given dictionary
    :return: A dictionary that stores the result of the incrementation with its respective key
    """
    # Solution: Initialize a new dictionary object to
    # return result of incrementation. A new dictionary object is
    # needed because python is pass by reference
    to_return = dict()
    for key, value in d.items():
        to_return[key] = value + i
    return to_return


class TestIncrementDictionaryValue(TestCase):

    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)

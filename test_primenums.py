import unittest

from primenumbers import is_prime
from primenumbers import prime_generator


class PrimeTestCase(unittest.TestCase):
    # start by testing the is_prime function to ensure it's all good as its used by the prime_generator function

    def test_is_0_prime(self):
        """ Zero is not a prime number"""
        self.assertFalse(is_prime(0), msg="Your function failed on test case for 0")

    def test_is_5_prime(self):
        """ Five is a prime number"""
        self.assertTrue(is_prime(5), msg="Your function failed to give the correct output for 5")

    def test_is_2_prime(self):
        """ Two is the only even prime number and should return true """
        self.assertTrue(is_prime(2), msg="Your function failed to give the correct output for 2")

    def test_is_4_prime(self):
        """ Four is an even number hence not prime"""
        self.assertFalse(is_prime(4), msg="Your function failed to give the correct output for 4")

    def test_negative_num(self):
        """ Negative numbers should not be accepted"""
        for index in range(-1, -10, -1):
            self.assertFalse(prime_generator(index), msg='{} is a negative number and hence isn\'t prime'.format(index))

    def test_input_type(self):
        self.


if __name__ == '__main__':
    unittest.main()

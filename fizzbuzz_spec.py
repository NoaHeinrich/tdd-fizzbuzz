import unittest
from fizzbuzz import fizzbuzz

class FizzbuzzTestCase(unittest.TestCase):
    # tests for fizzbuzz.py
    def test_returns_an_array(self):
        self.assertEqual(type(fizzbuzz(100)), list)
    
    def test_returns_100_length_array(self):
        fizzbuzz_array = fizzbuzz(100)
        self.assertEqual(len(fizzbuzz_array), 100)

    def test_third_element_is_fizz(self):
        print(fizzbuzz(5))
        self.assertEqual(fizzbuzz(100)[2], "Fizz")
    
    def test_fifth_element_is_buzz(self):
        self.assertEqual(fizzbuzz(100)[4], "Buzz")

    def test_fifteenth_element_is_fizzbuzz(self):
        self.assertEqual(fizzbuzz(100)[14], "Fizzbuzz")
    
    def test_output_is_fizzbuzz(self):
        fb = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizzbuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizzbuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "Fizzbuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, "Fizzbuzz", 61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "Fizzbuzz", 76, 77, "Fizz", 79, "Buzz","Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 88, 89, "Fizzbuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz"]
        self.assertEqual(fizzbuzz(100), fb)  

if __name__ == '__main__':
    unittest.main()
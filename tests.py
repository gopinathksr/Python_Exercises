import unittest
import collections
from datetime import datetime
from lru import user_page
from anagrams import is_anagram
from lottery import next_result_datetime


class TestNextResultDateTime(unittest.TestCase):

    def setUp(self):
        self.test1 = datetime(2016, 6, 26, 19, 0, 0)  # Sunday    7 PM
        self.test2 = datetime(2016, 6, 27, 19, 0, 0)  # Monday    7 PM
        self.test3 = datetime(2016, 6, 28, 19, 0, 0)  # Tuesday   7 PM
        # Test 4 : Here the assuption is our result are updated sharp
        # 8:00PM in to clous, so by default this is the point
        # where ticks for next draw starts.
        self.test4 = datetime(2016, 6, 29, 20, 0, 0)  # Wednesday 8 PM
        self.test5 = datetime(2016, 6, 30, 19, 0, 0)  # Thursday  7 PM
        self.test6 = datetime(2016, 7, 1,  20, 0, 0)  # Friday    8 PM
        self.test7 = datetime(2016, 7, 2,  19, 0, 0)  # Saturday  7 PM
        self.test8 = datetime(2016, 7, 2,  21, 0, 0)  # Saturday  9 PM
        self.result1 = datetime(2016, 6, 29,  20, 0, 0)  # Wednesday 8 PM
        self.result2 = datetime(2016, 6, 29,  20, 0, 0)  # Wednesday 8 PM
        self.result3 = datetime(2016, 6, 29,  20, 0, 0)  # Wednesday 8 PM
        self.result4 = datetime(2016, 7, 02,  20, 0, 0)  # Saturday  8 PM
        self.result5 = datetime(2016, 7, 02,  20, 0, 0)  # Saturday  8 PM
        self.result6 = datetime(2016, 7, 02,  20, 0, 0)  # Saturday  8 PM
        self.result7 = datetime(2016, 7, 02,  20, 0, 0)  # Saturday  8 PM
        self.result8 = datetime(2016, 7, 06,  20, 0, 0)  # Saturday  8 PM

    def test(self):
        self.assertEqual(next_result_datetime(self.test1), self.result1)
        self.assertEqual(next_result_datetime(self.test2), self.result2)
        self.assertEqual(next_result_datetime(self.test3), self.result3)
        self.assertEqual(next_result_datetime(self.test4), self.result4)
        self.assertEqual(next_result_datetime(self.test5), self.result5)
        self.assertEqual(next_result_datetime(self.test6), self.result6)
        self.assertEqual(next_result_datetime(self.test7), self.result7)
        self.assertEqual(next_result_datetime(self.test8), self.result8)


class TestIsAnagram(unittest.TestCase):

    def setUp(self):
        self.test1 = ["Rambo", ["Ambro", "Orbam", "Mabor", "MMabor"], ["Ambro", "Orbam", "Mabor"]]
        self.test2 = ["1234", ["2314", "4321", "11243", "11223344"], ["2314", "4321"]]
        self.test3 = [None, ["Ambro", "Orbam", "Mabor", "MMabor"], None]
        self.test4 = ["Rambo", None, None]
        self.test5 = [None, None, None]

    def test(self):
        self.assertEqual(is_anagram(self.test1[0], self.test1[1]), self.test1[2])
        self.assertEqual(is_anagram(self.test2[0], self.test2[1]), self.test2[2])
        self.assertEqual(is_anagram(self.test3[0], self.test3[1]), self.test3[2])
        self.assertEqual(is_anagram(self.test4[0], self.test4[1]), self.test4[2])
        self.assertEqual(is_anagram(self.test5[0], self.test5[1]), self.test5[2])


class UserPageTest(unittest.TestCase):

    def setUp(self):
        self.test1 = 1
        self.test2 = 2
        self.test3 = 3
        self.test4 = 4  # test 1 to 4 show the order of keys in Cache
        self.test5 = 5  # test to validate removal of LRU and update
        self.test6 = 3  # reshuffling cache
        self.test7 = 2  # reshuffling cache
        self.test8 = 10  # updating new page
        self.test9 = 10  # no change in cache
        self.result1 = collections.OrderedDict([(1, 1)])
        self.result2 = collections.OrderedDict([(1, 1), (2, 4)])
        self.result3 = collections.OrderedDict([(1, 1), (2, 4), (3, 9)])
        self.result4 = collections.OrderedDict([(1, 1), (2, 4), (3, 9), (4, 16)])
        self.result5 = collections.OrderedDict([(2, 4), (3, 9), (4, 16), (5, 25)])
        self.result6 = collections.OrderedDict([(2, 4), (4, 16), (5, 25), (3, 9)])
        self.result7 = collections.OrderedDict([(4, 16), (5, 25), (3, 9), (2, 4)])
        self.result8 = collections.OrderedDict([(5, 25), (3, 9), (2, 4), (10, 100)])
        self.result9 = collections.OrderedDict([(5, 25), (3, 9), (2, 4), (10, 100)])

    def test(self):
        self.assertEqual(user_page(self.test1), self.result1)
        self.assertEqual(user_page(self.test2), self.result2)
        self.assertEqual(user_page(self.test3), self.result3)
        self.assertEqual(user_page(self.test4), self.result4)
        self.assertEqual(user_page(self.test5), self.result5)
        self.assertEqual(user_page(self.test6), self.result6)
        self.assertEqual(user_page(self.test7), self.result7)
        self.assertEqual(user_page(self.test8), self.result8)
        self.assertEqual(user_page(self.test9), self.result9)


if __name__ == '__main__':
    unittest.main()
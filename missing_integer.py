# https://codility.com/programmers/lessons/4-counting_elements/missing_integer/

import unittest


class MissingIntegerTestCase(unittest.TestCase):
    def test1(self):
        A = [1, 3, 6, 4, 1, 2]
        self.assertEqual(solution(A), 5)

    def test2(self):
        A = [1, 3]
        self.assertEqual(solution(A), 2)


def solution(A):
    nums = {}
    for i in A:
        if i > 0:
            nums[i] = True
    i = 1
    while True:
        if not nums.get(i, False):
            return i
        i += 1


if __name__ == '__main__':
    unittest.main()

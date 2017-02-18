# https://codility.com/programmers/lessons/6-sorting/max_product_of_three/

import unittest


class MaxProductOfThreeTestCase(unittest.TestCase):
    def test1(self):
        A = [-3, 1, 2, -2, 5, 6]
        self.assertEqual(solution(A), 60)

    def test2(self):
        A = [-4, -3, 0, 1, 2]
        self.assertEqual(solution(A), 24)

    def test3(self):
        A = [-4, -3, -2, -1]
        self.assertEqual(solution(A), -6)

    def test4(self):
        A = [-4, -3, -2, 0]
        self.assertEqual(solution(A), 0)

    def test5(self):
        A = [-4, -3, 0, 1, 2, 7]
        self.assertEqual(solution(A), 84)


def solution(A):
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])


if __name__ == '__main__':
    unittest.main()

# https://codility.com/programmers/lessons/5-prefix_sums/count_div/

import math
import unittest


class CountDivTestCase(unittest.TestCase):
    def test1(self):
        A = 6
        B = 11
        K = 2
        self.assertEqual(solution(A, B, K), 3)

    def test2(self):
        A = 0
        B = 0
        K = 11
        self.assertEqual(solution(A, B, K), 1)

    def test3(self):
        A = 10
        B = 10
        K = 5
        self.assertEqual(solution(A, B, K), 1)

    def test4(self):
        A = 10
        B = 10
        K = 7
        self.assertEqual(solution(A, B, K), 0)

    def test5(self):
        A = 11
        B = 345
        K = 17
        self.assertEqual(solution(A, B, K), 20)


def solution(A, B, K):
    a = math.ceil(A / float(K)) * K
    b = math.floor(B / float(K)) * K
    if a > b:
        return 0
    return int(b / K) - int(a / K) + 1


if __name__ == '__main__':
    unittest.main()

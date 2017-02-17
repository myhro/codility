# https://codility.com/programmers/lessons/3-time_complexity/frog_jmp/

import math
import unittest


class FrogJumpTestCase(unittest.TestCase):
    def test1(self):
        X = 10
        Y = 85
        D = 30
        self.assertEqual(solution(X, Y, D), 3)

    def test2(self):
        X = 10
        Y = 10
        D = 30
        self.assertEqual(solution(X, Y, D), 0)


def solution(X, Y, D):
    r = (Y - X) / float(D)
    return int(math.ceil(r))


if __name__ == '__main__':
    unittest.main()

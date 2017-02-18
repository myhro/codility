# https://codility.com/programmers/lessons/6-sorting/distinct/

import unittest


class DistinctTestCase(unittest.TestCase):
    def test1(self):
        A = [2, 1, 1, 2, 3, 1]
        self.assertEqual(solution(A), 3)

    def test2(self):
        A = []
        self.assertEqual(solution(A), 0)


def solution(A):
    return len(set(A))


if __name__ == '__main__':
    unittest.main()

# https://codility.com/programmers/lessons/6-sorting/triangle/

import unittest


class TriangleTestCase(unittest.TestCase):
    def test1(self):
        A = [10, 2, 5, 1, 8, 20]
        self.assertEqual(solution(A), 1)

    def test2(self):
        A = [10, 50, 5, 1]
        self.assertEqual(solution(A), 0)

    def test3(self):
        A = []
        self.assertEqual(solution(A), 0)

    def test4(self):
        A = [1, 2, 3]
        self.assertEqual(solution(A), 0)

    def test5(self):
        A = [-1, 2, 3]
        self.assertEqual(solution(A), 0)


def solution(A):
    n = len(A)
    if n < 3:
        return 0
    A.sort()
    for i in range(n):
        if n - i < 3:
            return 0
        elif A[i] + A[i+1] > A[i+2]:
            return 1


if __name__ == '__main__':
    unittest.main()

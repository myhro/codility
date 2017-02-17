# https://codility.com/demo/take-sample-test/

import unittest


class DemoTestCase(unittest.TestCase):
    def test1(self):
        A = [-1, 3, -4, 5, 1, -6, 2, 1]
        self.assertNotEqual(solution(A), -1)

    def test2(self):
        A = []
        self.assertEqual(solution(A), -1)

    def test3(self):
        A = [1]
        self.assertNotEqual(solution(A), -1)

    def test4(self):
        A = [500, 1, -2, -1, 2]
        self.assertNotEqual(solution(A), -1)

    def test5(self):
        A = [-1, 0]
        self.assertNotEqual(solution(A), -1)

    def test6(self):
        A = [-1, -1, 1]
        self.assertNotEqual(solution(A), -1)

    def test7(self):
        A = [1, 2, 3]
        self.assertEqual(solution(A), -1)


def solution(A):
    n = len(A)
    if n == 0:
        return -1
    B = [0]
    for i in range(1, n):
        B.append(B[i-1] + A[i-1])
    total = B[n-1] + A[n-1]
    for i in range(n):
        total_ant = B[i] + A[i]
        if B[i] == (total - total_ant):
            return i
    return -1


if __name__ == '__main__':
    unittest.main()

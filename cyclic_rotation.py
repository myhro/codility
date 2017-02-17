# https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/

import unittest


class CyclicRotationTestCase(unittest.TestCase):
    def test1(self):
        A = [3, 8, 9, 7, 6]
        K = 3
        self.assertEqual(solution(A, K), [9, 7, 6, 3, 8])

    def test2(self):
        A = [1, 2, 3]
        K = 3
        self.assertEqual(solution(A, K), [1, 2, 3])

    def test3(self):
        A = []
        K = 1
        self.assertEqual(solution(A, K), [])

    def test4(self):
        A = [5, -1000]
        K = 1
        self.assertEqual(solution(A, K), [-1000, 5])


def solution(A, K):
    n = len(A)
    if n == 0:
        return A
    K = K % n
    if K == 0:
        return A
    return A[n-K:] + A[:n-K]


if __name__ == '__main__':
    unittest.main()

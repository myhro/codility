# https://codility.com/programmers/lessons/4-counting_elements/frog_river_one/

import unittest


class FrogRiverOneTestCase(unittest.TestCase):
    def test1(self):
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        X = 5
        self.assertEqual(solution(X, A), 6)

    def test2(self):
        A = [1, 3, 1, 4, 2, 3, 4]
        X = 5
        self.assertEqual(solution(X, A), -1)


def solution(X, A):
    n = len(A)
    count = 0
    leafs = {}
    for i in range(n):
        if not leafs.get(A[i], False):
            count += 1
            if count == X:
                return i
            leafs[A[i]] = True
    return -1


if __name__ == '__main__':
    unittest.main()

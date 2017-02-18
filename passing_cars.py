# https://codility.com/programmers/lessons/5-prefix_sums/passing_cars/

import unittest


class PassingCarsTestCase(unittest.TestCase):
    def test1(self):
        A = [0, 1, 0, 1, 1]
        self.assertEqual(solution(A), 5)

    def test2(self):
        A = [1, 0]
        self.assertEqual(solution(A), 0)

    def test3(self):
        A = [1, 0, 1]
        self.assertEqual(solution(A), 1)


def solution(A):
    total = 0
    zeroes = 0
    for i in A:
        if i == 0:
            zeroes += 1
        elif i == 1:
            total += zeroes
    if total > 1000000000:
        return -1
    return total


if __name__ == '__main__':
    unittest.main()

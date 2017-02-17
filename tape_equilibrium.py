# https://codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

import unittest


class TapeEquilibriumTestCase(unittest.TestCase):
    def test1(self):
        A = [3, 1, 2, 4, 3]
        self.assertEqual(solution(A), 1)

    def test2(self):
        A = [70, 1]
        self.assertEqual(solution(A), 69)

    def test3(self):
        A = [2, 1, 1]
        self.assertEqual(solution(A), 0)


def solution(A):
    n = len(A)
    B = [0]
    for i in range(1, n):
        B.append(A[i-1] + B[i-1])
    total = B[-1] + A[-1]
    minimo = None
    for i in range(1, n):
        total_posterior = total - B[i]
        diferenca = abs(total_posterior - B[i])
        if minimo and diferenca < minimo:
            minimo = diferenca
        elif minimo is None:
            minimo = diferenca
    return minimo


if __name__ == '__main__':
    unittest.main()

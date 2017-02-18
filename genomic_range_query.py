# https://codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

import unittest


class GenomicRangeQueryTestCase(unittest.TestCase):
    def test1(self):
        S = 'CAGCCTA'
        P = [2, 5, 0]
        Q = [4, 5, 6]
        self.assertEqual(solution(S, P, Q), [2, 4, 1])


def solution(S, P, Q):
    n = len(S)
    factors = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4,
    }
    pos = {
        'A': [0] * (n + 1),
        'C': [0] * (n + 1),
        'G': [0] * (n + 1),
        'T': [0] * (n + 1),
    }
    result = []
    for i in range(1, n + 1):
        c = S[i - 1]
        for j in 'ACGT':
            if c == j:
                pos[j][i] = pos[j][i - 1] + 1
            else:
                pos[j][i] = pos[j][i - 1]
    for i, j in zip(P, Q):
        for k in 'ACGT':
            if pos[k][i + 1] != pos[k][j + 1] or S[i] == k:
                result.append(factors[k])
                break
    return result


if __name__ == '__main__':
    unittest.main()

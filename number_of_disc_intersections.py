# https://codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/

import unittest


class NumberOfDiscIntersectionsTestCase(unittest.TestCase):
    def test1(self):
        A = [1, 5, 2, 1, 4, 0]
        self.assertEqual(solution(A), 11)


def pair_cmp(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    if x1 - y1 > x2 - y2:
        return 1
    if x1 - y1 < x2 - y2:
        return -1
    return 0


def solution(A):
    n = len(A)
    pairs = []
    for i in range(n):
        pairs.append((i - A[i], i + A[i]))
    pairs = sorted(pairs, pair_cmp)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = pairs[i]
            x2, y2 = pairs[j]
            if x2 <= y1 and y2 >= x1:
                result += 1
    return result


if __name__ == '__main__':
    unittest.main()

# https://codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

import unittest


class PermMissingElemTestCase(unittest.TestCase):
    def test1(self):
        A = [2, 3, 1, 5]
        self.assertEqual(solution(A), 4)


def solution(A):
    n = len(A) + 1
    complete_sum = (n * (n + 1)) / 2
    partial_sum = sum(A)
    return complete_sum - partial_sum


if __name__ == '__main__':
    unittest.main()

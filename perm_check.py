# https://codility.com/programmers/lessons/4-counting_elements/perm_check/

import unittest


class PermCheckTestCase(unittest.TestCase):
    def test1(self):
        A = [4, 1, 3, 2]
        self.assertEqual(solution(A), 1)

    def test2(self):
        A = [4, 1, 3]
        self.assertEqual(solution(A), 0)


def solution(A):
    n = len(A)
    nums = {}
    for i in A:
        nums[i] = True
    for i in range(1, n + 1):
        if not nums.get(i, False):
            return 0
    return 1


if __name__ == '__main__':
    unittest.main()

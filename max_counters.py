# https://codility.com/programmers/lessons/4-counting_elements/max_counters/

import unittest


class MaxCountersTestCase(unittest.TestCase):
    def test1(self):
        A = [3, 4, 4, 6, 1, 4, 4]
        N = 5
        self.assertEqual(solution(N, A), [3, 2, 2, 4, 2])

    def test2(self):
        A = [1]
        N = 1
        self.assertEqual(solution(N, A), [1])

    def test3(self):
        A = [1, 3, 1, 3, 1]
        N = 2
        self.assertEqual(solution(N, A), [3, 2])

    def test4(self):
        A = [1, 3, 1, 1, 1, 3, 1, 1, 3]
        N = 2
        self.assertEqual(solution(N, A), [6, 6])


def solution(N, A):
    size = len(A)
    initial = 0
    max_count = 0
    nums = {}
    for i in range(size):
        if A[i] == N + 1:
            nums = {}
            initial += max_count
            max_count = 0
        else:
            p = A[i] - 1
            nums[p] = nums.get(p, 0) + 1
            c = nums[p]
            if c > max_count:
                max_count = c
    return [initial + nums.get(i, 0) for i in range(N)]


if __name__ == '__main__':
    unittest.main()

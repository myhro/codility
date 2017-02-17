# https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

import unittest


class OddOccurrencesTestCase(unittest.TestCase):
    def test1(self):
        A = [9, 3, 9, 3, 9, 7, 9]
        self.assertEqual(solution(A), 7)


def solution(A):
    count = {}
    for i in A:
        count[i] = 1 + count.get(i, 0)
    return min([x for x in count if count[x] % 2 != 0])


if __name__ == '__main__':
    unittest.main()

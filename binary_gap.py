# https://codility.com/programmers/lessons/1-iterations/binary_gap/

import unittest


class BinaryGapTestCase(unittest.TestCase):
    def test1(self):
        N = 9
        self.assertEqual(solution(N), 2)

    def test2(self):
        N = 529
        self.assertEqual(solution(N), 4)

    def test3(self):
        N = 20
        self.assertEqual(solution(N), 1)

    def test4(self):
        N = 15
        self.assertEqual(solution(N), 0)

    def test5(self):
        N = 1041
        self.assertEqual(solution(N), 5)

    def test6(self):
        N = 2
        self.assertEqual(solution(N), 0)


def solution(N):
    n_bin = '{0:b}'.format(N)
    count = 0
    max_count = 0
    one = False
    for i in n_bin:
        if i == '1':
            one = True
            if count > max_count:
                max_count = count
            count = 0
        elif one and i == '0':
            count += 1
    return max_count


if __name__ == '__main__':
    unittest.main()

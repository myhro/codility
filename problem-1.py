import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        S = 'a0Ba'
        self.assertEqual(solution(S), 2)

    def test2(self):
        S = 'a0bb'
        self.assertEqual(solution(S), -1)

    def test3(self):
        S = 'ABCd'
        self.assertEqual(solution(S), 4)

    def test4(self):
        S = 'a'
        self.assertEqual(solution(S), -1)

    def test5(self):
        S = 'A'
        self.assertEqual(solution(S), 1)

    def test6(self):
        S = '1'
        self.assertEqual(solution(S), -1)

    def test7(self):
        S = 'A0A0A0'
        self.assertEqual(solution(S), 1)


def solution(S):
    upper = 0
    lower = 0
    biggest = -1
    for i in S:
        if i.isdigit():
            upper = 0
            lower = 0
        elif i.islower():
            lower += 1
        else:
            upper += 1
        if upper > 0 and (lower + upper) > biggest:
            biggest = lower + upper
    return biggest


if __name__ == '__main__':
    unittest.main()

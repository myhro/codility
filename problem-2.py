import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        A = 12
        B = 56
        self.assertEqual(solution(A, B), 1526)

    def test2(self):
        A = 56
        B = 12
        self.assertEqual(solution(A, B), 5162)

    def test3(self):
        A = 12345
        B = 678
        self.assertEqual(solution(A, B), 16273845)

    def test4(self):
        A = 123
        B = 67890
        self.assertEqual(solution(A, B), 16273890)

    def test5(self):
        A = 1234
        B = 0
        self.assertEqual(solution(A, B), 10234)

    def test6(self):
        A = 0
        B = 0
        self.assertEqual(solution(A, B), 0)

    def test7(self):
        A = 1
        B = 0
        self.assertEqual(solution(A, B), 10)

    def test8(self):
        A = 0
        B = 1
        self.assertEqual(solution(A, B), 1)


def solution(A, B):
    a = str(A)
    b = str(B)
    minor = min(len(a), len(b))
    result = ''
    for i in range(minor):
        result += a[i] + b[i]
    result += a[minor:] + b[minor:]
    result = int(result)
    if result > 10**8:
        return -1
    return result


if __name__ == '__main__':
    unittest.main()

import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        A = [60, 80, 40]
        B = [2, 3, 5]
        M = 5
        X = 2
        Y = 200
        self.assertEqual(solution(A, B, M, X, Y), 5)

    def test2(self):
        A = [40, 40, 100, 80, 20]
        B = [3, 3, 2, 2, 3]
        M = 3
        X = 5
        Y = 200
        self.assertEqual(solution(A, B, M, X, Y), 6)

    def test3(self):
        A = [10, 10, 10]
        B = [2, 2, 2]
        M = 3
        X = 2
        Y = 15
        self.assertEqual(solution(A, B, M, X, Y), 6)

    def test4(self):
        A = [10]
        B = [2]
        M = 3
        X = 2
        Y = 20
        self.assertEqual(solution(A, B, M, X, Y), 2)

    def test5(self):
        A = [10, 10]
        B = [2, 3]
        M = 3
        X = 2
        Y = 20
        self.assertEqual(solution(A, B, M, X, Y), 3)

    def test6(self):
        A = [10, 10]
        B = [2, 2]
        M = 3
        X = 2
        Y = 20
        self.assertEqual(solution(A, B, M, X, Y), 2)

    def test7(self):
        A = [1]
        B = [1]
        M = 1
        X = 1
        Y = 1
        self.assertEqual(solution(A, B, M, X, Y), 2)


def solution(A, B, M, X, Y):
    n = len(A)
    capacity = 0
    first_person = 0
    movements = 0
    weight = 0
    for i in range(n):
        if weight + A[i] <= Y and capacity + 1 <= X:
            weight += A[i]
            capacity += 1
        else:
            movements += len(set(B[first_person:i])) + 1
            capacity = 1
            first_person = i
            weight = A[i]
    return movements + len(set(B[first_person:])) + 1


if __name__ == '__main__':
    unittest.main()

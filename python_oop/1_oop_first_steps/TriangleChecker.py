class TriangleChecker:
    def __init__(self, a, b, c):
        self.lst = [a, b, c]

    def is_triangle(self):
        for num in self.lst:
            if not isinstance(num, int) or num <= 0:
                return 1
        if max(self.lst) >= sum(self.lst) - max(self.lst):
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

a, b, c = 3.0, 4.0, 5.0
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

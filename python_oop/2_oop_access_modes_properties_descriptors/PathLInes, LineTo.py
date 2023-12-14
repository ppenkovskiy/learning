class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *lines):
        self.lines = [LineTo(0,0),]
        if lines:
            for line in lines:
                self.lines.append(line)

    def get_path(self):
        if self.lines:
            return [(line.x, line.y) for line in self.lines]
        return []

    def get_length(self):
        res = 0
        for i in range(1, len(self.lines)):
            res += ((self.lines[i].x - self.lines[i - 1].x) ** 2 + (
                    self.lines[i].y - self.lines[i - 1].y) ** 2) ** 0.5
        return res

    def add_line(self, line):
        if type(line) == LineTo:
            self.lines.append(line)
        return self.lines


# line_1 = LineTo(1, 2)
# line_2 = LineTo(3, 4)
# path = PathLines(line_1, line_2)
# print(path.get_path())

# path = PathLines()
# print(path.get_path())

path = PathLines()

path.add_line(LineTo(20, -10))
print(path.get_path())
print(path.get_length())

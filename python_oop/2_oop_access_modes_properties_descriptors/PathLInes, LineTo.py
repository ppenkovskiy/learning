class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *lines):
        self.lines = []
        if lines:
            self.lines.append(LineTo())
            for line in lines:
                self.lines.append(line)
            # print(len(lines))

    def get_path(self):
        if self.lines:
            return [(line.x, line.y) for line in self.lines]
        return []

line_1 = LineTo(1, 2)
line_2 = LineTo(3, 4)
line_3 = LineTo(5, 6)

path_1 = PathLines(line_1, line_2, line_3)

print(path_1.get_path())

path_2 = PathLines()
print(path_2.get_path())

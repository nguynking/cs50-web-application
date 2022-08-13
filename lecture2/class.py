from ctypes import pointer


class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 4.3)
print(p.x)
print(p.y)
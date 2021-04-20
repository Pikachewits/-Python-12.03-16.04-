class Road:
    _length = 10
    _width = 5


    def __init__(self, length, width, weight, coverage):
        self._length = length
        self._width = width
        result = self._length * self._width * weight * coverage
        print(result)

Road = Road(20, 5000, 25, 5)
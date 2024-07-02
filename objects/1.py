class Shape:
    def __init__(self, name: str):
        self.name = name

    def __add__(self, other):
        raise NotImplementedError("addition is not implemented for this shape.")

    def __repr__(self):
        return self.name


class SquareShape(Shape):
    def __init__(self, side_length: float):
        super().__init__("square")
        self.side_length = side_length

    def __add__(self, other):
        if isinstance(other, SquareShape):
            return RectangleShape(self.side_length, other.side_length)
        else:
            raise TypeError("addition on square only work with squares")


class RectangleShape(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def __add__(self, other):
        if isinstance(other, RectangleShape):
            if self.width == other.width and self.height == other.height:
                return SquareShape(self.width * 2)
            else:
                return RectangleShape(self.width + other.width, max(self.height, other.height))
        else:
            raise TypeError("addition on rectangle only work with rectangles")


class TriangleShape(Shape):
    def __init__(self, base, height):
        super().__init__("triangle")
        self.base = base
        self.height = height

    def __add__(self, other):
        if isinstance(other, TriangleShape):
            s1 = 0.5 * self.base * self.height
            s2 = 0.5 * other.base * other.height

            width = max(self.base, other.base)
            new_height = (s1 + s2) / width

            if width == new_height:
                return SquareShape(width)
            else:
                return RectangleShape(width, new_height)


def main() -> int:
    rect1 = RectangleShape(8, 8)
    rect2 = RectangleShape(8, 8)
    tr1 = TriangleShape(3, 4)
    tr2 = TriangleShape(9, 1)
    print(rect1 + rect2)
    print(tr1 + tr2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

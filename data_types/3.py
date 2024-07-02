# для интересующихся (необязательно):
# Создайте тип данных, который может хранить только числа больше нуля


class PositiveList():
    def __init__(self, *numbers: int) -> None:
        self.numbers = [x for x in numbers if x > 0]

    def append(self, number: int) -> None:
        if number > 0:
            self.numbers.append(number)
        else:
            raise ValueError("number should be positive")

    def extend(self, iterable: list[int]) -> None:
        for number in iterable:
            if number > 0:
                self.numbers.append(number)
            else:
                raise ValueError("number should be positive")

    def __repr__(self) -> str:
        return f"PositiveList({self.numbers})"


def main():
    a = PositiveList(3, 4, 5, -3, 6, -5)
    b = [7, 4, 5, -3]
    a.extend(b)
    print(a)


if __name__ == "__main__":
    raise SystemExit(main())

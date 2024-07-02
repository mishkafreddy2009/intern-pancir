from typing import Iterator


def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main() -> int:
    for i in fibonacci():
        print(i)
    return 0


if __name__ == "__main__":
    main()

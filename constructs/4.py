# Написать программу, которая использует цикл while для подсчета факториала
# числа, введенного пользователем.


def compute_factorial(number: int) -> int:
    result = 1
    while number != 0:
        result *= number
        number -= 1
    return result


def main() -> int:
    x = int(input())
    print(compute_factorial(x))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

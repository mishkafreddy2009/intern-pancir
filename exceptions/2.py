# Написать функцию, которая делит два числа и обрабатывает исключение деления
# на ноль.


def divide_two_numbers(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("[err] can't be divided by 0")
        exit(1)
    else:
        return result


def main() -> int:
    print(divide_two_numbers(5, 4.5))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

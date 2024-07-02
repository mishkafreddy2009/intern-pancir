# Написать программу, которая использует while цикл для подсчета суммы чисел от
# 1 до 100.


def main() -> int:
    total = 0
    i = 1

    while i <= 100:
        total += i
        i += 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main())

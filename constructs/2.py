# Написать функцию, которая принимает список чисел и возвращает два списка
# отсортированных по четному и нечетному числу


def split_by_parity(numbers: list[int]) -> tuple[list[int], list[int]]:
    even = [number for number in numbers if number % 2 == 0]
    odd = [number for number in numbers if number % 2 != 0]
    return even, odd


def main() -> int:
    print(split_by_parity([3, 4, 5, 6 ,7, 8, 9, 0]))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

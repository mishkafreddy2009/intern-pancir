# Написать функцию, которая принимает список строк и возвращает словарь, где
# ключи — это длины строк, а значения — списки строк соответствующей длины.


def get_strings_by_len(strings: list[str]) -> dict[int, list[str]]:
    result = {len(i): [] for i in sorted(strings, key=len)}
    for i in strings:
        result[len(i)].append(i)
    return result


def main() -> int:
    print(get_strings_by_len(["sadf", "sdf", "gjf", "kdjfkdj"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

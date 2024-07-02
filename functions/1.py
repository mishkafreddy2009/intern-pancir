def avg(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def main() -> int:
    print(avg([2, 3, 4]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

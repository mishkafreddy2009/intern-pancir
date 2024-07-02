def foo(bar: float) -> list[float]:
    return [bar] * int(bar)


def main() -> int:
    print(foo(4.5))
    return 0


if __name__ == "__main__":
    main()

def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def main() -> int:
    prime_numbers = [number for number in range(1, 101) if is_prime(number)]
    print(prime_numbers)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

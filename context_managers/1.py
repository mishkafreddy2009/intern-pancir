def main() -> int:
    with open("1.txt", "r") as f:
        print(f.read())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

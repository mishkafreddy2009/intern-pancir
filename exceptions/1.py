def main() -> int:
    try:
        float(input())
    except ValueError:
        print("[err] input is not number")
    else:
        print("[ok] input is number")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

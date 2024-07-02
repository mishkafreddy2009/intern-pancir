# Написать программу, которая считывает содержимое файла и обрабатывает
# возможные исключения, такие как FileNotFoundError и PermissionError. (если
# есть трудности, прочтите тему контекстных менеджеров и можете возвращаться)


def read_file(file):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        print("[err] file not found")
        exit(1)
    except PermissionError:
        print("[err] not enough permissions")
        exit(1)
    else:
        print(f.read())
        f.close()


def main() -> int:
    read_file("3.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

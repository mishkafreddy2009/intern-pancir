# Создать класс Car с атрибутами made_by,  model и методом display_info,
# который выводит информацию о машине.

class Car:
    def __init__(self):
        self.made_by = "Toyota"
        self.model = "bB"

    def display_info(self) -> None:
        print(f"made by: {self.made_by}\nmodel: {self.model}")


def main() -> int:
    car = Car()
    car.display_info()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

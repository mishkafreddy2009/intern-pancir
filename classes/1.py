class Car:
    def __init__(self):
        self.made_by = "Toyota"
        self.model = "bB"

    def display_info(self) -> None:
        print(f"made by: {self.made_by}\nmodel: {self.model}")


car = Car()
car.display_info()

# Создайте классы Car, Driver
# Car, свойства: mileage (пробег), is_turned_on, driver
# Driver, наследуется от класса Person, опишите на своё усмотрение

# Далее, создайте контекстный менеджер, который будет принимать в себя
# аргументы car, driver, и при инициализации контекстного менеджера, будет
# включать двигатель машины, и каждую секунду пока двигатель активен, добавлять
# +1 к mileage, и когда мы выходим из контекста, двигатель глушился и
# реализуйте валидацию ситуации, когда пользователь пытается завести уже
# заведенную машину.

# Дополнительно: добавьте валидацию, что машиной может управлять только тот
# человек, чья это машина, и возвращать ошибку, если машиной начал управлять не
# собственник машины. Затем, поменяйте свойство driver, на drivers, и
# реализуйте логику чтобы собственников могло быть несколько.

# Супер-дополнительно: реализуйте метод, с помощью которого можно будет узнать
# каким т/c в данный момент управляет водитель, и какими машинами владеет


import time
import sys


class Person:
    def __init__(self, first_name: str, age: int):
        self.first_name = first_name
        self.age = age


class Driver(Person):
    def __init__(self,
                 first_name: str,
                 age: int,
                 driving_experience_in_years: int):
        super().__init__(first_name, age)
        self.driving_experience_in_years = driving_experience_in_years
        self.now_driving_car = None
        self.cars = set()

    def display_info(self):
        print(f"now driving: {self.now_driving_car}\ncars: {self.cars}")


class Car:
    def __init__(self, name: str):
        self.is_turned_on = False
        self.mileage = 0
        self.drivers = set()
        self.name = name

    def add_driver(self, driver: "Driver"):
        self.drivers.add(driver)
        driver.cars.add(self)

    def __repr__(self):
        return f"Car('{self.name}')"


class CarDriving:
    def __init__(self, car: "Car", driver: "Driver"):
        self.car = car
        self.driver = driver

    def __enter__(self):
        if self.car.is_turned_on:
            print("[err] car is already started.")
            sys.exit(1)

        if self.driver not in self.car.drivers:
            print(f"[err] {self.driver.first_name} not allowed to this car.")
            sys.exit(1)

        self.car.is_turned_on = True
        self.start_time = int(time.time())

        self.driver.now_driving_car = self.car

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.car.is_turned_on = False
        self.stop_time = int(time.time())

        self.car.mileage += self.stop_time - self.start_time


def main() -> int:
    driver_isa = Driver("Isa", 49, 23)
    car1 = Car("Toyota")

    driver_john = Driver("John", 21, 2)
    car2 = Car("BMW")

    car1.add_driver(driver_john)
    car1.add_driver(driver_isa)
    car2.add_driver(driver_isa)

    driver_john.display_info()
    with CarDriving(car1, driver_isa):
        driver_isa.display_info()
        time.sleep(3)

    return 0


if __name__ == "__main__":
    main()

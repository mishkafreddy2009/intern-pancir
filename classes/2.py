# Создать класс BankAccount с атрибутами balance и методами deposit, withdraw,
# и get_balance. Реализовать контроль за достаточностью средств при снятии.


class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("not enough money")

    def get_balance(self) -> int:
        return self.__balance


def main() -> int:
    bank_account = BankAccount(500)
    print(bank_account.get_balance())
    bank_account.deposit(5000)
    print(bank_account.get_balance())
    bank_account.withdraw(4000)
    print(bank_account.get_balance())
    bank_account.withdraw(4000)
    bank_account.withdraw(1500)
    print(bank_account.get_balance())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

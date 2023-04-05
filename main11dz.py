# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.

from datetime import datetime
from enum import Enum


class OperationEnum(Enum):
    PLUS = "пополнение счета"
    MINUS = "снятие денег"


class AccountHistory:
    def __init__(self, OperationEnum, amount, data_time):
        self.operation = OperationEnum
        self.amount = amount
        self.data_time = data_time


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.history = []

    def add_money(self, amount: int or float) -> int or float:  # пополнение счета
        self.balance += amount
        operation = AccountHistory(OperationEnum.PLUS, amount, datetime.now())
        self.history.append(operation)

    def withdraw_money(self, amount):  # снятие денег со счета
        if self.balance < amount:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            operation = AccountHistory(OperationEnum.MINUS, amount, datetime.now())
            self.history.append(operation)

    def print_history(self):
        for operation in self.history:
            print("{}: {} on {}".format(operation.operation, operation.amount, operation.data_time))


account = BankAccount()
account.add_money(1000)
account.withdraw_money(200)
account.withdraw_money(350)
account.add_money(10000)
account.withdraw_money(500)
account.print_history()

# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.
from datetime import datetime


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.history = []

    def add_money(self, amount):  # пополнение счета
        self.balance += amount
        operation = {
            "Тип операции": "пополнение счета",
            "Сумма": amount,
            "Дата и время": datetime.now()
        }
        self.history.append(operation)

    def withdraw_money(self, amount):    # снятие денег со счета
        if self.balance < amount:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            operation = {
                "Тип операции": "снятие денег",
                "Сумма": amount,
                "Дата и время": datetime.now()
            }
            self.history.append(operation)

    def print_history(self):
        for operation in self.history:
            print("{}: {} on {}".format(operation["Тип операции"], operation["Сумма"], operation["Дата и время"]))


account = BankAccount()
account.add_money(1000)
account.withdraw_money(200)
account.withdraw_money(350)
account.print_history()


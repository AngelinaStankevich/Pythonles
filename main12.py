# 1 задание
# Реализовать декоратор ЧЕРЕЗ КЛАСС!, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров


# import datetime
#
#
# class decorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         now_time = datetime.datetime.now()
#         positional_args = ", ".join(str(arg) for arg in args)
#         keyword_args = ", ".join(f"{k}={v}" for k, v in kwargs.items())
#
#         if args and kwargs:
#             print(
#                 f"Function {self.func.__name__} called at {now_time} with positional arguments: {positional_args} and keyword arguments: {keyword_args}")
#         elif args:
#             print(f"Function {self.func.__name__} called at {now_time} with positional arguments: {positional_args}")
#         elif kwargs:
#             print(f"Function {self.func.__name__} called at {now_time} with keyword arguments: {keyword_args}")
#         else:
#             print(f"Function {self.func.__name__} called at {now_time} without parameters")
#
#         return self.func(*args, **kwargs)
#
#
# @decorator
# def add(a=0, b=0) -> int:
#     return a + b
#
#
# add(5, b=7)

# 2 задание
# Добавить обработку исключений в следующие задания:
# 3* (из ДЗ номер 3)
# Написать мини-игру «Камень ножницы бумага с ботом», в которой пользователь должен выбрать либо камень,
# либо ножницы, либо бумагу. Бот делает случайный выбор (случайное число).
# Вывести результат если, например, игрок выбрал бумагу, а бот ножницы:
# Бот выбрал ножницы, вы проиграли!
# Подсказка: я не показывала, как в Pyhon получить случайное число, попробуйте найти это сами


# import random
#
# options = ["камень", "ножницы", "бумага"]
# bot_choice = random.choice(options)
# while True:
#     try:
#         user_choice = input("Выберите камень, ножницы или бумага:")
#         if user_choice not in options:
#             raise ValueError("Вы ввели неверную опцию!")
#         break
#     except ValueError as e:
#         print("Ошибка:", e)
#
# if user_choice == bot_choice:
#     print("Бот выбрал ту же опцию ")
#     print("Ничья!")
# elif user_choice == "камень":
#     if bot_choice == "ножницы":
#         print("Бот выбрал ножницы ")
#         print("Вы выиграли!")
#     else:
#         print("Бот выбрал бумагу ")
#         print("Вы проиграли:(")
# elif user_choice == "бумага":
#     if bot_choice == "ножницы":
#         print("Бот выбрал ножницы ")
#         print("Вы проиграли:(")
#     else:
#         print("Бот выбрал камень ")
#         print("Вы выиграли!")
# elif user_choice == "ножницы":
#     if bot_choice == "бумага":
#         print("Бот выбрал бумагу ")
#         print("Вы выиграли!")
#     else:
#         print("Бот выбрал камень ")
#         print("Вы проиграли:(")


# 3 задание
# 2 (из ДЗ номер 5)
# Написать функцию, которая принимает целое число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.


def even_number(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


def foo(n: int):
    try:
        if type(n) is not int:
            raise TypeError("Вы ввели неверные данные")
        else:
            for num in range(0, n):
                if num % 7 == 0 and num % 4 == 0:
                    continue
                elif even_number(num):
                    print(num * num)
                else:
                    print(num)
    except TypeError as e:
        print("Oшибка:", e)


foo(7)

# 1
# Написать функцию, которая проверяет является ли целое число четным.
# Функция возвращает True, если число четное, False если нет.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.
# Ввод и вывод результата производится вне функции проверки

# def even_number(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     return False
#
#
# number = input("Введите целое число:")
# if not number.isdigit():
#     print("Введенные данные не являются числом")
# else:
#     number = int(number)
#     print(even_number(number))


#2 задание
# Написать функцию, которая принимает число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Для проверки на четность использовать функцию из задания 1.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.

def even_number(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


def foo(n: int):
    if type(n) is not int:
        print("Введенные данные не являются числом")
    else:
        for num in range(0, n):
            if num % 7 == 0 and num % 4 == 0:
                continue
            elif even_number(num):
                print(num * num)
            else:
                print(num)

foo(7)






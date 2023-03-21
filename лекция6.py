
# def even_or_odd(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 == 1:
#         return False
#     else:
#         print("Введенные данные не являются числом")
#
#
# num = print("Введите число:")
# print(even_or_odd(num))





# # поменять местами ключ и значение
# dict_ = {'a': 4, 'b': 6, 'c': 8}
#
#
# def change_dict(dict_: dict) -> dict:
#     dict2 = {}
#     for key in dict_:
#         dict2[dict_[key]] = key
#     return dict2
#
# # одной строчкой
# new_dict = {dict_[key]: key for key in dict_}
# print(new_dict)
#
# print(change_dict(dict_))



#нахождение факториала числа

def fact(number: int) -> int:
    if number < 0:
        return
    if number == 1 or number == 0:
        return 1
    return number * fact(number - 1)
print(fact(4))



# map,filter




















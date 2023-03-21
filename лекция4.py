# friends_phone = {
#     'Egor': 123,
#     'Liza': 555,
#     'Vanya': 444,
#      }
# friends_names = list(friends_phone)
# print(friends_names)
# friends_names[0] = 'Arina'
# print(friends_names)
# friends_names[0], friends_names[1] = friends_names[1], friends_names[0]
# print(friends_names)
# friends_names.append('Iryna')
# print(friends_names)
# friends_names.insert(2, 'Galy')

# Дан список numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# Заменить каждый второй элемент на 0
# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# for i, num in enumerate(numbers):
#     if i % 2 == 1:
#         numbers[i] = 0
# print(numbers)
# Дан список numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# Посчитать сумму элементов списка, не использую встроенную функцию sum
# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# a = 0
# for num in numbers:
#     a += num
# print(a)
# print(sum(numbers))

# Дан словарь:
# friends_phone_numbers = {
#     'Egor': 123,
#     'Liza': 555,
#     'Vanya': 908,
#     'Yana': 150,
# }
# Для каждого элемента словаря вывести на экран: "У друга <имя> номер телефона <номер>"

# friends_phone_numbers = {
#     'Egor': 123,
#     'Liza': 555,
#     'Vanya': 908,
#     'Yana': 150,
# }
# for name in friends_phone_numbers:
#     print(f'у друга {name} номер телефона {friends_phone_numbers[name]}')

# Пользователь вводит число. Проверить, если пользователь ввел какие-либо символы
# кроме цифр, вывести сообщение 'Вы ввели невалидное число", иначе вывести на экран сумму цифр числа.
# Сделать двумя способами (с циклом и без)
# num_str = input("Введите число:")
# sum = 0
# if num_str.isdigit():
#     for symbol in num_str:
#         sum += int(symbol)
#     print(sum)
# else:
#     print("Вы ввели невалидное число")

# Пользователь вводит строку. Нужно посчитать сколько раз встречается каждый из символов строки
string = input("Введите строку :")
dict_ = dict()

for str in string:
    if str in dict_:
        dict_[str] += 1
    else:
        dict_[str] = 1
print(dict_)















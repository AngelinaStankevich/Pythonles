#1 задание

# name = input("Введите ваше имя:")
# age = int(input("Введите ваш возраст:"))
# while True:
#     if age > 18:
#         print(f'Приветсвую,{name}! У вас есть доступ к взрослому контенту.')
#     elif age < 18:
#         print(f'Приветсвую,{name}! У вас нет доступа к взрослому контенту.')
#     else:
#         print(f'Приветсвую,{name}! Поздравляю с совершеннолетием! У вас есть доступ к взрослому контенту.')

#2 задание
#Написать программу, используя функции input() и print().
# Программа запрашивает ввести произвольную строку.
# Затем необходимо создать 2 строковые переменные,
# первая из которых состоит только из чётных символов введённой строки,
# а вторая только из не чётных (сделать это двумя способами: через слайсы и через цикл).
# Вначале вывести введённую строку без начальных и завершающих пробелов
# в формате "Введена строка <введённая строка>”.
# Сделать 2 отступа (используя аргументы функции print)
# и затем обе переменные вывести одной функцией print, разделяя их между собой пятью
# пробелами и закончить вывод переводом строки и тремя восклицательными знаками.

# input_string = input("Введите произвольную строку:")
#
# print(f'Введенная строка:{input_string}')
# print("\n\n")
#
# even_chars = input_string[1::2]
# odd_chars = input_string[0::2]
#
# even_chars1 = ""
# odd_chars1 = ""
#
# n = len(input_string)
#
# for i in range(n):
#     if i % 2 == 0:
#         odd_chars1 += input_string[i]
#     else:
#         even_chars1 += input_string[i]
#
# print(f'Четные символы(с помощью слайсов):{even_chars}')
# print(f'Нечетные символы(с помощью слайсов):{odd_chars}')
# print(f'Четные символы(с помощью цикла):{even_chars1}')
# print(f'Нечетные символы(с помощью цикла):{odd_chars1}')
# print(f'Четные и нечетные символы : {even_chars1}     {odd_chars1}')
# print("!!!")


#3 задание
# Сделать программу, в которой нужно будет угадывать число

# import random
# number = random.randint(1, 10)
# print("Я загадал число от 1 до 10, попробуй угадать его")
#
# while True:
#     guess_choice = int(input("Введите число:"))
#     if guess_choice > number:
#         print("Ваше число больше загаданного")
#     elif guess_choice < number:
#         print("Ваше число меньше загаданного")
#     else:
#         print("Вы угадали число!")
#         break


#4 задание
#Ввести строку (считаем, что в начале и в конце строки нет пробелов,
# все слова в строке разделены одним пробелом). Для введенной строки
# изменить порядок символов в каждом слове в предложении,
# сохраняя при этом пробелы и первоначальный порядок слов.

# string = input("Введите предложение:")
#
# words = string.split(" ")
# new_words = []
#
# for word in words:
#     new_word = word[::-1]
#     new_words.append(new_word)
# new_string = " ".join(new_words)
# print(new_string)


# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5 по модулю.



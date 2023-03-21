# 1
# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину.

# text_ = """Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела"""
#
# # with open('article.txt', 'w') as file:
# #     file.write(text_)
#
# def read(file_name: str) -> list:
#     with open(file_name, "r") as file:
#         words = file.read().split()
#         max_word_len = len(words[0])
#         for word in words[1:]:
#             if max_word_len < len(word):
#                 max_word_len = len(word)
#         result = print(list(filter(lambda slovo: len(slovo) == max_word_len, words)))
#         return result
#
#
# print(read("article.txt"))

# 2
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

def read_last(lines_number: int, file_name: str) -> None:
    if lines_number < 0:
        print("Неверный параметр")
        return
    file = open(file_name)
    lines = file.readlines()
    for line in lines[-lines_number:]:
        print(line)
    file.close()


read_last(-2, "article.txt")
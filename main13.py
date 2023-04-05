# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.


# через итератор
import random


class RandomIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        return random.randint(self.start, self.end)


random_iterator = RandomIterator(1, 14)
for i in range(5):
    print(next(random_iterator))

print("\n")
# через генератор


def random_generator(start, end):
    while True:
        yield random.randint(start, end)


random_gener = random_generator(10, 50)
for i in range(10):
    print(next(random_gener))

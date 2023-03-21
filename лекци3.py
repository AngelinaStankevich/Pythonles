# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# numbers[0] = 10
# numbers[8] = 5
# print(numbers)
x = int(input("Введите x:"))
y = int(input("Введите y:"))
if x % 2 == 0 and y % 2 == 0:
    print("Оба числа кратны 0")
elif x % 2 != 0 and y % 2 != 0:
    print("оба числа не кратны 0")
if x > y:
    print(f'{x} больше {y}')
elif x < y:
    print(f'{x} меньше {y}')
elif x == y:
    print(f'{x} равно {y}')

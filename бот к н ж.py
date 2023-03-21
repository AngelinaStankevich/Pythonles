import random
options = ["камень", "ножницы","бумага"]
user_choice = input("Выберите камень, ножницы или бумага:")
bot_choice = random.choice

if user_choice in options:
    if user_choice == bot_choice:
        print("Бот выбрал ту же опцию ")
        print("Ничья!")
    elif user_choice == "камень":
        if bot_choice == "ножницы":
            print("Бот выбрал ножницы ")
            print("Вы выиграли!")
        else:
            print("Бот выбрал бумагу ")
            print("Вы проиграли:(")
    elif user_choice == "бумага":
        if bot_choice == "ножницы":
            print("Бот выбрал ножницы ")
            print("Вы проиграли:(")
        else:
            print("Бот выбрал камень ")
            print("Вы выиграли!")
    elif user_choice == "ножницы":
        if bot_choice == "бумага":
            print("Бот выбрал бумагу ")
            print("Вы выиграли!")
        else:
            print("Бот выбрал камень ")
            print("Вы проиграли:(")
else:
    print("Вы выбрали неверную опцию ")
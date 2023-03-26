#1 задание
class Auto:

    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


auto = Auto("audi", 3, "black", "a8", 1000)
# auto.move()
# auto.stop()
# print(auto.mark)

#2 задание
import time


class Truck(Auto):
    def __init__(self, max_load):
        self.max_load = max_load

    def move(self):
        print("attantion")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def move(self):
        super.move()
        print(f"max speed is {self.max_speed}")


truck = Truck(1000)
car = Car(280)
truck.move()
truck.load()
print(truck.max_load)
print(car.max_speed)



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
auto.move()
auto.stop()
print(auto.mark)

#2 задание

class Truck(Auto):
    def __init__(self, max_load):
        self.max_load = max_load

    def move(self):
        print("attantion")
        super().move()



class Car(Auto):
    pass

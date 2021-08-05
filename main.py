from typing import Collection


class Car(object):
    def __init__(self, name, color, speed, weight, model):
        self.name = name
        self.color = color
        self.speed = speed
        self.weight = weight
        self.model = model

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def changeGear(self,gear_type):
        print("Gear Changed")
        "Gear Related Functionality Is Here"

    def speed(self):
        print("Speed Has Been Boosted By 100 KM/h")
        "accelerator functionality is here"
# Define some students
john = Car("Nexon", "black", "120 KM/h", 520, "XZA+")
jane = Car("BMW", "white","120 KM/h", 580, "Q3")
audi = Car("Audi", "Black","120 KM/h", 220, "Q10" )
audi.color
# Now we can get to the grades easily
print(john.start())
print(jane.start())
print(audi.color)
print(audi.model)
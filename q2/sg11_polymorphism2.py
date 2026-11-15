# SG 11: Polymorphism
# Activity 2: Duck-Typing
—
# 1. a. What is duck typing, as explained in the video?
# According to the video, duck-typing is a way to achieve polymorphism, aside from inheritance. It's a concept that mainly checks the methods, and does not care about the classes much. It follows the saying, "If it walks like a duck and it quacks like a duck, then it must be a duck."
# b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
# The Car class needed to have the method speak() to print its attribute, even if it didn't inherit or is a part of the animal class.
—
# 2.
class Car():
    def move(self):
        print("\nThe car drives on the road.")

class Boat():
    def move(self):
        print("The boat sails on the water.")

class Drone():
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

print("Starting the trip with different vehicles:")
start_trip(car)
start_trip(boat)
start_trip(drone)
—
# 3. How does the code in 2.2 demonstrate polymorphism?
# Polmorphism was demonstrated in the code above through the use of duck-typing, not needing a parent-child inheritance to call the method. Instead, the code simply needed the existence of the specific method in the classes to make the code work and print their respective attributes.


# File Name : main.py
# Student Name: Collin Baines
# email:  bainesct@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   02/27/2025
# Course #/Section:   IS4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Collaborate with group to model a real life object in Python

# Brief Description of what this module does. This module calls upon the functions created in dog.py
# Citations: In Class Work 2/18/2025 (Avocado)

# Anything else that's relevant: N/A

from dogPackage.dog import *

if __name__ == "__main__":
    dogInfo = dog(name="Digby", breed="Rottweiler", age=9, color="Black" )
    print("Dog Name:", dogInfo.name)
    print("Dog Breed:", dogInfo.breed)
    print("Dog Age:", dogInfo.age)
    print("Dog Color:", dogInfo.color)
    print("------------------------")

    print(dogInfo)
    print("------------------------")

    print(repr(dogInfo))
    print("------------------------")

    print(dogInfo.get_name())
    dogInfo.set_name("Sparky")
    print(dogInfo.get_name())
    print("------------------------")

    print(dogInfo.get_breed())
    dogInfo.set_breed("Poodle")
    print(dogInfo.get_breed())
    print("------------------------")

    print(dogInfo.get_age())
    dogInfo.set_age(4)
    print(dogInfo.get_age())
    print("------------------------")

    print(dogInfo.get_color())
    dogInfo.set_color("White")
    print(dogInfo.get_color())
    print("------------------------")


    barkingNoise = dogInfo.bark()
    print(barkingNoise)
    print("------------------------")

    fetchBall = dogInfo.fetch_ball()
    print(fetchBall)
    print("------------------------")



    



    

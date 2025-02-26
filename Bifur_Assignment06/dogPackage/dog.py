# File Name : Bifur_Assignment06
# Student Name: Jack Driehaus
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   02/27/2025
# Course #/Section:   IS4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Collaborate with group to model a real life object in Python

# Brief Description of what this module does. This module creates the functions that model the dog to be called on in the main.py file
# Citations: https://stackoverflow.com/questions/1984162/purpose-of-repr-method , https://stackoverflow.com/questions/72350060/how-to-use-str-function-to-return-a-string-representation-of-a-class

# Anything else that's relevant:

class dog(object):
    """A cute fluffy dog who loves to play fetch"""

    def __init__(self, name, breed, age, color):
        """
        Initialize the Dog object
        @param name str: The name of the dog
        @param breed str: The breed of the dog
        @param age int: The age of the dog in years
        @param color str: The color of the dog
        """
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


    def __str__(self):
        """
        A string that describes the dog
        @return str: A descriptive string of the dog.
        """
        return f"{self.name} is a {self.age}-year-old {self.color} {self.breed} who loves to play fetch."


    def __repr__(self):
        """
        A string representation of the Dog's features
        @return str: A string that represents the Dog object with its attributes
        """
        return f"Dog(name='{self.name}', breed='{self.breed}', age={self.age}, color='{self.color}')"


    # Getter and setter for name:
    def get_name(self):
        """
        Get the name of the dog
        @return str: The name of the dog
        """
        return self.name

    def set_name(self, name):
        """
        Set the name of the dog
        @param name str: The new name of the dog
        """
        if isinstance(name, str) and name:
            self.name = name
        else:
            raise ValueError("Name must be a string")


    # Getter and setter for breed:
    def get_breed(self):
        """
        Get the breed of the dog
        @return str: The breed of the dog
        """
        return self.breed

    def set_breed(self, breed):
        """
        Set the breed of the dog
        @param breed str: The new breed of the dog
        """
        if isinstance(breed, str) and breed:
            self.breed = breed
        else:
            raise ValueError("Breed must be a string.")


    # Getter and setter for age:
    def get_age(self):
        """
        Get the age of the dog
        @return int: The age of the dog
        """
        return self.age

    def set_age(self, age):
        """
        Set the age of the dog
        @param age int: The new age of the dog
        """
        if isinstance(age, int) and age >= 0:
            self.age = age
        else:
            raise ValueError("Age must be a positive number")


    # Getter and setter for color:
    def get_color(self):
        """
        Get the color of the dog        
        @return str: The color of the dog.
        """
        return self.color

    def set_color(self, color):
        """
        Set the color of the dog.        
        @param color str: The new color of the dog.
        """
        if isinstance(color, str) and color:
            self.color = color
        else:
            raise ValueError("Color must be a string.")


    def bark(self):     
        """
        Makes the dog bark
        @return str: A barking sound
        """
        return "Woof! Woof!"


    def fetch_ball(self):
        """
        Make the dog fetch a ball.
        @return str:  A message indicating the dog fetched the ball
        """
        return f"{self.name} runs after the ball and brings it back!"
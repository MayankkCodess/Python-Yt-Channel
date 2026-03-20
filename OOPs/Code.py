# . The Evolution to OOP (from Images 1 & 2)
# Before jumping into OOP, your slides show how programming approaches have evolved using a simple addition problem:

# Imperative Approach: Just writing raw variables and adding them. It's simple, but if you want to add multiple different pairs of numbers, you have to keep creating new variables (a, b, c, d, x, y...).

# Functional Approach: Grouping the addition logic into a def addition(a, b): function. This is better because you can reuse the function, but data and functions are still floating around separately.

# Object-Oriented Programming (OOP): A paradigm where you group data (attributes/variables) and behavior (methods/functions) together into a single "Object".

# 2. Classes and Objects (from Images 3, 5, & 6)
# To understand OOP, you must understand the relationship between a Class and an Object.

# The Class (The Blueprint)
# A class is just a template or a blueprint. If you are building a house, the class is the architectural drawing on paper. It defines that the house will have doors and windows, but it isn't a physical house you can live in.

# The Object (The Reality)
# An object (also called an "instance") is the actual, physical house built using that blueprint. You can build 100 different houses (objects) from the same blueprint (class), and they can all have different paint colors!


# Python
# 1. Defining the Blueprint (Class)
class Dog:
    species = "Canine" # Attribute (Data)
    
    def bark(self):    # Method (Behavior)
        print("Woof! Woof!")

# 2. Creating the Actual Object
my_dog = Dog() 

# 3. Accessing its powers using the "dot" syntax
print(my_dog.species)  # Output: Canine
my_dog.bark()          # Output: Woof! Woof!


# 3. The Constructor & self (from Image 7)
# In the real world, when you manufacture a bag (your slide's example), you need to give it specific materials, zips, and pockets right at the moment it's created on the assembly line.

# In Python, we do this using a Constructor. This is a special method called __init__ that runs automatically the exact moment you create an object.

# The self keyword is absolutely crucial here. Because you can make 100 different bags from the same class, self acts as a name tag pointing to the specific bag currently being created or modified.

# Python


class Bag:
    # The Constructor
    def __init__(self, material, zips):
        self.material = material  # Assigns the material to THIS specific bag
        self.zips = zips          # Assigns the zip count to THIS specific bag

# Creating two different objects from the same Class
bag1 = Bag("Leather", 3)
bag2 = Bag("Nylon", 5)

print(bag1.material) # Output: Leather
print(bag2.material) # Output: Nylon



# 4. Types of Attributes (from Image 8)
# Attributes are just variables that belong to a class. There are two main types:

# Class Attributes: Defined directly inside the class. These are shared by every single object created from that class. (e.g., Every car has 4 wheels).

# Instance Attributes: Defined inside the __init__ constructor using self.. These are unique to each specific object. (e.g., Your car might be red, mine might be blue).

# Python



class Car:
    wheels = 4  # Class Attribute (Shared by ALL cars)

    def __init__(self, color):
        self.color = color  # Instance Attribute (Unique to THIS car)

my_car = Car("Red")
print(f"My car has {my_car.wheels} wheels and is {my_car.color}.")



# 5. Types of Methods (from Images 8 & 9)
# Methods are functions inside a class. There are three types you need to know:

# Instance Methods: The standard method. It uses self as its first parameter so it can access and modify specific instance attributes.

# Class Methods: Uses the @classmethod decorator. It takes cls (the class itself) as the first parameter instead of self. It can only modify Class Attributes, not Instance Attributes.

# Static Methods: Uses the @staticmethod decorator. It takes neither self nor cls. It's basically just a regular, standalone function that you threw inside the class for organizational purposes.

# Python


class MathStudent:
    school_name = "Python High" # Class Attribute

    # 1. Instance Method
    def introduce(self, name):
        print(f"Hi, I'm {name}.")

    # 2. Class Method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name # Changes it for EVERY student
        print(f"School is now {cls.school_name}")

    # 3. Static Method
    @staticmethod
    def add_numbers(a, b):
        # Doesn't care about 'self' or 'cls', just does simple math
        return a + b 
    


# 6. Inheritance (from Image 10)
# Inheritance allows a new class (the Child class) to adopt all the attributes and methods of an existing class (the Parent class).

# Why is this amazing? * Code Reusability: If you have an Animal class with a eat() method, your new Dog class and Cat class can just inherit it instead of you having to write the eat() method three different times!

# Organization: It creates a clean, logical structure.

# Python



# The PARENT Class
class Animal:
    def __init__(self):
        self.eyes = 2
        
    def eat(self):
        print("I am eating food.")

# The CHILD Class (Inherits from Animal by passing it in parentheses)
class Dog(Animal):
    def bark(self):
        print("Woof!")

# Let's test it!
my_puppy = Dog()

# It can do its own methods...
my_puppy.bark() 

# AND it can do the inherited methods from the Parent!
my_puppy.eat()  
print("I have", my_puppy.eyes, "eyes.")



# 1. Advanced Inheritance & The super() Function (from Images 11, 12, 13, & 14)
# We know inheritance allows a Child class to get the attributes and methods of a Parent class. But what happens if the Child class needs its own custom constructor (__init__), while still keeping the Parent's attributes?

# This is where the super() function comes in. It acts as a direct hotline to the Parent class, allowing you to trigger the Parent's constructor from inside the Child.

# Python

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        # 1. Call the Parent's constructor to handle 'name'
        super().__init__(name) 
        # 2. Handle the new 'age' attribute specifically for the Child
        self.age = age         

    def display(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

c = Child("Riya", 20)
c.display()

# Your slides also highlight that inheritance isn't just a simple 1-to-1 relationship. There are different structures:

# Single Inheritance: One Parent -> One Child.

# Multiple Inheritance: Two Parents -> One Child. (e.g., class Child(Father, Mother):). Note: If both parents have a method with the same name, Python uses MRO (Method Resolution Order), prioritizing the class listed first (Father).

# Multilevel Inheritance: Grandparent -> Parent -> Child. Attributes pass all the way down the chain.




# 2. Polymorphism & Duck Typing (from Images 15 & 16)
# Polymorphism translates to "many forms". It means that different classes can have methods with the exact same name, but behave entirely differently.

# Method Overriding: This is the most common form in Python. It happens when a Child class has a method with the exact same name as a Parent class, thereby "overriding" or replacing the Parent's version.

# Python
class Animal:
    def sound(self):
        print("Generic animal noise")

class Dog(Animal):
    # This overrides the Parent's sound() method
    def sound(self): 
        print("Woof! Woof!")

my_dog = Dog()
my_dog.sound() # Output: Woof! Woof!



# Duck Typing: This is a famous Python philosophy: "If it walks like a duck and quacks like a duck, it must be a duck." Python doesn't actually care what specific type of class an object is; it only cares if the object has the specific method you are trying to use.

# Python
class Duck:
    def talk(self): print("Quack!")

class Human:
    def talk(self): print("Hello!")

# This function doesn't care IF the object is a Duck or a Human.
# It only cares that the object has a .talk() method!
def make_it_speak(entity):
    entity.talk()

make_it_speak(Duck())  # Works!
make_it_speak(Human()) # Also works!


# 3. Encapsulation & Access Modifiers (from Images 17 & 18)
# Encapsulation is the practice of bundling data (attributes) and methods together within a class, and strictly controlling what can be accessed from the outside. Think of it like a protective capsule around your code.

# Python uses naming conventions to establish "Access Modifiers":

# Public: self.name (Accessible from anywhere).

# Protected: self._age (Has a single underscore. It's a gentleman's agreement among programmers meaning "Please don't touch this outside the class," but Python won't actually stop you).

# Private: self.__salary (Has a double underscore. Python actively hides this variable so it cannot be easily accessed or modified from outside the class).

# Python
class Employee:
    def __init__(self):
        self.name = "John"      # Public
        self._department = "IT" # Protected
        self.__salary = 50000   # Private

emp = Employee()
print(emp.name)        # Works fine
print(emp._department) # Works, but bad practice to do this outside the class!
# print(emp.__salary)  # ERROR! Python hides this to protect it.




# 4. Abstraction (from Image 19)
# Abstraction is about hiding the complex background implementation and showing only the essential features.

# In Python, we achieve this using Abstract Base Classes (ABC). An abstract class is like a strict contract: it defines methods that must exist, but leaves them empty. Any child class that inherits from it is forced to actually build out those methods.

# Note: You cannot create an object directly from an Abstract class!

# Python
from abc import ABC, abstractmethod

# The strict contract (Abstract Class)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass # Empty! We just declare it exists.

# The Child MUST implement the method, or Python will throw an error
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

my_cat = Cat()
my_cat.make_sound()




# 5. Dunder (Magic) Methods (from Image 20)
# Dunder stands for "Double Underscore". These are special built-in methods (like __init__) that trigger automatically in the background when you perform specific actions.

# They allow your custom classes to behave like native Python data types.

# __init__: Automatically called when an object is created.

# __str__: Automatically called when you print() your object. Without it, printing an object just gives you an ugly memory address.

# __add__: Automatically called when you use the + operator between two objects.

# Python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # Customizing what happens when someone prints this object!
    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

my_book = Book("Harry Potter", 400)

# Behind the scenes, this automatically triggers the __str__ dunder method!
print(my_book) # Output: 'Harry Potter' (400 pages)




# 1. Decorators (from Image 21)
# A Decorator is a function that takes another function, extends or modifies its behavior, and returns it—all without permanently changing the original function's source code.

# As your slide mentions, think of it like putting icing on a cake. The cake (your original function) remains the same, but you've added an outer layer (the decorator) that makes it look or taste different.

# We use the @ symbol to apply a decorator.

# Python
# 1. Create the decorator function
def my_decorator(func):
    def wrapper():
        print("-> Something is happening BEFORE the function runs.")
        func() # This executes the original function
        print("-> Something is happening AFTER the function runs.")
    return wrapper # Returns the modified behavior

# 2. Apply it using the @ symbol
@my_decorator
def say_hello():
    print("Hello! I am the original function.")

# 3. Call your function
say_hello()




# 2. *args and **kwargs (from Image 22)
# Sometimes you want to build a function, but you have no idea how many arguments the user is going to pass into it.

# *args (Arguments): Allows you to pass a flexible number of positional arguments. Python packs them all into a Tuple.

# **kwargs (Keyword Arguments): Allows you to pass a flexible number of named/keyword arguments. Python packs them into a Dictionary.

# Python
def flexible_function(*args, **kwargs):
    print("Args (Tuple of positional arguments):", args)
    print("Kwargs (Dictionary of keyword arguments):", kwargs)

# We can pass as many items as we want!
flexible_function(1, 2, 3, name="Arin", age=21, city="Delhi")




# 3. Comprehensions (from Image 23)
# Comprehensions are a beautiful Python feature that allows you to create Lists, Dictionaries, or Sets in a single, highly readable line of code, rather than writing out a bulky multi-line for loop.

# Python
# --- LIST COMPREHENSION ---
# Traditional way:
# evens = []
# for x in range(5):
#     if x % 2 == 0:
#         evens.append(x)

# Comprehension way (Format: [expression for item in iterable if condition]):
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print("List:", labels) # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']

# --- DICTIONARY COMPREHENSION ---
# Format: {key: value for item in iterable if condition}
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print("Dictionary:", even_squares) # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}




# 4. Lambda Functions (from Images 23 & 24)
# A Lambda function is a small, anonymous (unnamed) function. You use the lambda keyword instead of def.

# The Rule: They can take any number of arguments, but they can only have one single expression (no multi-line logic allowed).

# Use Case: Perfect for short, throwaway functions that you only need to use once.

# Python
# A standard function
def square_normal(x):
    return x ** 2

# The exact same thing as a Lambda function
square_lambda = lambda x: x ** 2

print("Lambda output:", square_lambda(4)) # Output: 16

# Lambda with an if-else statement
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Is 7 even?", check_even(7)) # Output: Odd




# 5. Map, Filter, and Zip (from Images 24 & 25)
# These are powerful built-in functions used to process collections of data (like lists). They pair exceptionally well with Lambda functions!

# map(): Transforms data. It applies a specific function to every single item in a list and gives you back the modified list.

# filter(): Removes data. It runs a test (a function that returns True/False) on every item. It only keeps the items that return True.

# (Note on zip(): Your slide header mentioned it, though the text didn't. zip() takes two or more lists and pairs their elements together side-by-side!)

# Python
numbers = [1, 2, 3, 4, 5]

# --- MAP Example: Multiply everything by 2 ---
# map(function, iterable)
doubled = map(lambda x: x * 2, numbers)
print("Mapped:", list(doubled)) # Output: [2, 4, 6, 8, 10]

# --- FILTER Example: Keep only even numbers ---
# filter(function, iterable)
evens = filter(lambda x: x % 2 == 0, numbers)
print("Filtered:", list(evens)) # Output: [2, 4]

# --- ZIP Example ---
names = ["Alice", "Bob"]
ages = [25, 30]
paired = zip(names, ages)
print("Zipped:", list(paired)) # Output: [('Alice', 25), ('Bob', 30)]





# 6. Modules and Packages (from Images 25 & 26)
# As your Python programs get larger, you can't keep everything in one file.

# Module: A single Python file (e.g., math_tools.py) containing functions and variables. You can import this file into another file to reuse the code.

# Package: A normal computer folder that contains multiple modules (multiple .py files) organized together.

# Types of Modules/Packages:

# Built-in: Come pre-installed with Python. Just import them! (e.g., math, random, datetime).

# Third-Party: Created by other developers. You must download them from the internet using an installer like pip before you can import them. (e.g., numpy for math, pandas for data science).

# Python
# Importing a built-in module
import math
import random

print("Square root of 16 is:", math.sqrt(16))
print("Random number between 1 and 10:", random.randint(1, 10))








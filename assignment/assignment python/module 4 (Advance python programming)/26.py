#26. Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? 

# >>> Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit attributes and methods from another
# class. The class that is inherited from is called the parent (or base) class, and the class that inherits is called the child 
# (or derived) class. Inheritance promotes code reuse and can lead to a hierarchical organization of classes.


#Example:

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(dog.speak()) 
# print(cat.speak())  

# >>> The __init__ method in Python is a special method called a constructor. It is automatically invoked when a new instance of a class 
# is created. The primary purpose of a constructor is to initialize the attributes of the class.


#>>> Constructor (__init__ Method): When an instance of Person is created, the __init__ method initializes the name and age attributes.
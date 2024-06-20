#22. How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 

# A class is defined using the class keyword followed by the class name. It typically includes attributes (data fields) and 
# methods (functions associated with the class). 

# >> self is a convention in Python that represents the instance of the class. It is the first parameter of instance methods.
# >> When you call an instance method, Python automatically passes the instance (self) as the first argument.

class MyClass:

    def __init__(self, param1, param2):
        # Instance attributes
        self.instance_attr1 = param1
        self.instance_attr2 = param2
    
    
    def instance_method(self):
        return f"Instance method called with {self.instance_attr1} and {self.instance_attr2}"
    
    def class_method(cls):
        return "Class method called with class attribute"

    def static_method():
        return "Static method called"

"""In python self.key is the instance of attribute and it is the way to istore the specific of the information"""
class Person:
    """A method is the function that is defined inside the class and it is used to perform some specific action"""
    def __init__(self, key):
        self.key = key

m = Person("John")
print(m.key)

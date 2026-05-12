def name (name):
    print(f"{name}! Welcome back.")
    
    
name("Kaushik")

"""Inside the function we cant use the keyword self as the self is used in the classes only """
def age1 (age):
    print(f"{age}! is your age")
    
    
age1(12)


class Person:
    def name(self,name):
        print(f"{name} Welcome back.")
 
 
"""This is an instance of the class first"""        
p1 = Person()
"""Python automatically sends me as p1 as the self argument"""
p1.name("Raj")


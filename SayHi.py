# Write a class called Dog that has two properties: name and age. Write a constructor that takes three arguments self, name and age and set these to the object properties.
# Now write a function sayHI(dog) where dog is the dog class object that returns a Hi, my name is <dog’s name> and I am <age> years old!

# sayHi(d1) # Hi, my name is Dot and I am 4 years old!
# sayHi(d2) # Hi, my name is Elf and I am 3 years old!

class SayHi():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sayHI(self):
        return f"Hi, my name is {self.name} and I an {self.age} years old"

obj1 = SayHi("Dot",4)
obj2 = SayHi("Mike",5)
obj3 = SayHi("Zabuza",50)
print(obj1.sayHI())
print(obj3.sayHI())
print(obj2.sayHI())
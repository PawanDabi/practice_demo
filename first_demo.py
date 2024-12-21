class Person:
    def __init__(self, first_name, last_name):
        self.__name=first_name
        self.lastname=last_name
    
    def display_firstname(self):
        print(f"your first name is: {self.__name}")
        print(f"your last name is: {self.lastname}")

p=Person("pawan ", "dabi")
p.display_firstname()    

print("this is the last one")   
print("this is another method")
print("this is for main demo")

class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)

ozzy.doginfo()
skippy.doginfo()
filou.doginfo()
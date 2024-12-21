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
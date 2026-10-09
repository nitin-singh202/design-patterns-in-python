class Student:
    # Methods
    def __init__(self, name: str, age: int, gender: str) -> None: # --> this is a constructor or initializer
        # Attributes- attributes are nothing but just variables assigned to the classes
        self.name = name
        self.age = age
        self.gender = gender
    # method iss basically a function inside the class
    def display(self) -> None:
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")
# name age gender are parameter 
    def get_age(self) -> int: #-> int: is not compulsory to add but if u add then it would  be better for other developers to understand the code better.
        return self.age

    def get_set(self, name: str , age: int , gender: str):
        

s1 = Student("Anirudh", 22, "Male")
print(s1.get_age())

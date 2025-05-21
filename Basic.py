class Animal:
    name = "DOG"
    def __init__(self, name, age, birth):
        self.name = name
        self.age = age 
        self.birth = birth 
     
        

    def speak(self):
        return f"{self.name} {self.age} {self.birth} makes a sound"
    

cat = Animal("Cat","23","2022")
dog = Animal("Dog","24","2000")
camel = Animal("Camel", "567", "1576")
print(cat.speak()) 
print(dog.speak()) 
print(camel.speak()) 


class Calculator:
    def __init__(self,num1, num2):
        self.history = {
            "add" : 0,
            "sub" : 0,
            "prod" : 0
        }
        self.num1= num1
        self.num2 = num2
       

        
    def add(self):
        self.history["add"] += 1
       
        return self.num1 + self.num2
    
    def product(self):
        self.history["sub"] += 1
        return self.num1 * self.num2
    
    def substract(self):
        self.history["prod"] += 1
        return self.num1 - self.num2
  

calc = Calculator(2,3)
print(calc.add())
print(calc.product())
print(calc.substract())
print(calc.add())
print(calc.product())
print(calc.substract())
print(calc.add())
print(calc.product())
print(calc.substract())
print(calc.history)


    

"""
class Laptop:
    def __init__(self,brand,price,color,memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        print(f"The name of brand {self.brand} . Price : {self.price}. color : {self.color}")


class Mobile:
    def __init__(self,brand,price,color,camera):
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera

    def SMS(self,number,text):
        print(f"Number : {number}\n SMS : {text}")


dell = Laptop("DELL","54000","RED","12 GB")
dell.run()


iphone = Mobile("Nokia","23000","White", "50px")
iphone.SMS("01717256912","I am here")
        
        



class Vehicle:
    def __init__(self,name,brand,price,color):
        self.name = name
        self.brand = brand
        self.price = price 
        self.color = color 

    def __repr__(self):
        return f"Name = {self.name}\n Brand = {self.brand}\n Price = {self.price}\n Color = {self.color}"
    

class Bus(Vehicle):
    def __init__(self, name, brand, price, color,company):
        self.company = company
        super().__init__(name, brand, price, color)
        
    def __repr__(self):
        return super().__repr__()
    

class AC_BUS(Bus):
    def __init__(self, name, brand, price, color, company,ac):
        self.ac = ac
        super().__init__(name, brand, price, color, company)

    def __repr__(self):
        print(f"AC= {self.ac}")
        return super().__repr__()
    

sb = AC_BUS("SB SUPER DELUXE", "HINO","5000000","BLUE","RN2","AC")
print(sb)



class Family:
    def __init__(self,father ,mother,address):
        self.father = father
        self.mother = mother
        self.address = address

class School:
    def __init__(self,name ,cls,roll):
        self.name = name
        self.cls = cls
        self.roll = roll

class Student(Family,School):
    def __init__(self, father, mother, address,name,cls,roll):

        School.__init__(self,name,cls,roll)
        super().__init__(father, mother, address)


    def Details(self):
        print(f"Address : {self.address} Father : {self.father} Class = {self.cls}  ROll : {self.roll}")

        


a = Student("Jobbar","Sokina","Dhaka","Modhu","9","22")
a.Details()   






class Bank:
    def __init__(self,holder_name,initital_deposit):
        self.holder_name = holder_name
        self.__balance = initital_deposit

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if self.__balance > amount:
            self.__balance -= amount
            return self.__balance
        
        else:
            return f"You Do not have sufficient balance !!"
    

tanim = Bank("Tanism Sumon", 5000)
tanim.deposit(1500)
tanim.deposit(2500)
print(tanim.get_balance())

print(tanim.withdraw(5000))
        



from abc import ABC, abstractclassmethod
class Animal:
    def __init__(self,name):

        self.name = name
        self.category = "Monkey"
    @abstractclassmethod
    def eat(self):
        print(f"I Am Eating Banana !!")
    @abstractclassmethod
    def dance(self):
        print(f"I am Dancing !!")


class Monkey(Animal):
    def __init__(self, name,food):
        self.food = food
        super().__init__(name)

    def eat(self):
        print(f"I Am Eating Banana !!")


    def dance(self):
        print(f"I am Dancing !!")


m = Monkey("Monkey","Banana")
m.eat()
m.dance()





class Animal:
    def __init__(self,name):
        self.name = name

    def Voice(self):
        print(f"Yau Yau Yau")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def Voice(self):
        print(f"MAW MAW MAW")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def Voice(self):
        print(f"GAW GAW GAW")

d = Dog("Dog")
d.Voice()
c = Cat("Cat")
c.Voice()
a = Animal("Elephant")
a.Voice()

animals = [d,c,a]

for animal in animals:
    animal.Voice()




from math import pi
class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        pass

class Circle(Shape):

    def __init__(self, name,radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius * self.radius
        

class Rectangle(Shape):

    def __init__(self, name,length,width):
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length*self.width
    

c = Circle("Circle", 7)
print(c.area())

r = Rectangle("Rectangle", 5,4)
print(r.area())


"""      
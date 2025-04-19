"""
class student:
    cls = "Nine"
    subjects = 4 
    roll = 23
    district = "Dhaka"
    Basic = "good"



badol = student()
print(badol.cls)
print(badol.roll)
print(badol.subjects)
print(badol.district)





class mobile:
    color ="red"
    brand = "Svmsung"
    price = 15000

    def sms(self, number, message):
        text = f"Sending sms to : {number} and sms is :{message}"
        return text
    
a = mobile()
print(a.brand)
print(a.color)
print(a.price)
result = a.sms("01717262544", "I want to see You !!")
print(result)



class calculator:
    brand = "Casio MS-99"
    def add(self,x,y):
        print(f"REsult is {x+y}")

    def sub(self,x,y):
        print(f"REsult is {x-y}")

    def mul(self,x,y):
        print(f"REsult is {x*y}")

    def div(self,x,y):
        print(f"REsult is {x/y}")


casio = calculator()
print(casio.brand)
print(casio.add(20,10))
print(casio.sub(20,10))
print(casio.mul(20,10))
print(casio.div(20,10))




class phone:
    def __init__(self,model,price,color):
        self.model = model
        self.price = price
        self.color = color

    def sms(self,number,message):
        print(f"Sending sms to :{number} sms is :{message}")


a = phone("svmsung", 16000,"Black")
print(a.model)
print(a.price)
print(a.color)
print( a.sms("01717563566","I want to talk to you!!"))



class shop:
    
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []
    def add_to_cart(self,item):
        self.cart.append(item)

badol = shop("badol")
badol.add_to_cart("Shirt")
badol.add_to_cart("Pant")
badol.add_to_cart("court")
badol.add_to_cart("Panjabi")

print(badol.cart)

paglu = shop("Paglu")
paglu.add_to_cart("Table")
paglu.add_to_cart("Chair")

print(paglu.cart)



class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 5000

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance = self.balance+amount
        print(f"Your current balance is {self.get_balance()}")
    
    def withdraw(self, amount):
        if amount < 100:
            print(f"You Can not Withdraw lessthan {self.min_withdraw}")

        elif amount > self.max_withdraw:
            print(f"You can not withdraw more than {self.max_withdraw}")

        else:
            self.balance -= amount
            print(f"Your Current balance is {self.get_balance()}")




kajol = Bank(5000)
tareq = Bank(6000)

kajol.deposit(500)
kajol.deposit(500)
kajol.deposit(500)
kajol.deposit(500)

tareq.withdraw(250)
tareq.withdraw(250)
tareq.withdraw(250)
tareq.withdraw(250)



class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self,product,price,quantity):
        puchase = {"product":product, "price":price, "quantity":quantity}
        self.cart.append(puchase)


    def bill(self,amount):
        total = 0

        for i in self.cart:
            total += i["price"] * i["quantity"]
        
        print(f"You have paid {amount} Taka.")
        print(f"Total Bill is {total} Taka.")

        if total > amount:
            print(f"You have to pay {total-amount} Taka More !!")

        else:
            extra = amount - total
            print(f"You will get Back {extra} Taka!!")


a = shopping("Abid Mia")

a.add_to_cart("Alu",30,4)
a.add_to_cart("Tomato",40,4)
a.add_to_cart("Rice",50,5)
a.add_to_cart("Egg",60,6)

taka = int(input("Please Enter Your Amount = "))
a.bill(taka)


class Student:
    def __init__(self,name,cls,id):
        self.name = name
        self.cls = cls
        self.id = id

    def __repr__(self) -> str:
        return f"Name : {self.name} Class :{self.cls}  id = {self.id}"


class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject

    def __repr__(self) -> str:
        return f'Teacher-Name : {self.name} Subject :{self.subject}'
    
class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_to_teacher(self,name,subject):
        id = len(self.teachers)+1
        teacher = Teacher(name,subject)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee < 6500:
            return f"Not Enough Money!!"
        
        else:
            id = len(self.students)+1
            student = Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id {id}'
        
    def __repr__(self):
        print("............OUR TEACHER ............")
        for teacher in self.teachers:
            print(teacher)

        print("............OUR STUDENT...............")
        for student in self.students:
            print(student)
        return f"All DONE"
        


x = School('phitron')
x.enroll("Mashud",7000)
x.enroll("Rana",7000)
x.enroll("Tareque",7000)
x.enroll("Jamal",7000)


x.add_to_teacher("Rana","BAngla")
x.add_to_teacher("Jalal","English")
x.add_to_teacher("Rana","BAngla")

print(x)

"""

"""
def double_it(n):
    result = n*2
    print(result)

double_it(5)


"""
"""
def sum(a,b,c,d):
    total = a+b+c+d
    return total


result = sum(10,20,30,40)
print(result)
"""

"""
def all_sum(*numbers):
    sum = 0

    for num in numbers:
        sum = sum + num

    return sum


total = all_sum(10,20,30,40,50)
print("Total = ",total)"""

"""
def full_name(first,last):
    name = f" {first} {last}"
    return name

result = full_name("Alu", "Mostan")
print(f"Name =  {result}")
"""

"""
def a_lot(num1,num2):
    sum = num1 + num2
    div = num1 / num2
    rem = num1 - num2
    return [sum, div, rem]


a = a_lot(40,20)

for i in a:
    print(i)
    
"""
"""

x = input("Enter product name : ")
y = int(input("Enter product price : "))
balance = int(input("Enter Your balance : "))

def shopping(item, price):
    global balance
    balance = balance - price

    print(f"Product = {item} and Price = {price} After Balance ={balance}")

shopping(x,y)
"""
"""
highest = max([1,2,3,4,5,6,7,8,9])
minimum = min([1,2,3,4,5,6,7,8,9])
add = sum([1,2,3,4,5,6,7,8,9])
lenght = len([1,2,3,4,5,6,7,8,9])

print(f"Hight = {highest},  Minimum = {minimum},  Sum ={add}, Length = {lenght}")  
"""
  
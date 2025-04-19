"""
print("Hello Python !!")
print(100)
print(200)
print(300)
print("Welcome!!")"
"""

"""
age = 25
commision = 2.5
name = "kodom Ali"
district ="Dhaka"
is_boy = True

print(type(age))
print(type(commision))
print(type(name))
print(type(district))
print(type(is_boy))

text = f"{name} lives in {district}. he gets {commision} % commision. he is {age} years old"
print(text)"
""
"""

"""
first_person = int(input("Please Enter for first person : "))
second_person = int(input("Please Enter for second person : "))
third_person = int(input("Please Enter for third person : "))

total = first_person+ second_person + third_person

print("First person : ",first_person, "  Second PErson : ",second_person, " third person : ",third_person)
print(f"Total Amount = {total}")"
""
"""

"""

num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))

print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} % {num2} = {num1%num2}")
print(f"{num1} // {num2} = {num1//num2}")"
"""
"""
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

if a>b and a>c:
    print(f"{a} is getter than {b} and {c}")
    if b>c:
        print(f"{b} is getter than {c}")
    else:
        print(f"{c} is getter then {b}")

elif b>a and b>c:
    print(f"{b} is getter than {a} and {c}")
    if a>c:
        print(f"{a} is getter than {c}")
    else:
        print(f"{c} is getter then {a}")

elif c>b and c>a:
    print(f"{c} is getter than {a} and {b}")
    if a>b:
        print(f"{a} is getter than {b}")
    else:
        print(f"{b} is getter then {a}")

elif a==b and b==c:
    print(f"{a},{b} and {c} are equal!!")
    """
"""
num = 1

while num <= 10:
    
    if num%2 == 0:
        print(num)
    
    
    num = num+1"
    """
"""
number = [1,2,3,4,5]
sum = 0

for i in number:
     
    sum = sum +i
print(sum)

text = "I love My Country "
for char in text:
    print(char)

for d in range(2,20,2):
    print(d)"
    """



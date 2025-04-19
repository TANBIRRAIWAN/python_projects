
"""
name = "Sakib Khan"
name1 = 'shakib khan'
name2 = "
     Shakib KHan 
     NUmber One 
"

print(name)
print(name1)
print(name2)

print(name1[0:6])
print(name[::-1])

if 'khan' in name1:
    print("Exist !!")


print(name.upper())



things = 'Glass', 'table', 'Chair', 'Bed','Mobile'

#print(type(things))

#print(things[2:4])

print(things[::-1])

if 'Glass' in things:
    print("Exist")


for i in things:
    print(i)



number = [1,2,3,4,5,5,2,8,9]

print(number)

number_set = set(number)
print(number_set)

number_set.add(55)
number_set.remove(3)
print(number_set)

for item in number_set:
    print(item)

if 1 in number_set:
    print("Exist")




person ={'Name': 'Modhu', 'Roll' : 25, 'class': 8, 'District': 'Kushtia'}
print(person)

print(person.keys())
print(person.values())
person['Name'] = 'ALu Mostan'
person['Language'] = 'Bangla'
print(person)



from math import *
from random import *



num = 4.33

print(ceil(num))
print(randint(1,10))
print(choice(["Sakib","Rakib","Paglu"]))


try:
    result = 30/4
    print(result)

except:
    print("Error!!")

finally:
    print("Finally here")
    

with open('message.txt','w') as file:
    file.write('I love python')
    

with open('message.txt','a') as file:
    file.write("Bangaladesh\n")
    


double = lambda x: x*x

print(double(4))

add = lambda a,b,c: a+b+c

print(add(10,20,30,))



actors = [10,20,30,40,50,60]

double = map(lambda x: x*2, actors)
print(list(double))
"""

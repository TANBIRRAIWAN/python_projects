#from test import market as m 

#a = m("Dress", 1500)

"""
number = [1,2,3,4,5,6,7,8,9]

number.append(10)
print(number)

number.insert(1,22)
print(number)

if 22 in number:
    number.remove(22)
print(number)
"""
"""
numbers = [1,2,3,4,5,6,7,8,9]
odd = []
even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

    else:
        odd.append(num)
print(even)
print(odd)
"""
"""
players = ["Sakib", "Tamim", "Liton"]
ages = [20,25,30]
for player in players:
    print(player)
    


num = int(input())

for i in range(1,num,1):
    print(i)
"""

num = (input())

reverse = num[:: -1]

if num == reverse:
    print("YES")

else:
    print("NO")

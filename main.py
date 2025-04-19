from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurent import Restaurent
from users import Admin,User, Employee,Customer

mamar_restaurent = Restaurent("mamar_restaurent")


def Customer_menu():
    name = input("Enter your name = ")
    email = input("Enter e-mail Address = ")
    phone = input("Enter phone number = ")
    address =  input("Enter your Address = ")

    customer = Customer(name = name, email = email, phone=phone, address=address)

    while True:
        print(f"Welcome...{customer.name}")
        print("1. View Menu ")
        print("2. Add Item to Cart  ")
        print("3. View Cart ")
        print("4. Pay Bill ")
        print("5. Exist !!")

        choice = int(input("Enter Your Choice = "))

        if choice == 1:
            customer.view_menu(mamar_restaurent)

        elif choice == 2:
            item_name = input("Enter Item Name : ")
            item_quantity = input("Enter Item Quantity : ")
            customer.add_to_cart(mamar_restaurent,item_name,item_quantity)
            

        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.Pay_bill()

        elif choice == 5:
            break

        else:
            print("Invalid Input !!")






def Admin_menu():
    name = input("Enter your name = ")
    email = input("Enter e-mail Address = ")
    phone = input("Enter phone number = ")
    address =  input("Enter your Address = ")

    admin = Admin(name = name, email = email, phone=phone, address=address)

    while True:
        print(f"Welcome...{admin.name}")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. View items")
        print("5. Delete item ")
        print("6. Exist !!")

        choice = int(input("Enter Your Choice = "))

        if choice == 1:
            item_name = input("Enter Item Name = ")
            item_price = int(input("Enter Item Price = "))
            item_quantity = int(input("Enter Item Quantity = "))

            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restaurent,item)



        elif choice == 2:
            name = print("Enter Employee name = ")
            email = print("Enter Employee email = ")
            phone = print("Enter Employee phone = ")
            address = print("Enter Employee address = ")
            designation = print("Enter Employee designation = ")
            salary = print("Enter Employee salary = ")
            age = print("Enter Employee age = ")
            employee = Employee(name, phone, email, address,designation,salary,age)

            admin.add_employees(mamar_restaurent,employee)


        elif choice == 3:
            admin.view_employee(mamar_restaurent)

        elif choice == 4:
            admin.view_menu(mamar_restaurent)

        elif choice == 5:
            item_name = input("Enter item name = ")
            admin.remove_item(mamar_restaurent,item_name)

        elif choice == 6:
            break
        else:
            print("Invalid Input !!")


while True:
    print("*****WELCOME******")
    print("1 . Customer")
    print("2 . Admin")
    print("3 . Exit!!")

    choice = int(input("Enter Your Choice = "))

    if choice == 1:
        Customer_menu()

    elif choice == 2:
        Admin_menu()

    elif choice ==  3:
        break

    else:
        print("Invalid Input !!")


        
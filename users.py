from abc import ABC
from orders import Order


class User:
    def __init__(self,name,phone,email,address):
        self.name  = name
        self.phone = phone
        self.email = email
        self.address = address


class Employee(User):
    def __init__(self, name, phone, email, address,designation,salary,age):
        super().__init__(name, phone, email, address)
        self.designation = designation
        self.salary = salary
        self.age = age



class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        

    def add_employees(self, restaurent , employee):
        restaurent.add_employees(employee)

    
        
    def view_employee(self,restaurent):
        restaurent.view_employee()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_items(item)

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()
        

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item  =restaurent.menu.find_item(item_name)

        if item:
            if quantity > item.quantity:
                print("No enough food avaliable!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added!!")
            
            
        else:
            print("Item not found !!")

    def view_cart(self):
        print("*****MENU*****")
        print("Name\tPrice\tQuantity\t")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price = {self.cart.total_price()}")

    def Pay_bill(self):
        print(f"You successfully paid ")
        self.cart.clear()













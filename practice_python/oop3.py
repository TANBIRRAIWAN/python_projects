"""
class shopping:
    def __init__(self,item):
        self.item = item

    @classmethod
    def display(self,product):
        print(f"You bought {product}")

    @staticmethod
    def mul(a,b):
        print(f"{a*b}")
        
s = shopping("Dress")
shopping.mul(4,5)
shopping.display("Dress")




class Ram:
    def __init__(self,ram):
        self.ram = ram

class Hard_Disc:
    def __init__(self,hard):
        self.hard = hard

class Cores:
    def __init__(self,core):
        self.core = core

class Computer:
    def __init__(self,ram_size,hard_disc,core_size):
        self.ram1 = Ram(ram_size)
        self.hard1 = Hard_Disc(hard_disc)
        self.core1 = Cores(core_size)


hp = Computer("12 GB","512","Core i 3")
c = Cores("HHHH")
print(c.core)
        

"""
'''
Create a Notebook class that will contain the fields: manufacturer, net_price, and RAM_memory.
Add two separate methods to: calculate the gross price
(+ 23% VAT) and increase the amount of RAM.
'''

class Notebook:
    def __init__(self , manufacturer, net_price, ram_memory):
        self.manufacturer = manufacturer
        self.net_price = net_price
        self.RAM_memory = ram_memory

    def calculate_gross_price(self):
        return self.net_price + 0.23*self.net_price

    def increase_ram_amount(self):
        self.RAM_memory *= 2

    def __str__(self):
        return f"\n\nManufacturer is : {self.manufacturer}\nNet price is {self.net_price}\nGross price(with VAT = 23%) is : {self.calculate_gross_price()}\nRAM memory is : {self.RAM_memory}GB\n"

notebook_1 = Notebook("Samsung", 1200, 8)
print(notebook_1)

notebook_1.increase_ram_amount()
print(f"\nNew amount of RAM is : {notebook_1.RAM_memory}GB")
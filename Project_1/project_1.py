'''
Write a DataBox class that will be tasked with collecting data and calculating its simplest statistical parameters, such as arithmetic mean, geometric mean and mode (the most frequently recurring value).

The class should have two attributes: data and amount_of_data: the first is a list to which data of type int/float will be dumped, and the second is a field indicating how much data the class object currently holds.

Methods to implement:

    .count_arithmetic_average(): a method that calculates the arithmetic average of a list of data,
    .count_geometric_average(): a method that calculates the geometric average of the data that the class object stores,
    .get_amount_of_data(): a method that returns the number of data currently stored by the DataBox object,
    .get_modal(): a method that counts the mode, that is, sets the value of the most frequently recurring data,
    .add_data(): a method that adds some data to the object. Its argument can be a number or a list of numbers. In the first case, a number will be added to the self.data attribute, in the second - all the numbers in the list of numbers.
    .remove_data(): a method that removes ALL data from the list (ie. from the self.data field).
    .get_data(): a method that returns a list of data that the object stores.

Example of calling and creating an object:

box = DataBox()

box.add_data([1,2,3,4,5])
print(box.get_data())
# >>> [1,2,3,4,5]

print(box.count_arithmetic_average())
# >>> 3

box.get_modal()
# >>> 1 # In case of inability to determine the most frequent values, we return the first element from the attribute self.data

print(box.get_amount_of_data())
# 5 # number of elements in the list self.data

box.remove_data()
print(box.get_data())
# >>> [] # After removing the data, there is no value for the self.data attribute, it is an empty list

If you want to add data of a type other than int or float to an object (in the .add_data() method), you should raise a BadDataTypeError exception - you must create such an exception beforehand.
'''

import math

class BadDataTypeError(Exception):
    pass

class DataBox:
    def __init__(self):
        self.data = []
        self.amount_of_data = 0

    def count_arithmetic_average(self):
        if not self.data:
            raise ValueError("You don't have elements to compute arithmetic average!")
        if self.amount_of_data == 0:
            raise ZeroDivisionError("You cannot divide by 0!")
        return sum(self.data) / self.amount_of_data

    def count_geometric_average(self):
        if not self.data:
            raise ValueError("You don't have elements to compute geometric average!")
        if self.amount_of_data == 0:
            raise ZeroDivisionError("You cannot divide by 0!")
        return math.pow(math.prod(self.data), 1 / self.amount_of_data)

    def get_amount_of_data(self):
        if self.amount_of_data == 0:
            raise ValueError("You don't have any elements!\nPlease input something!")
        return self.amount_of_data

    def get_modal(self):
        set_of_data = set(self.data)
        frequency_of_data = dict()
        for element in set_of_data:
            frequency_of_data[element] = self.data.count(element)
        for max_freq_elem in frequency_of_data.keys():
            if frequency_of_data[max_freq_elem] == max(frequency_of_data.values()):
                print(max_freq_elem)
                break

    def add_data(self, data):
        if isinstance(data, (int, float, list)):
            if type(data) == list:
                 for element in data:
                    if not isinstance(element, (int, float)):
                       raise BadDataTypeError("List elements must be numeric!")
                 self.data.extend(data)
            elif type(data) == int or type(data) == float:
                 self.data.append(data)
            self.amount_of_data = len(self.data)
        else:
            raise BadDataTypeError("Only int, float, or list of numbers allowed!")

    def remove_data(self):
        self.data = []
        self.amount_of_data = 0

    def get_data(self):
        return self.data


box = DataBox()

box.add_data([1, 2, 3, 4, 5])

box.get_modal()

print(box.get_data())

print(box.count_arithmetic_average())

box.get_modal()

print(box.get_amount_of_data())

box.remove_data()

print(box.get_data())
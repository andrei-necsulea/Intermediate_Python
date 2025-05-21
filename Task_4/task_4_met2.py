'''
Write a program that returns the absolute value of a number retrieved from the user.
The program should keep asking for this number until it is correctly given.
Remember that the user may not always enter a numeric value, but may also enter, for example, "cauliflower".
Check what happens then and be sure to handle exceptions.
'''

def absolute_value():
    while True:
        n = input("Please enter a number : ")
        try:
            n = complex(n)
            return abs(n)
        except ValueError:
            print("\n\nYour input value is not a number!\nPlease input a number!\n")

print(f"The absolute value is: {absolute_value()}")
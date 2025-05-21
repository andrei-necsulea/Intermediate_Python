'''
Write a program that returns the absolute value of a number retrieved from the user.
The program should keep asking for this number until it is correctly given.
Remember that the user may not always enter a numeric value, but may also enter, for example, "cauliflower".
Check what happens then and be sure to handle exceptions.
'''

def absolute_value():
  while True:
   n = input("\nPlease enter a number : ")
   try:
    if float(n):
        n = float(n)
    elif int(n):#mai mult educativ, putem sa testam direct pentru complex
        n = int(n)#(complex contine si float si int, ca la matematica)
    elif complex(n):
        n = complex(n)
    print(abs(n))
   except ValueError:
     print("\n\nYour input value is not a number!\nPlease input a number!\n")

print(absolute_value())
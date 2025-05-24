'''
Create a Fraction class to represent the fractional numbers. Each Fraction object should have two attributes: nominator and denominator. The main goal of the task is to make additional supplementation, thanks to which it will be possible to add, multiply, divide and subtract two Fraction objects from each other.

    To do this, the operators +, -, *, / should be overloaded (magic methods: add, sub, mul, truediv).
    It must be remembered that before adding the fractions, they should be reduced to a common denominator!
    For the sake of simplicity: you do not need to shorten the fractions, so the fraction 10/20 will not need to be reduced to 1/2.

Such actions should be successful:

half = Fraction(1, 2)
print(half.nominator)
#>>> 1

print(half.denominator)
#>>> 2

quarter = Fraction(1, 4)
print(quarter.nominator)
#>>> 1

print(quarter.denominator)
#>>> 4

result = half + quarter  # 1/2 + 1/4
print(result.nominator)
#>>> 6

print(result.denominator)
#>>> 8

Note that we don't want to shorten the fraction to 3/4 in this case.
The algorithm converts 1/2 to 4/8 and 1/4 to 2/8 (it just multiplies the numbers by itself).
'''

class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __add__(self, other):
        new_nominator = self.nominator * other.denominator + other.nominator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_nominator , new_denominator)

    def __sub__(self, other):
        new_nominator = self.nominator * other.denominator - other.nominator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_nominator, new_denominator)

    def __mul__(self, other):
        new_nominator = self.nominator * other.nominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_nominator, new_denominator)

    def __truediv__(self, other):
        new_nominator = self.nominator * other.denominator
        new_denominator = self.denominator * other.nominator
        return Fraction(new_nominator, new_denominator)


half = Fraction(1, 2)
print(half.nominator)

print(half.denominator)


quarter = Fraction(1, 4)
print(quarter.nominator)

print(quarter.denominator)

result = half + quarter  # 1/2 + 1/4
print(result.nominator)

print(result.denominator)
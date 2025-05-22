'''
Create a Calculator class in which you implement the actions:
    adding,
    subtraction,
    multiplication,
    dividing.
Additionaly, write simple tests that will check the correct behaviour of the aforementioned methods.
'''
def convert(n):
    try:
        return float(n)
    except ValueError:
        raise ValueError("Please input valid numbers!")


class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Calculator:
    def __init__(self):
        self.a = convert(input("\n\nInput a : "))
        self.b = convert(input("Input b : "))

        self.operation = input("Wanted Operation(+, -, *, /, exit) : ")

        match self.operation:
          case "+":
            result = Adding(self.a , self.b).get_result()
          case "-":
            result = Subtraction(self.a , self.b).get_result()
          case "*":
            result = Multiplication(self.a , self.b).get_result()
          case "/":
              try:
                  result = Dividing(self.a, self.b).get_result()
              except ZeroDivisionError as e:
                  print(e)
                  return
          case "exit":
             exit()
          case _ :
            print(ValueError("Invalid Operation!"))

        print(f"\nResult of {self.operation} is : {result}\n")

class Adding(Operation):
    def __init__(self, a, b):
     super().__init__(a , b)

    def get_result(self):
     return self.a + self.b

class Subtraction(Operation):
    def __init__(self, a, b):
     super().__init__(a , b)

    def get_result(self):
     return self.a - self.b

class Multiplication(Operation):
    def __init__(self, a, b):
     super().__init__(a , b)

    def get_result(self):
     return self.a * self.b

class Dividing(Operation):
    def __init__(self, a, b):
     super().__init__(a , b)

    def get_result(self):
        if self.b == 0:
            raise ZeroDivisionError("Dividing by zero is not allowed!")
        return self.a / self.b

def run_tests():
    assert Adding(5, 3).get_result() == 8
    assert Subtraction(10, 4).get_result() == 6
    assert Multiplication(7, 6).get_result() == 42
    assert Dividing(12, 4).get_result() == 3.0
    try:
        Dividing(5, 0).get_result()
    except ZeroDivisionError:
        print("Passed: division by zero test")
    else:
        print("Failed: division by zero test")
    print("All other tests passed!")

if __name__ == "__main__":
    run_tests()
    Calculator()
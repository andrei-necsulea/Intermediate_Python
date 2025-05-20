'''
Create a decorator called debug that will display information about the function name,
the parameters passed, and the result returned when calling the function.
'''

def debug(function_name):
    def solve_function(*args , **kwargs):
        print(f"Function: {function_name.__name__}")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        result = function_name(*args , **kwargs)
        return result
        print(f"Returned: {result}")
    return solve_function

@debug
def debug_1(a, b, c, d, e, f, g, *iterabil):
    return a, b, c, d, e, f, g, *iterabil

print(debug_1(1, 2, 3, 4, 5, 6, 7, [1,2,3,4]))
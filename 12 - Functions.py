# Functions in Python

# The general form of a Python function is:
# def function_name(arguments):
#   {lines telling the function what to do to produce the results
#   return result

# produce a function that returns x^2
def squared(x):
    result = x**2
    return result

# the_number = int(input("Enter number to be squared: "))
# print(squared(the_number))

# function to produce x^2 + y^2
def squared_addition(x, y):
    result = squared(x) + squared(y)
    return result

# first_num = int(input("Enter 1st number: "))
# second_num = int(input("Enter 2nd number: "))
# print("x^2 + y^2 = ", squared_addition(first_num, second_num))

# A new function
def born(country):
    return ("I am from " + country)


print(born("Italy"))
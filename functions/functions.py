# # Create an inner function to calculate the addition in the following way
# # 1) Create an outer function that will accept two parameters, a and b
# # 2) Create an inner function inside an outer function that will calculate the addition of a and b
# # 3) At last, an outer function will add 5 into addition and return it
#
# def outer_function(a, b):
#     def inner_function():
#         return a + b
#     return inner_function() + 5
#
# print(outer_function(5, 6))

# # Create a recursive function
# # Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# # A recursive function is a function that calls itself again and again.
#
# def recursive_function(n):
#     if (n > 0):
#         sum_of_numbers = n + recursive_function(n - 1)
#     else:
#         sum_of_numbers = 0
#     return sum_of_numbers
#
# print(recursive_function(10))

# Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

# def display_student(name, age):
#     name = input("text name here: ")
#     assert type(name) == str, "name should be string format"
#     age = input("text age here: ")
#     print(name, age)

    # try:
    #     print(x)
    # except NameError:
    #     print("Variable x is not defined")
    # except:
    #     print("Something else went wrong")

name = input("print name: ")

try:
    type(name) == str
except ValueError:
    print('Valid name, please')

print(type(name))

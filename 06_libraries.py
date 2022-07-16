from my_python_library import math_functions
import useless_functions


add_result = math_functions.add_numbers(10, 5)
multiply_result = math_functions.multiply_numbers(add_result, 5)
final_result = math_functions.divide_numbers(multiply_result, 5)

print(final_result)

useless_functions.say_hello()
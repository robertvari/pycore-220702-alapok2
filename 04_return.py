def add_numbers(a, b):
    return a+b


def multiply_numbers(a, b):
    return a*b


def divide_numbers(a, b):
    return a/b


add_result = add_numbers(10, 5)
multiply_result = multiply_numbers(add_result, 20)
final_result = divide_numbers(multiply_result, 3.5)

print(final_result)
# required positional argument
def say_hello(name):
    print(f"Hello {name}")
# say_hello("Kata")


# required positional argument
def say_hello2(name, phone, address):
    print(f"Hello {name}")
    print(f"Your phone number is: {phone}")
    print(f"Your address is: {address}")
# say_hello2("Robert", "06 20 555 6677", "Pécs")


# parameter notation: name: str, fave_numbers: lst, age: int
def say_hello3(name: str, phone: str, age: int, address: str):
    print(f"Hello {name}")
    print(f"Your phone number is: {phone}")
    print(f"Your address is: {address}")
    print(f"Your age: {age}")


# say_hello3("Robert", "06 20 555 6677", "Pécs", 30)


# call function with keyword parameters
say_hello3(
    age=40,
    address="Pécs",
    name="Kriszta",
    phone="06 20 777 8899"
)
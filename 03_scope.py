PHOTO_FOLDER_PATH = "C:\\photos"


def say_hello():
    print(PHOTO_FOLDER_PATH)


def say_hello2():
    print(PHOTO_FOLDER_PATH)
    name = "Kriszta"
    print(name)


def override_global_variable():
    global PHOTO_FOLDER_PATH
    PHOTO_FOLDER_PATH = "Csaba"


# override_global_variable()
say_hello()
say_hello2()
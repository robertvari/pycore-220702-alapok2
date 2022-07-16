#                  required positional parameters        default parameters
def registration_form(email, password1, password2, name=None, address=None, phone=None):
    if "@" not in email:
        print("Email is not valid")
        return  # early return

    if len(password1) < 6:
        print("Password must contain minimum 6 characters.")
        return

    if password1 != password2:
        print("Passwords are not the same")
        return

    if name:
        print(f"Thank you {name} for you registration")
    else:
        print("Thank you for your registration.")

    if address:
        print(f"Please review your address: {address}")

    if phone:
        print(f"Please review your phone number: {phone}")

    print(f"We sent an email to {email} with further instructions.")


registration_form(
    email="robert@gmail.com",
    password1="testpas123",
    password2="testpas123",
    name="Kriszta",
    address="Budapest",
    phone="06 20 555 6677"
)
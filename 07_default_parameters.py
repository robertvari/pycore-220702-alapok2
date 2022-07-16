def registration_form(email, password1, password2):
    if "@" not in email:
        print("Email is not valid")
        return  # early return

    if len(password1) < 6:
        print("Password must contain minimum 6 characters.")
        return

    if password1 != password2:
        print("Passwords are not the same")
        return

    print("Thank you for your registration.")
    print(f"We sent an email to {email} with further instructions.")


registration_form(
    email="robert@gmail.com",
    password1="testpas123",
    password2="testpas123",
)
def check_password(password):
    if len(password) < 8:
        return "Weak: Too short"
    elif password.isalpha() or password.isdigit():
        return "Weak: Use both letters and numbers"
    else:
        return "Strong password!"

pwd = input("Enter password: ")
print(check_password(pwd))

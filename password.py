password = "passworddasfdsdgagfsasf123"

def length_check(password):
    if len(password) < 5:
        print("Your password is too short")
    elif len(password) > 5 and len(password) < 21:
        print("Your password is an acceptable length.")
    elif len(password) > 20:
        print("Your password is way too long and may be forgotten")
    else:
        print("something went wrong")

length_check(password)

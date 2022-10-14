password = "password123"

def length_check(password):
    if len(password) < 5:
        print("Your password is too short")
    elif len(password) > 5 and len(password) < 21:
        print("Your password is an acceptable length.")
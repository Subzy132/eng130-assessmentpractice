
def is_twin(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

print(is_twin("silent", "listen"))


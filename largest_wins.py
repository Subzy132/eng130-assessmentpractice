
numbers = [4, 5, 3, 7, 32, 100, 3, 5]

def find_largest(numbers):
    largest_number = 0

    for i in numbers:
        if i > largest_number:
            largest_number = i
        else:
            pass

    return largest_number

print(find_largest(numbers))

def odd_even_counter(number):
    num_list = [0, 0]

    while number != 0:
        if number % 2 == 0:
            num_list[0] = num_list[0] + number
        else:
            num_list[1] = num_list[1] + number

        number = number - 1
    return num_list

number = int(input("Input a number:"))
print(odd_even_counter(number))





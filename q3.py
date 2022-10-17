# Write a function for checking the speed of drivers.
# This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70),
# it should give the driver one demerit point and print the total number of demerit points. For example,
# if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended

def speed_check(speed):
    demermit_point = 0

    if speed < 70:
        print('ok')
    elif speed > 70:
        a = speed - 70
        demermit_point = int(a) / 5
        print(f'you have {demermit_point} points')
        if demermit_point > 12:
            print('License suspended')

user_speed = int(input('Please enter your speed: '))
speed_check(user_speed)




# Write a program to remove characters from a string starting from zero up to n and return a new string.
#
# For example:
#
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
# Note: n must be less than the length of the string

def remove_chars(string1, a):

    if a < len(string1):
        print(string1[a:])
    else:
        print("number given is longer than string. please try again")

remove_chars("Hello World!", 3)
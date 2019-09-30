#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            number_elements = number_elements + 1
        except IndexError:
            break
    print()
    return (number_elements)

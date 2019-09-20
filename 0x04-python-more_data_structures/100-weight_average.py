#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum = 0
    sum2 = 0

    for x, y in my_list:
        sum = sum + (x * y)
        sum2 = sum2 + y
    average = sum / sum2
    return (average)

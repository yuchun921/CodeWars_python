import math


def get_average(marks):
    sum = 0
    for i in marks:
        sum += i
    avg = sum/len(marks)
    return math.floor(avg)
    raise NotImplementedError("TODO: get_average")

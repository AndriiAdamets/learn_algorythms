import math


def binary(data, item):
    min = 0
    max = len(data) - 1
    while min < max:
        index = math.ceil(min + max / 2)
        candidate = data[index]
        if candidate == item:
            return index
        if candidate > item:
            max = index
        else:
            min = index
    return -1


def add(a, b):
    return a + b

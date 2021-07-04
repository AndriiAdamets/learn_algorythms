import random


def bubble_sort(data):
    max_item_index = len(data) - 1
    for i in range(max_item_index):
        for j in range(max_item_index - i):
            if data[j] > data[j + 1]:
                temp = data[j + 1]
                data[j + 1] = data[j]
                data[j] = temp
    return data


def smallest_item_index(data):
    smallest_index = 0
    smallest_item = data[smallest_index]
    for i in range(len(data)):
        candidate = data[i]
        if candidate < smallest_item:
            smallest_item = candidate
            smallest_index = i
    return smallest_index


def selection_sort(data):
    result = []
    while len(data):
        index = smallest_item_index(data)
        result.append(data[index])
        del data[index]
    return result


def quick_sort(data):
    if len(data) < 2:
        return data
    pivot_index = random.randint(0, len(data) - 1)
    left = []
    right = []
    pivot = data[pivot_index]
    del data[pivot_index]
    for i in range(len(data)):
        if data[i] > pivot:
            right.append(data[i])
        else:
            left.append(data[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

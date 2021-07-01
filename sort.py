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

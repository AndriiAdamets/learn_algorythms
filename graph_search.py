
def width_search(graph, start_node, search_node):
    deque = graph[start_node]
    checked = []
    while len(deque):
        person = deque.pop(0)
        if person == search_node:
            return True
        else:
            deque += graph[person]
            checked += person

    return False

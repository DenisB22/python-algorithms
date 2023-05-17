def nested_loops_to_recursion(idx, collection):
    if idx == len(collection):
        print(' '.join([str(x) for x in collection]))
        return

    for num in range(1, len(collection) + 1):
        collection[idx] = num
        nested_loops_to_recursion(idx + 1, collection)


n = int(input())
collection = [0] * n


nested_loops_to_recursion(0, collection)



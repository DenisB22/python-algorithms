def reverse_arr(idx, collection):
    if idx == len(collection) // 2:
        print(' '.join(collection))
        return

    left_element = collection[idx]
    right_element = collection[len(collection) - 1 - idx]

    collection[idx] = right_element
    collection[len(collection) - 1 - idx] = left_element

    reverse_arr(idx + 1, collection)


collection = input().split()

reverse_arr(0, collection)
def gen01(collection, idx):

    if idx == len(collection):
        print(''.join([str(x) for x in collection]))
        return

    for num in range(2):
        collection[idx] = num
        gen01(collection, idx + 1)


n = int(input())
collection = [0] * n

gen01(collection, 0)

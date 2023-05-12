def calc_sum(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]

    return arr[idx] + calc_sum(arr, idx + 1)


arr = [int(x) for x in input().split()]

print(calc_sum(arr, 0))
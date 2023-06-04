def binary_search(numbers, target):
    # mid_idx = len(numbers) // 2
    # mid_el = numbers[mid_idx]
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = numbers[mid_idx]

        if mid_el == target:
            return mid_idx

        if mid_el > target:
            right = mid_idx - 1


        if mid_el < target:
            left = mid_idx + 1

    return -1


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))
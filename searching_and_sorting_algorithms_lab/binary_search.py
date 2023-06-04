# 0, 1, 2, 3, 4
# 1, 2, 3, 4, 5
# L     M  L  R

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = nums[mid_idx]

        if mid_el == target:
            return mid_idx

        if target > mid_el:
            left = mid_idx + 1

        else:
            right = mid_idx - 1

    return -1



nums = [int(x) for x in input().split()]
target = int(input())


print(binary_search(nums, target))


# TODO: try to solve this task using recursion
def merge_arrays(left, right):
    left_idx = 0
    right_idx = 0
    result_idx = 0
    result = [None] * (len(left) + len(right))

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result[result_idx] = left[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right[right_idx]
            right_idx += 1
        result_idx += 1

    while left_idx < len(left):
        result[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1

    while right_idx < len(right):
        result[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid_idx = len(nums) // 2
    left_array = nums[:mid_idx]
    right_array = nums[mid_idx:]

    return merge_arrays(merge_sort(left_array), merge_sort(right_array))


nums = [int(x) for x in input().split()]

print(*merge_sort(nums), sep=' ')



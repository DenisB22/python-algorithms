def bubble_sort(nums):
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for idx in range(len(nums) - 1):
            left = nums[idx]
            right = nums[idx + 1]

            if left > right:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                is_sorted = False

    return nums


nums = [int(x) for x in input().split()]
print(*bubble_sort(nums), sep=' ')
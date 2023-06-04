def bubble_sort(nums):
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True

        for i in range(len(nums) - 1):

            current_num = nums[i]
            next_num = nums[i + 1]

            if current_num > next_num:
                is_sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums


nums = [int(x) for x in input().split()]
print(*bubble_sort(nums), sep=' ')
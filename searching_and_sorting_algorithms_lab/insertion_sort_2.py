def insertion_sort(nums):

    for i in range(len(nums) - 1):
        curr_idx = i
        next_idx = i + 1

        curr_num = nums[curr_idx]
        next_num = nums[next_idx]

        if curr_num > next_num:
            nums[curr_idx], nums[next_idx] = nums[next_idx], nums[curr_idx]

            for j in range(i, 0, -1):
                curr_idx = j - 1
                next_idx = j
                curr_num = nums[curr_idx]
                next_num = nums[next_idx]

                if curr_num > next_num:
                    nums[curr_idx], nums[next_idx] = nums[next_idx], nums[curr_idx]

    return nums


nums = [int(x) for x in input().split()]
print(*insertion_sort(nums), sep=' ')

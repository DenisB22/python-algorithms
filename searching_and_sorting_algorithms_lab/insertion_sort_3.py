def insertion_sort(nums):
    for i in range(len(nums) - 1):

            for j in range(i + 1, 0, -1):
                curr_num = nums[i]
                next_num = nums[j]

                if next_num < curr_num:
                    nums[j], nums[i] = nums[i], nums[j]


nums = [int(x) for x in input().split()]
insertion_sort(nums)


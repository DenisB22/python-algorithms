def selection_sort(nums):
    for idx in range(len(nums)):
        current_num = nums[idx]
        min_el = current_num

        for next_idx in range(idx + 1, len(nums)):
            next_num = nums[next_idx]

            if next_num < min_el:
                min_el = next_num
                nums[idx], nums[next_idx] = nums[next_idx], nums[idx]

    return nums


nums = [int(x) for x in input().split()]
print(*selection_sort(nums), sep=' ')

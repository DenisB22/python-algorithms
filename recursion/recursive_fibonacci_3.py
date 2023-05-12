def get_fibonacci(n):

    if n == 1 or n == 0:
        return 1

    nums_sum = get_fibonacci(n - 1) + get_fibonacci(n - 2)

    return nums_sum


n = int(input())
print(get_fibonacci(n))
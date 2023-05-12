def get_fibonacci(n):
    sum_nums = 0

    if n == 1 or n == 0:
        return 1

    sum_nums += get_fibonacci(n - 1) + get_fibonacci(n - 2)

    return sum_nums


a = 5
n = int(input())
print(get_fibonacci(n))

def draw_fig(n):
    if n <= 0:
        return

    print(n * '*')
    draw_fig(n - 1)
    print(n * '#')


n = int(input())

draw_fig(n)
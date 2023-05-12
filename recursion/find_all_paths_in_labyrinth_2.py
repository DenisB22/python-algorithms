def is_not_inside(row, col, labyrinth):
    if row >= len(labyrinth) or row < 0 or col >= len(labyrinth[0]) or col < 0:
        return True


def is_exit(row, col, labyrinth):
    if labyrinth[row][col] == 'e':
        return True


def is_free(row, col, labyrinth):
    if labyrinth[row][col] == '-':
        return True


def print_path(path):
    print(''.join(path))


def mark(row, col, sign):
    labyrinth[row][col] = sign


def find_paths(row, col, direction, labyrinth, path):

    # path.append(direction)
    # print(path)

    if is_not_inside(row, col, labyrinth):
        return

    if direction:
        path.append(direction)

    if is_exit(row, col, labyrinth):
        # path.append(direction)
        print_path(path)

    # if direction:
    #     path.append(direction)
    if is_free(row, col, labyrinth):
        mark(row, col, 'v')
        find_paths(row - 1, col, 'U', labyrinth, path)
        find_paths(row + 1, col, 'D', labyrinth,  path)
        find_paths(row, col + 1, 'R', labyrinth, path)
        find_paths(row, col - 1, 'L', labyrinth, path)
        mark(row, col, '-')
    if path:
        path.pop()


x = int(input())
y = int(input())

labyrinth = [[element for element in input()] for row in range(x)]
find_paths(0, 0, '', labyrinth, [])

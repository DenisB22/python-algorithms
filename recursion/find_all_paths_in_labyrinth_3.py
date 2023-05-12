def is_outside(lab, row, col):
    if row >= len(lab) or col >= len(lab[0]) or row < 0 or col < 0:
        return True


def mark(lab, row, col, sign):
    lab[row][col] = sign


def is_exit(lab, row, col):
    if lab[row][col] == 'e':
        return True


def is_available(lab, row, col):
    if lab[row][col] == '-':
        return True


def find_path(lab, row, col, direction, path):

    if is_outside(lab, row, col):
        return

    if direction:
        path.append(direction)

    if is_exit(lab, row, col):
        print(''.join(path))

    if is_available(lab, row, col):
        mark(lab, row, col, 'v')
        find_path(lab, row + 1, col, 'D', path)
        find_path(lab, row - 1, col, 'U', path)
        find_path(lab, row, col + 1, 'R', path)
        find_path(lab, row, col - 1, 'L', path)
        mark(lab, row, col, '-')

    if path:
        path.pop()


x = int(input())
y = int(input())
lab = [[el for el in input()] for row in range(x)]
find_path(lab, 0, 0, '', [])
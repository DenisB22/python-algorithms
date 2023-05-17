class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def connected_areas_count(row, col, matrix):

    if row >= len(matrix) or col >= len(matrix[0]) or row < 0 or col < 0:
        return 0

    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'

    count = 1
    count += connected_areas_count(row + 1, col, matrix)
    count += connected_areas_count(row - 1, col, matrix)
    count += connected_areas_count(row, col + 1, matrix)
    count += connected_areas_count(row, col - 1, matrix)

    return count


rows = int(input())
cols = int(input())
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        size = connected_areas_count(row, col, matrix)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for idx, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')
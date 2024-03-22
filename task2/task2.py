f = open('input02.txt', 'r', encoding='utf-8')
lines = f.readlines()

matrix = []
for line in lines:
    values = line.split()
    boolean_values = []
    for value in values:
        if value == 'True':
            boolean_values.append(True)
        else:
            boolean_values.append(False)
    matrix.append(boolean_values)


def add_border(matrix):
    r = len(matrix)
    c = len(matrix[0]) if r > 0 else 0

    new_matrix = [[0 for _ in range(c + 2)] for _ in range(r + 2)]

    for z in range(r):
        for x in range(c):
            new_matrix[z + 1][x + 1] = matrix[z][x]

    return new_matrix


bordered_matrix = add_border(matrix)
square = 0
w, h = -1, -1
coord_x, coord_y = -1, -1

# for row in bordered_matrix:
# #     print(*row)

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):

        if matrix[i][j]:

            left = j
            right = j

            for k in range(left + 1, cols):
                if matrix[i][k]:
                    right = k
                else:
                    break

            width = right - left + 1

            found_break = False
            height = 1
            for g in range(i + 1, rows):
                for h in range(left, right + 1):
                    if not matrix[g][h]:
                        found_break = True
                        break
                if found_break:
                    break
                height += 1

            s = height * width
            if s <= square:
                continue

            warning = False

            for a in range(left, right + 3):
                if bordered_matrix[i][a]:
                    warning = True
                    break

            for b in range(left, right + 3):
                if bordered_matrix[i + height + 1][b]:
                    warning = True
                    break

            for c in range(i, i + height + 2):
                if bordered_matrix[c][left]:
                    warning = True
                    break

            for d in range(i, i + height + 2):
                if bordered_matrix[d][right + 2]:
                    warning = True
                    break

            if warning:
                continue

            square = s
            w = width
            h = height
            coord_x = i
            coord_y = j

print(coord_x, coord_y, w, h)

f = open('output02.txt', 'w')
f.write(str(coord_x) + " " + str(coord_y) + " " + str(w) + " " + str(h))
f = open('input03_1.txt', 'r')
lines = f.readlines()

arr = []
for line in lines:
    arr.append([int(elem) for elem in line.split(' ')])


def join_segments(segments):
    segments.sort(key=lambda x: x[0])
    joined_segments = [segments[0]]

    for segment in segments[1:]:
        if segment[0] <= joined_segments[-1][1]:
            joined_segments[-1][1] = max(segment[1], joined_segments[-1][1])
        else:
            joined_segments.append(segment)
    return joined_segments


print(arr)
new_arr = join_segments(arr)
print(new_arr)

f = open('output03.txt', 'w')
for segment in new_arr:
    for elem in segment:
        f.write(str(elem) + ' ')
    f.write('\n')

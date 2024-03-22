f = open('input01.txt', 'r')
lines = f.readlines()

arr1 = [int(elem) for elem in lines[0].split(', ')]
arr2 = [int(elem) for elem in lines[1].split(', ')]
new_arr = []

for num in arr1:
    for divider in arr2:
        if divider not in (-1, 0, 1) and num != abs(divider) and num % divider == 0:
            new_arr.append(num)
            break
print(new_arr)

f = open('output01.txt', 'w')
for elem in new_arr:
    f.write(str(elem) + ' ')

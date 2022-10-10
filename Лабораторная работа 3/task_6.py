list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max = 0
index = 0
for pos, value in enumerate(list_numbers):
    if max < value:
        max = value
        index = pos
[list_numbers[index], list_numbers[-1]] = [list_numbers[-1], list_numbers[index]]

print(list_numbers)

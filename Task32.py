def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if lst[i] >= min_val and lst[i] <= max_val:
            indexes.append(i)
    return indexes

massiv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_num = 3
max_num = 7

result = find_indexes(massiv, min_num, max_num)
print("Индексы элементов, принадлежащих заданному диапазону:")
print(result)
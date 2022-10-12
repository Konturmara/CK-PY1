def delete(list_, index=None):
    if index == None:
        index = len(list_)-1
    res = []
    left_list_ = list_[:index]
    right_list_ = list_[index + 1:]
    res = left_list_ + right_list_
    return res
    ...  # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

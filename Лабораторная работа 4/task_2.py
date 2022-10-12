def get_count_char(str_):
    res_dict = {}
    work_str_ = str_.lower().split(' ')
    for word in work_str_:

        for letter in word:
            if (letter.isalpha()):
                if letter in res_dict:
                    res_dict[letter] += 1  # оценку уже встречали, поэтому увеличиваем количество
                else:
                    res_dict[letter] = 1

    return res_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

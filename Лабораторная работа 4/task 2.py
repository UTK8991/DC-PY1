def get_count_char(str_):
    dict = {}
    for letter in str_.lower():
        if letter.isalpha():
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
    return dict

def percent_count(dict_):
    sum_ = 0
    for value in dict_.values():
        sum_ += value
    percent_dict = {}
    for key, value in dict_.items():
        percent_dict[key] = round(value / sum_ * 100, 2)
    return percent_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
count_dict = get_count_char(main_str)

print(count_dict)
print(percent_count(count_dict))
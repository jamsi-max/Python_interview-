# 3. Создать два списка с различным количеством элементов. В первом должны быть записаны 
# ключи, во втором — значения. Необходимо написать функцию, создающую из данных ключей и 
# значений словарь. Если ключу не хватает значения, в словаре для него должно сохраняться 
# значение None. Значения, которым не хватило ключей, необходимо отбросить.
from itertools import zip_longest


def get_dict(key, value):
    if len(key) > len(value):
        print(dict(zip_longest(key, value)))
    else:
        print(dict(zip(key, value)))


def main():
    list_key = ['user_1', 'user_5', 'user_11', 'user_2']
    list_value = ['pass_1', 'pass_5', 'pass_11', 'pass_2', 'pass_8', 'pass_3']
    get_dict(list_key, list_value)
    list_key = ['user_1', 'user_5', 'user_11', 'user_2', 'user_8', 'user_3']
    list_value = ['pass_1', 'pass_5', 'pass_11']
    get_dict(list_key, list_value)


if __name__ == '__main__':
    main()


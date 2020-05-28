# 1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
# Первый и второй множитель должны задаваться в виде аргументов функции.
# Значения каждой строки таблицы должны быть представлены списком, который
# формируется в цикле. После этого осуществляется вызов внешней lambda-функции,
# которая формирует на основе списка строку. Полученная строка выводится в 
# главной функции. Элементы строки (элементы таблицы умножения) должны 
# разделяться табуляцией.


# Долго вникал в ТЗ так и не понял, что нужно использовать просто lambda или 
# внешнюю функцию... сделал и так и так
def get_str(x,y):
    return f'{x}\tX\t{y}\t=\t{x*y}'


def mul_table(a, b):
    for x in range(1,a+1):
        for y in range(1,b+1):
            print((lambda x, y: f'{x}\tX\t{y}\t=\t{x*y}')(x, y))
            #print(get_str(x,y)) 


# 2. Функция принимает имя каталога и распечатывает его содержимое
#     в виде «путь и имя файла», а также любые другие
#     файлы во вложенных каталогах.

#     Эта функция подобна os.walk. Использовать функцию os.walk
#     нельзя. Данная задача показывает ваше умение работать с 
#     вложенными структурами.

import os
def print_directory_contents(sPath):
    try:
        for obj in os.listdir(sPath):
            path_obj = os.path.join(sPath, obj)
            if os.path.isdir(path_obj):
                print_directory_contents(path_obj)
            else:
                print(sPath, obj, sep=' -> ')
    except FileNotFoundError:
        print('The directory was not found. Check that the path is correct')


#  3. Разработать генератор случайных чисел. В функцию передавать начальное и 
#     конечное число генерации (нуль необходимо исключить). Заполнить этими 
#     данными список и словарь. Ключи словаря должны создаваться по шаблону: 
#     “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.       

# Многовато циклов, но каак убрать рационально по памяти 0 пришёл только к такому решению
import random
def get_rnd(min, max):
    if min - max:
        rnd_list = random.choices([_ for _ in range(min, max+1) if _ != 0], k=10)
        rnd_dict = {}
        for i in range(10):
            rnd_dict[i] = random.choice([_ for _ in range(min, max+1) if _ != 0])
        print(rnd_list)
        print(rnd_dict)
    else:
        print('The values of the variables match!')


# 4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами. 
# Клиент банка делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется 
# процентная ставка: 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых). 
# 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых). 100000–1000000 
# руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых). Необходимо написать функцию,
#  в которую будут передаваться параметры: сумма вклада и срок вклада. Каждый из трех банковских 
# продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24). Ключам 
# соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого 
# срока. В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять 
# расчет по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.

def deposit(sum, term):
    min_package = {
        'begin_sum': 1000,
        'end_sum': 10000,
        6: 0.05,
        12: 0.06,
        24: 0.05
    }

    ave_package = {
        'begin_sum': 10000,
        'end_sum': 100000,
        6: 0.06,
        12: 0.07,
        24: 0.065
    }

    max_package = {
        'begin_sum': 100000,
        'end_sum': 1000000,
        6: 0.07,
        12: 0.08,
        24: 0.075
    }
    if sum < min_package['begin_sum']:
        print('Insufficient Deposit amount!')
    elif sum < min_package['end_sum']:
        print(f'Deposit amount at the end of the term: {sum+sum*min_package[term]}.')
    elif sum < ave_package['end_sum']:
        print(f'Deposit amount at the end of the term: {sum+sum*ave_package[term]}.')
    elif sum <= max_package['end_sum']:
        print(f'Deposit amount at the end of the term: {sum+sum*max_package[term]}.')
    else:
        print(f'too much money')


# 5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться 
# фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную 
# функцию подсчета процентов для пополняемой суммы. Примем, что клиент вносит средства в последний день 
# каждого месяца, кроме первого и последнего. Например, при сроке вклада в 6 месяцев пополнение 
# происходит в течение 4 месяцев. Вложенная функция возвращает сумму дополнительно внесенных средств 
# (с процентами), а главная функция — общую сумму по вкладу на конец периода.

def deposit_v2(sum, term, repl):
    min_package = {
        'begin_sum': 1000,
        'end_sum': 10000,
        6: 0.05,
        12: 0.06,
        24: 0.05
    }

    ave_package = {
        'begin_sum': 10000,
        'end_sum': 100000,
        6: 0.06,
        12: 0.07,
        24: 0.065
    }

    max_package = {
        'begin_sum': 100000,
        'end_sum': 1000000,
        6: 0.07,
        12: 0.08,
        24: 0.075
    }

    def add_income(term, repl, rate):
        return (term-2)*repl+(term-2)*repl*rate


    if sum < min_package['begin_sum']:
        print('Insufficient Deposit amount!')
    elif sum < min_package['end_sum']:
        print(f'Deposit amount at the end of the term: {sum+sum*min_package[term]}.')
        print(f'Additional income from deposited funds: {add_income(term, repl, min_package[term])}.')
    elif sum < ave_package['end_sum']:
        print(f'Deposit amount at the end of the term: {sum+sum*ave_package[term]}.')
        print(f'Additional income from deposited funds: {add_income(term, repl, ave_package[term])}.')
    elif sum <= max_package['end_sum']:
        print(f'Deposit amount at the end of the term: {sum+sum*max_package[term]}.')
        print(f'Additional income from deposited funds: {add_income(term, repl, max_package[term])}.')
    else:
        print(f'too much money')


def main():
    # mul_table(2, 8)
    # print_directory_contents('/home/device/Рабочий стол/Python interview')
    # get_rnd(-4, 2)
    # deposit(10071, 6)
    deposit_v2(1000, 6, 10)


if __name__ == '__main__':
    main()


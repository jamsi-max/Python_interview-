# 5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке
#  часть строковых значений заменить на значения типа example345 (строка+число). Далее — 
# усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных). 
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: 
# вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок 
# на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы только
#  в начале и конце — например, example345.
import os, sys, random, re

# надеюсь правильно понял задачу!!!
def read_file(file_name, find_str):
    with open(file_name) as f:
        text = f.read()
        print(re.search(f'{find_str}', text).start())
        print(re.findall(f'{find_str}', text))
        print(re.sub(r'\b\d+', '#', text)) # меняем все цифры отдельно стоящие на #
        print(re.findall(r'\b\w+\d{3}\b', text)) # находим example345 по шаблону начало слова потом буквы потом три цифры потом конец слова


def create_file(file_name):
    if os.path.isfile(file_name):
        print('The file already exists. Enter a different name')
    else:
        list_first = [_ for _ in 'asjkencbjsdmnvijKJNiwnweijw']
        for i in range(7):
            list_first[random.randint(0, len(list_first)-1)] = ' example345'

        list_second = [_ for _ in range(20)]

        with open(file_name, 'w') as f:
            for text, num in zip(list_first, list_second):
                f.write(text+' '+str(num))
        read_file(file_name, 'example345')
        


def main():
    try:
        create_file(sys.argv[1])
    except IndexError:
        print('Enter the name of the file you want to create')


if __name__ == '__main__':
    main()


# 4. Написать программу, в которой реализовать две функции. В первой должен создаваться 
# простой текстовый файл. Если файл с таким именем уже существует, выводим соответствующее
#  сообщение. Необходимо открыть файл и подготовить два списка: с текстовой и числовой 
# информацией. Для создания списков использовать генераторы. Применить к спискам функцию 
# zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл 
# таким образом, чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать 
# вторую функцию. В нее должна передаваться ссылка на созданный файл. Во второй функции 
# необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся программа
#  должна запускаться по вызову первой функции.
import os, sys


def read_file(file_name):
    with open(file_name) as f:
        print(f.read())
        # тут не совсем понял вообщем и так и так сделал
        # print(f.readlines())

def create_file(file_name):
    if os.path.isfile(file_name):
        print('The file already exists. Enter a different name')
    else:
        list_first = [_ for _ in 'asjkencbjsdmnvijKJNiwnweijw']
        list_second = [_ for _ in range(20)]
        with open(file_name, 'w') as f:
            for text, num in zip(list_first, list_second):
                f.write(text+' - '+str(num)+'\n')
        read_file(file_name)
        


def main():
    try:
        create_file(sys.argv[1])
    except IndexError:
        print('Enter the name of the file you want to create')


if __name__ == '__main__':
    main()


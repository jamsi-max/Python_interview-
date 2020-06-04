# 1. Написать программу, которая будет содержать функцию для получения имени файла из 
# полного пути до него. При вызове функции в качестве аргумента должно передаваться 
# имя файла с расширением. В функции необходимо реализовать поиск полного пути по имени
#  файла, а затем «выделение» из этого пути имени файла (без расширения).
import os, sys


def get_name(file_name):
    if os.path.isfile(file_name):
        print(os.path.abspath(file_name).split('/')[-1].split('.')[0])
    else:
        print('File not found!')


def main():
    try:
        get_name(sys.argv[1])
    except:
        print('File not found or argument!')


if __name__ == '__main__':
    main()


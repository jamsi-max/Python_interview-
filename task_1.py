# 2. Написать программу, которая запрашивает у пользователя ввод числа. 
# На введенное число она отвечает сообщением, целое оно или дробное. 
# Если дробное — необходимо далее выполнить сравнение чисел до и после 
# запятой. Если они совпадают, программа должна возвращать значение True, 
# иначе False.
import os


def compare():
    num = input('Enter nmber: ')
    if '.' in num or ',' in num:
        print(f'The entered number {num} is an float')
        print('True') if len(set(num.split('.'))) == len(set(num.split(','))) else print('False')
    else:
        print (f'The entered number {num} is an integer')


def main():
    compare()


if __name__ == '__main__':
    main()


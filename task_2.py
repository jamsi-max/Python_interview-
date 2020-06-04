# 3. Написать программу, которая запрашивает у пользователя ввод числа. 
# На введенное число она отвечает сообщением, целое оно или дробное. Если 
# дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если 
# они совпадают, программа должна возвращать значение True, иначе False.
import os

# тут сделал через множество если разрезать строку и конвертировать во множество то полученый 
# лист в случае если дробная и целая части совпадают будет иметь длину равную 1
def compare():
    num = input('Enter your number: ')
    try:
        float(num)
    except:
        print('You entered not a number!!!')
    else:
        if '.' in num:
            print(f'Number {num} is float')
            if len(set(num.split('.'))) == 1:
                print('Integer and fractional parts match!!!')
            else:
                print('The whole and and fractional parts are different!')
        else:
            print(f'Number {num} is integer!')      


def main():
    compare()


if __name__ == '__main__':
    main()


# Пересматриваю лекции понял ошибку в 1 ДЗ переделал вывод таблицы умножения в
# соответствии с ТЗ

def get_str(mlt, arr):
    return list(mlt*x for x in arr) if mlt else list(x for x in arr)
 
def mlt_table(a,b):
    for y in range(b+1):
        print(y, *get_str(y, [_ for _ in range(1, a+1)]), sep='\t')
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# 1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский
#  (ItemDiscount), должен содержать статическую информацию о товаре: название и цену. Второй — 
# дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data), отвечающую за 
# отображение информации о товаре в одной строке. Проверить работу программы, создав экземпляр 
# (объект) родительского класса.

# class ItemDiscount:

#     def __init__(self, name, price):    
#         self.name = name
#         self.price = price


# class ItemDiscountReport(ItemDiscount):

#     def get_parent_data(self):
#         print(f'Product - {self.name}\nPrice - {self.price} $')


# 2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что 
# при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.

# class ItemDiscount:
    
#     def __init__(self, name, price):    
#         self.__name = name
#         self.__price = price


# class ItemDiscountReport(ItemDiscount):
    
#     def get_parent_data(self):
#         print(f'Product - {self.__name}\nPrice - {self.__price} $')


# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным 
# переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.

# class ItemDiscount:
    
#     def __init__(self, name, price):    
#         self.__name = name
#         self.__price = price

#     def get_name(self):
#         return self.__name

#     def get_price(self):
#         return self.__price


# class ItemDiscountReport(ItemDiscount):

#     def get_parent_data(self):
#         print(f'Product - {self.get_name()}\nPrice - {self.get_price()} $')


# 4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский,
# и дочерний классы получили новое значение цены. Следует проверить это, вызвав соответствующий 
# метод родительского класса и функцию дочернего (функция, отвечающая за отображение информации 
# о товаре в одной строке).

# class ItemDiscount:
    
#     def __init__(self, name, price):    
#         self.__name = name
#         self.__price = price

#     def get_name(self):
#         return self.__name

#     def get_price(self):
#         return self.__price

#     def set_price(self, price):
#         if price >= 0:
#             self.__price = price
#         else:
#             raise ValueError("The price can't be negative!")


# class ItemDiscountReport(ItemDiscount):

#     def get_parent_data(self):
#         print(f'Product - {self.get_name()}\nPrice - {self.get_price()} $')


# 5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве 
# аргумента в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса 
# (метод init, в который должна передаваться переменная — скидка), и перегрузку метода str 
# дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — цена 
# товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и 
# родительский классы (вторая и третья строка после объявления дочернего класса).

# class ItemDiscount:
    
#     def __init__(self, name, price):    
#         self.__name = name
#         self.__price = price

#     def get_name(self):
#         return self.__name

#     def get_price(self):
#         return self.__price

#     def set_price(self, price):
#         if price >= 0:
#             self.__price = price
#         else:
#             raise ValueError("The price can't be negative!")


# class ItemDiscountReport(ItemDiscount):

#     def __init__(self, name, price, discount=0):
#         super().__init__(name, price)
#         self.discount = discount

#     def __str__(self):
#         return f'{round(self.get_price() - (self.discount / 100 * self.get_price()), 2)}'

#     def get_parent_data(self):
#         print(f'Product - {self.get_name()}\nPrice - {self.get_price()} $')

# 6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс 
# ItemDiscountReport на два класса. Инициализировать классы необязательно. Внутри каждого 
# поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара, 
# а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.

class ItemDiscount:
    
    def __init__(self, name, price):    
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("The price can't be negative!")


class ItemDiscountReportFirst(ItemDiscount):

    def get_parent_data(self):
        print(f'Product - {self.get_name()}\nPrice - {self.get_price()} $')
    
    def get_info(self):
        print(self.get_name()) 


class ItemDiscountReportSecond(ItemDiscount):

    def get_parent_data(self):
        print(f'Product - {self.get_name()}\nPrice - {self.get_price()} $')

    def get_info(self):
        print(self.get_price()) 


def main():
    # mlt_table(10, 10)
    
    # 1
    # cup = ItemDiscount('Cups_1', 2.45)
    # cup.get_parent_data()
    # не работает так как родитель ничего не знает про дочерний класс
    # cup = ItemDiscountReport('Cups_1', 2.45)
    # cup.get_parent_data()
    # работает
    
    # 2
    # cup = ItemDiscountReport('Cups_1', 2.45)
    # cup.get_parent_data()
    # доступ к свойствам объекта напрямую отсутствует

    # 3
    # cup = ItemDiscountReport('Cups_1', 2.45)
    # cup.get_parent_data()

    # 4
    # cup = ItemDiscountReport('Cups_1', 2.45)
    # cup.set_price(3.57)
    # print(cup.get_price())
    # cup.get_parent_data()

    # 5
    # cup = ItemDiscountReport('Cups_1', 2.54, 10)
    # print(cup)

    # 6
    cup_1 = ItemDiscountReportFirst('Cups_1', 2.54)
    cup_2 = ItemDiscountReportSecond('Cups_2', 2.54)
    
    # 6.1
    print('*'*50)
    cup_1.get_info()
    cup_2.get_info()
    #6.2
    print('*'*50)
    for obj in (cup_1, cup_2):
        obj.get_info()
    #6.3
    print('*'*50)
    def get_info_obj(obj):
        obj.get_info()
    
    get_info_obj(cup_1)
    get_info_obj(cup_2)


if __name__ == '__main__':
    main()


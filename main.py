# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 99)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                item = self.tableWidget.item(row, col).text()
                col += 1
            row += 1
            col = 0
        list_information_max_num = find_max(self.tableWidget)
        if not list_information_max_num:
            self.label_error.setText('Введены некорректные данные!')
        else:
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1]) + ';' + str(list_information_max_num[2]) + ']')
    def solve(self):
        list_information_max_num = find_max(self.tableWidget)

        index_i = list_information_max_num[1]
        index_j = list_information_max_num[2]
        row = 0
        col = 0
        limit = 0
        if index_i > 0:
            limit = self.tableWidget.rowCount() * index_i + index_j
        else:
            limit = index_j
        z = 0
        count = 0
        l = True

        for row in range(self.tableWidget.rowCount()):
            for col in  range(self.tableWidget.columnCount()):
                if limit > 0 and z <= limit:
                    number = float(self.tableWidget.item(row, col).text())
                    if number % 2 == 0:
                        print(number)
                        count = count + 1
                else:
                    l = False
                    break
                z = z + 1
            if l == False:
                break

        item = QTableWidgetItem()
        item.setText(str(list_information_max_num[0] + count))
        self.label_sum.setText("Количество четных чисел перед максимальным элементом:" + str(count))
        self.tableWidget.setItem(index_i,index_j,item)
        count = 0

def find_max(table_widget):
    """
    находим максимальное число из таблицы и его координаты
    :param table_widget: таблица
    :return: [max_num, row_max_number, col_max_number], если выкинуто исключение,
            то None
    """

    row_max_number = 0  # номер строки, в котором находится максимальне число
    col_max_number = 0  # номер столбца, в котором находится максимальне число
    max_num = float(table_widget.item(row_max_number, col_max_number).text())  # Максимальное значение

    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number > max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number]
    except Exception:
        return None







def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

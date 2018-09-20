import xlrd
from xlutils.copy import copy
import os
import shutil

from model import Model


def find_row_number(sheet):
    nrows = sheet.nrows
    while True:
        flag = False
        for i in range(0, 12):
            if sheet.cell_value(nrows - 1, i):
                flag = True
                break
        if not flag:
            nrows -= 1
        else:
            break
    return nrows


def find_url(sheet, row_number, url):
    for i in range(1, row_number):
        if sheet.cell_value(i, 11) == url:
            return True
    return False


def write(name, pt, model: Model):
    old_excel = xlrd.open_workbook(name, formatting_info=True)
    old_sheet = old_excel.sheet_by_index(0)
    row_number = find_row_number(old_sheet)
    if not find_url(old_sheet, row_number, model.url):
        new_excel = copy(old_excel)
        new_sheet = new_excel.get_sheet(0)
        new_sheet.write(row_number, 0, pt)
        new_sheet.write(row_number, 1, model.room_name)
        new_sheet.write(row_number, 2, model.location)
        new_sheet.write(row_number, 3, model.get_type)
        new_sheet.write(row_number, 4, model.tingshi)
        new_sheet.write(row_number, 5, model.prise)
        new_sheet.write(row_number, 6, model.first_prise)
        new_sheet.write(row_number, 7, model.total_prise)
        new_sheet.write(row_number, 8, model.size)
        new_sheet.write(row_number, 9, model.chaoxiang)
        new_sheet.write(row_number, 10, model.floor + '/' + model.total_floor)
        new_sheet.write(row_number, 11, model.url)
        new_sheet.write(row_number, 12, model.desc)
        new_sheet.write(row_number, 13, model.to_ziroom)
        new_sheet.write(row_number, 14, model.to_tiger)
        new_excel.save(name)


def clear():
    xls_name = './zhaofang.xls'
    xls_bak_name = './zhaofang-bak.xls'
    if os.path.exists(xls_name):
        os.remove(xls_name)
    shutil.copy(xls_bak_name, xls_name)
    pass


if __name__ == '__main__':
    clear()

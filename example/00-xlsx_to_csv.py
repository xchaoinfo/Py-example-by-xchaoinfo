#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-05-15 23:50:31
# @Author  : xchaoinfo (xchaoinfo@qq.com)
# @Link    : https://github.com/xchaoinfo
# @Version : v.0.0
"""csv 和 excel 快速转换的小工具"""


import openpyxl
import csv
import pyexcelerate


def csv_to_excel(fn="test.csv", coding="utf-8"):
    with open(fn, encoding=coding) as fr:
        rows = csv.reader(fr)
        data = [r for r in rows]
    wb = pyexcelerate.Workbook()
    wb.new_sheet(fn.split(".")[0], data=data)
    wb.save(fn.replace("csv", 'xlsx'))


def xlsx_to_csv(fn):
    ''' change xlsx or xls file to csv depends on openpyxl '''
    wb = openpyxl.load_workbook(filename=fn, read_only=True)
    sheet_name = wb.get_sheet_names()
    # print(sheet_name)  # 查看 excel 共有几张表
    sheet = wb[sheet_name[0]]  # 选择操作 excel 文件的第一张表
    with open('sample.csv', 'w', newline='', encoding='utf-8') as fw:
        ww = csv.writer(fw)
        for r in sheet.rows:
            row = [i.value for i in r]
            ww.writerow(row)

if __name__ == '__main__':
    fn = "sample.xlsx"
    xlsx_to_csv(fn)

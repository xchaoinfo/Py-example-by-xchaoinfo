#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-02-26 22:59:55
# @Author  : xchaoinfo (xchaoinfo)
# @github  : https://github.com/xchaoinfo
"""多种方式读写 csv 文件的 Demo"""
import csv
"""
data1.csv 的内容是

张三,北京,25
李四,上海,30

data2.csv 的内容是

姓名,城市,年龄
张三,北京,25
李四,上海,30

"""


# example 1 读取 csv 返回列表
def read_csv(fn='data1.csv'):
    """
    data1.csv 中数据格式，
    读取返回列表比较容易处理

    """
    # 读取打印 - reader-example1
    with open(fn, encoding="utf-8") as fr:
        csvfr = csv.reader(fr)
        for row in csvfr:
            print(", ".join(row))

    # 读取后，返回列表 - reader-example
    with open(fn, encoding="utf-8") as fr:
        csvfr = csv.reader(fr)
        rows = [row for row in csvfr]
    return rows


# example 2 读取 csv 返回列表
def read_csv_dict(fn="data2.csv"):
    """
    data2.csv 的数据格式，
    读取返回字典比较容易处理

    """
    with open(fn, encoding="utf-8") as fr:
        dict_rows = csv.DictReader(fr, fieldnames=None)
        # 不指定 fieldnames 的情况下
        # 默认第一行数据作为 fieldnames
        for row in dict_rows:
            print(row)  # row 是一个字典


# example 3 list 或 tuple 写入到 csv
def write_csv(fn="data1.csv"):
    """
    可以通过指定带 BOM 的 UTF-8 的编码方式，
    解决 Excel 直接打开 csv 乱码的问题
    即 encoding="utf-8-sig"
    """
    # with open(fn, 'w', newline="", encoding="utf-8-sig") as fw:
    with open(fn, 'w', newline="", encoding="utf-8") as fw:
        fwcsv = csv.writer(fw)
        one = ("张三", "北京", "25")  # tuple
        two = ["李四", "上海", "30"]  # list
        fwcsv.writerow(one)
        fwcsv.writerow(two)


# example 4 dict 写入到 csv 中
def write_dict_csv(fn="data2.csv"):
    dict1 = {
        "姓名": "张三",
        "城市": "北京",
        "年龄": "25"
    }
    dict2 = {
        "姓名": "李四",
        "城市": "上海",
        "年龄": "30"
    }
    fieldnames = ["姓名", "城市", "年龄"]

    # with open(fn, 'w', newline="", encoding="utf-8-sig") as fwd:
    with open(fn, 'w', newline="", encoding="utf-8") as fwd:
        fwdcsv = csv.DictWriter(fwd, fieldnames=fieldnames)
        fwdcsv.writeheader()
        fwdcsv.writerow(dict1)
        fwdcsv.writerow(dict2)


if __name__ == '__main__':
    write_dict_csv()
    write_csv()
    read_csv()
    read_csv_dict()

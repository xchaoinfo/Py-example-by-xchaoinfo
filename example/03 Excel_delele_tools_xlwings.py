#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-03-16 14:14:03
# @Author  : xchaoinfo (xchaoinfo)
# @github  : https://github.com/xchaoinfo
"""通过调用 xlwings 删除 Excel 文件中的特定内容"""
import xlwings as xw

fn = "data.xlsx"


class DeleteTools(object):
    """删除满足某些条件的行
    data.xlsx 中有很多重复的数据
    需要删除那些重复的
    """

    def __init__(self, fn):
        super(DeleteTools, self).__init__()
        self.ExistSet = set()
        self.ToDelList = list()
        self.fn = fn

    def rule(self, value):
        # 可以自定义规则来操作
        pass

    def Delete(self):
        # visible 控制 Excel 打开是否显示界面
        # add_book 控制是否添加新的 workbook
        app = xw.App(visible=True, add_book=False)
        # app.display_alerts = False

        # 打开 data.xlsx 文件到 wookbook 中
        wb = app.books.open(fn)
        # 切换到当前活动的 sheet 中
        sheet = wb.sheets.active

        # 选择 A1 所在的一列
        # 当 Excel 格式复杂的时候,不建议使用 expand
        # 可以这样选择
        ARange = sheet.range("A1:A100")
        # ARange = sheet.range("A1").expand("down")
        for A in ARange:
            if str(A.value).strip() not in self.ExistSet:
                self.ExistSet.add(str(A.value).strip())
            else:
                # address = A.address
                # 获取 A 所在的位置坐标
                self.ToDelList.append(A.address)
                # print(A.value)

        while self.ToDelList:
            td = self.ToDelList.pop()
            # 删除 A 所在的一行
            sheet.range(td).api.EntireRow.Delete()
        # 保存 wookbook
        # 相当于Excel 的 Ctrl+S 快捷键
        sheet.autofit()
        wb.save()
        app.quit()


if __name__ == '__main__':
    d = DeleteTools(fn)
    d.Delete()

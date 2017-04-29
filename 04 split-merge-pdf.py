#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-04-29 23:03:57
# @Author  : xchaoinfo (xchaoinfo)
# @github  : https://github.com/xchaoinfo
"""
pip install PyPDF2
"""

from PyPDF2 import PdfFileReader, PdfFileWriter


def split_pdf(infn, outfn):
    pdf_output = PdfFileWriter()
    pdf_input = PdfFileReader(open(infn, 'rb'))
    # 获取 pdf 共用多少页
    page_count = pdf_input.getNumPages()
    print(page_count)
    # 将 pdf 第五页之后的页面，输出到一个新的文件
    for i in range(5, page_count):
        pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))


def merge_pdf(infnList, outfn):
    pdf_output = PdfFileWriter()
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        print(page_count)
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))


if __name__ == '__main__':
    infn = 'infn.pdf'
    outfn = 'outfn.pdf'
    split_pdf(infn, outfn)

# Py-sample-by-xchaoinfo

小而美, 提高生活幸福感的Python脚本, By xchaoinfo.                                    
## 目录


- 00 xlsx_to_csv.py
    
    csv 和 excel 快速转换的小工具

- 01 connect_to_mysql.py
    
    通过 Python 连接 Mysql 的 Demo

- 02 csv_example_write_and_read.py
    
    多种方式读写 csv 文件的 Demo

- 03 Excel_delele_tools_xlwings.py
    
    通过调用 xlwings 删除 Excel 文件中的特定内容

- 04 split-merge-pdf.py
    
    分割合并 pdf 文件

- 05 fastCopy.py
    
    基于多线程的快速复制移动文件夹, 适用于大量小文件复制太慢的场景，支持多层目录

- 06 video2img.py
    
    将一段视频, 转为一组图片.

- 07 check_idcard_number.py
    
    检测一个字符串是否为中国大陆身份证号码

- 08 compress_img_base64.py
    
    对图片压缩后, 转为 base64编码

- 09 decrypt_excel.py
    
    批量解密Excel文件, pip install msoffcrypto-tool

- 10 retry_decorator_demo.py
    
    重复尝试次数的装饰器 demo

- 11 tree_xml_demo.py
    
    解析 xml 的结构为目录树，能够快速的对 xml 的结构有基本的了解。这也是 nonlocal 新关键字的一个 demo

- 12 cython-package-setup-demo.py
    
    利用 Cython 对 Python 包进行加密 demo, MANIFEST.in and include_package_data=True, 打包资源文件

- 13 logger_demo.py
    
    可在运行时，修改日志输出的文件位置

- 14 zipfile_encrypt.py
    
    通过 pyzipper 模块创建加密的 zip 压缩包

- 15 pandas_loss_rows_solve.py
    
    pandas_csv丢失部分行的问题



## 生成方法

该 Readme.md 通过 auto_readme.py 脚本自动生成, 利用了ast获取Python模块的docstrings, 然后通过 jinja2 的模板来写渲染文件, 测试效果是通过 Jupyter Notebook 完成
```
## 在 Jupyter Notebook 中执行
from IPython.display import Markdown

Markdown(open("Readme.md", encoding="utf-8"))
```
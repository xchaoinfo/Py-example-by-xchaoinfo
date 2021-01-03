# Py-sample-by-xchaoinfo

小而美, 提高生活幸福感的Python脚本, By xchaoinfo.                                    
## 目录

{% for script in script_list %}
- {{script.filename}}
    
    {{ script.docs}}
{% endfor %}


## 生成方法

该 Readme.md 通过 auto_readme.py 脚本自动生成, 利用了ast获取Python模块的docstrings, 然后通过 jinja2 的模板来写渲染文件, 测试效果是通过 Jupyter Notebook 完成
```
## 在 Jupyter Notebook 中执行
from IPython.display import Markdown

Markdown(open("Readme.md", encoding="utf-8"))
```

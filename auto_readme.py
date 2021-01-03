"""根据脚本的内容自动生成 Readme 文档"""
import os
import ast

from jinja2 import Template


def read_file(filename):
    """读取文件内容"""
    with open(filename, encoding="utf-8") as fr:
        data = fr.read()
    return data


def get_pyfile_list(src_folder):
    pyfile_list = [os.path.join(src_folder, fn) for fn in os.listdir(src_folder) if fn.endswith(".py")]
    return pyfile_list


def parser_docs_from_pyfile(src_folder="example"):
    pyfile_list = get_pyfile_list(src_folder)
    script_list = []
    for pyfile in pyfile_list:
        filename = os.path.basename(pyfile)
        # 读取 .py 文件
        pyfile_content = read_file(pyfile)
        docs = ast.get_docstring(ast.parse(pyfile_content))
        script_info = {
            "filename": filename,
            "docs": docs
        }
        script_list.append(script_info)
    return script_list


def main():
    src_folder = "example"
    template_file = "Readme_Template.md"
    out_file = "Readme.md"
    template_content = read_file(template_file)
    script_list = parser_docs_from_pyfile(src_folder)
    template = Template(template_content)
    render_md = template.render(script_list=script_list)
    with open(out_file, "w", encoding="utf-8") as fw:
        fw.write(render_md)


if __name__ == '__main__':
    main()

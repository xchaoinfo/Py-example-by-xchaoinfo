"""解析 xml 的结构为目录树，能够快速的对 xml 的结构有基本的了解。这也是 nonlocal 新关键字的一个 demo
"""
from io import BytesIO

from lxml import etree


def init_xpath(page_source: str):
    """page_source 的 xml 文本转为可以解析的 etree 对象
    """
    xml_root = etree.parse(BytesIO(page_source.encode()))
    return xml_root


def fmt(fg):
    """格式化输出"""
    print("-" * fg, end="")


def tree_xml(root, result, flags=0, step=2):
    result.append((flags, root))

    def tree(root):
        nonlocal flags
        ch_root = root.getchildren()
        if ch_root:
            flags += step
            for ch in ch_root:
                tree_xml(ch, result, flags)
        else:
            pass
    tree(root)
    return result


def main():
    data = """
    <xml>
        <aa>
            <bb></bb>
            <cc>
                <a11></a11>
                <a22>
                    <mue></mue>
                </a22>
            </cc>
            <dd></dd>
        </aa>
        <ee>
            <ff></ff>
        </ee>
    </xml>
    """
    xml_root = init_xpath(data)
    res_xml = tree_xml(xml_root.getroot(), [])
    for fg, _root in res_xml:
        fmt(fg)
        print(_root.tag)


if __name__ == '__main__':
    main()

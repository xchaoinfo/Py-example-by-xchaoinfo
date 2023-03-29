"""通过 pyzipper 模块创建加密的 zip 压缩包
"""

import pyzipper


def zip_encrypt(filenames, outzip, passwd):
    with pyzipper.AESZipFile('new_test.zip',
                             'w',
                             compression=pyzipper.ZIP_LZMA,
                             encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(passwd)
        for filename in filenames:
            zf.write(filename)
        # 可通过下面的方式写入压缩后的文本
        # zf.writestr("hello_str.txt", "hello_str text")


if __name__ == '__main__':
    files = ["hello.txt", "hello.png"]
    outzip = "hello.zip"
    passwd = b"hello"
    zip_encrypt(files, outzip, passwd)

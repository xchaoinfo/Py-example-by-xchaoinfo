"""批量解密Excel文件, pip install msoffcrypto-tool"""
import os
import msoffcrypto


def decrypt_excel(filename, decrypted_filename, password):
    """解密一个Excel文件
    Arguments:
        filename -- [需要解密的Excel文件名称]
        decrypted_filename -- [解密后excel文件名称]
        password -- [Excel的密码]
    """
    with open(filename, "rb") as frb, open(decrypted_filename, "wb") as fwb:
        excel = msoffcrypto.OfficeFile(frb)
        excel.load_key(password=password)
        excel.decrypt(fwb)


def get_excel_list(folder, format=".xlsx"):
    fnlist = [os.path.join(folder, fn) for fn in os.listdir(folder) if fn.endswith(format)]
    return fnlist


if __name__ == '__main__':
    password = "123456"
    folder = "data"
    save_folder = "data_res"
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    excel_list = get_excel_list(folder)
    for fn in excel_list:
        print(fn, "start")
        decrypted_fn = os.path.join(save_folder, "decrypted" + os.path.basename(fn))
        decrypt_excel(fn, decrypted_fn, password)


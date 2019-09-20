"""
检测是否为中国大陆身份证号码
"""
import time


def checkIdNumber(id_number):
    """验证身份证号码是否正确
    [从省份代码。出生日期，校验码几个维度来验证匹配出来的身份证的是否正确]
    Arguments:
        id_number(str) -- [18位身份证号码: str]
    Returns:
        bool  -- 返回身份证号码，或者 False
    """
    if len(id_number) != 18:
        return False

    # 省份代码
    id_number = str(id_number)
    provinceCode = ["11", "12", "13", "14", "15", "21", "22",
                    "23", "31", "32", "33", "34", "35", "36", "37", "41", "42", "43",
                    "44", "45", "46", "50", "51", "52", "53", "54", "61", "62", "63",
                    "64", "65", "71", "81", "82", "91"]
    # 省份代码验证
    id_province = id_number[:2]
    if id_province not in provinceCode:
        return False

    # 出生日期验证, 默认出生日期的年份为 19 和 20
    id_date = id_number[6:14]

    if id_date[:2] not in ["19", "20"]:
        return False
    try:
        time.strptime(id_date, "%Y%m%d")
    except ValueError:
        return False

    # 第 18 位校验码验证
    # 身份证前17位每位加权因子
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 身份证第18位校检码
    checkNumber = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
    id_number_17 = [int(i) for i in list(id_number[:17])]
    total = sum([i * j for i, j in zip(id_number_17, weights)])
    # print(total, total % 11)
    check_location = total % 11
    if checkNumber[check_location] != id_number[-1].upper():
        return False

    return True


if __name__ == '__main__':
    id_number = "xxxxxxxx"
    result = checkIdNumber(id_number)
    print(id_number, result)


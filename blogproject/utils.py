import hashlib


def encryption_md5(value):
    # 获取md5加密对象
    my_md5 = hashlib.md5()
    # 加密函数   数据使用utf-8编码
    my_md5.update(value.encode("utf-8"))
    # 获取加密后的数据
    data = my_md5.hexdigest()
    # 返回数据
    return data

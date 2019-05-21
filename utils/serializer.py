

def to_dict(obj, params):
    """
    将一个对象的部分属性转为字典
    :param obj:  对象
    :param params: 属性列表
    :return: 一个字典
    """
    data = {}
    for p in params:
        if (hasattr(obj, p)):
            data[p] = getattr(obj, p)
    return data
"""重复尝试次数的装饰器 demo"""
import time
import logging
from funtools import wraps


def retry(ExceptionToCheck=Exception, tries=3, delay=3, backoff=2, logger=None):
    """重复调用一定的次数(默认是3) 三次调用失败, 返回 False
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries + 1, delay
            mlogger = logger or logging
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    mlogger.warning(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return False

        return f_retry  # true decorator

    return deco_retry

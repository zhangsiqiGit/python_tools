# -*- coding: utf-8 -*-
"""
@ Author: Siqi.Zhang
@ Update_time: 2019.8.28
@ Contents: this file is writing for logging file, need to modify the last function
"""
import functools
import logging


def create_logger():
    logger = logging.getLogger('test_log')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('test.log')
    fmt = '\n%(asctime)s %(filename)s [line: %(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def log_exception(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        logger = create_logger()
        try:
            fn(*args, **kw)
        except Exception as e:
            logger.exception("[Error in {}] msg: {}".format(fn.__name__, str(e)))
            # 如果需要，抛出异常，否则注掉
            # raise
    return wrapper


@log_exception
def your_function():
    data = [1, 2, 's', 8, 'u']
    for d in data:
        n = d + 1
        print(n)


your_function()
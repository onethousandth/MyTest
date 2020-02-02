# -*- coding:utf-8 -*-
#
# Copyright (C) AddyXiao <addyxiao@msn.cn>
#
#

import traceback
import logging
from functools import reduce
"A error test example"

__author__ = "AddyXiao"
__author_email__ = "addyxiao@msn.cn"


def str2num(s):
    try:
        s=s.strip()
        return int(s)
    except ValueError as e:
        logging.exception(e)
        return float(s)

def cacl(exp):
    ss = exp.split("+")
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc+x, ns)


def main():
    try:
        r = cacl("100+200+345")
        print("100 + 200 + 345 = ", r)
        r = cacl("99+88+7.6")
        print("99 + 88 + 7.6 = ", r)
    except Exception as e:
        logging.exception(e)
        raise


main()

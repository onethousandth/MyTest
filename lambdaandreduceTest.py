# -*- coding:utf-8 -*-
#
# Copyright (C) AddyXiao <addyxiao@msn.cn>
#
#

from functools import reduce
import logging
import json

"A Lambda and Reduce Test"

__author__ = "AddyXiao"
__author_emain__ = "addyxiao@msn.cn"


def str2num(s):
    return json.loads(s)


def calc(exp):
    ss = exp.split("+")
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc+x, ns)


def main():
    try:
        str = "1+2+3+4+5+6+7+8+9+10"
        r = calc(str)
        print("1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = ", r)
    except ValueError as e:
        logging.exception(e)
        raise


main()

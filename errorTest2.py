# -*- coding:utf-8 -*-
#
# Copyright (C) Addyxiao <addyxiao@msn.cn
#

import logging
import traceback
import json
from functools import reduce

"Anthor Error Testing"

__author__ = "AddyXiao"
__author_email__ = "addyxiao@msn.cn"


def str2num(s):
    return json.loads(s)


def calc(exp):
    ss = exp.split("+")
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc+x, ns)


def main():
    try:
        r = calc("100+200+345")
        print("100 + 200 + 345 = ",r)
        r = calc("99+88+7.6")
        print("99 + 88 +7.6 = ", r)
    except Exception as e:
        logging.exception(e)
        raise


main()

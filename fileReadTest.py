# -*- coding:utf-8 -*-
#
# Copyright (C) AddyXiao <addyxiao@msn.cn>
#
#

"A read file Test"

__author__ = "AddyXiao"
__author_email__ = "addyxiao@msn.cn"

fpath = r"D:\Documents\Python\MyTest\restrictClass.py"

with open(fpath, "r") as f:
    s = f.read()
    print(s)

# -*- coding:utf-8 -*-
#
# Copyright (C) AddyXiao@msn.cn <addyxiao@msn.cn>
#
#

"A Test of inner function dir()"

__author__ = "addyxiao"
__author_email__ = "addyxiao@msn.cn"

int_Count = 0
for x in dir("ABC"):
    print(x)
    int_Count=int_Count+1
print(int_Count)

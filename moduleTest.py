# -*- coding:utf-8 -*-
# Copyrith (C) 2020 AddyXiao <AddyXiao@msn.cn>
#
# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/master/COPYING.LESSER

"""A module test"""

__author__="AddyXiao"
__authoremail__="addyxiao@msn.cn"

import sys
import os

def test():
    args=sys.argv
    if len(args)==1:
        print("Hello,world!")
    elif len(args)==2:
        print("Hello,%s!"% args[1])
    else:
        print("Too many arguments!")

if __name__=="__main__":
    test()
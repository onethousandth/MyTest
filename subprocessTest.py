# -*- coding:utf-8 -*-
#
# Copyright (C) AddyXiao <addyxiao@msn.cn>
#
#

import subprocess

"A subprocess test"

__author__="AddyXiao"
__author_email__="addyxiao@msn.cn"

def main():
    print("$nslookup www.python.org")
    r=subprocess.call(["nslookup","www.python.org"])
    print("Exit code.",r)

if __name__=="__main__":
    main()


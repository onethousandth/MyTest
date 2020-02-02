# -*- coding:utf-8 -*-
# Copyright (C) AddyXiao <addyxiao@.msn.cn>
#
#

"A test of Class Inherit"

__author__ = "AddyXiao"
__author_email__ = "addyxiao@msn.cn"


class clsAnimal(object):
    pass


class clsMammal(object):
    pass


class clsBird(object):
    pass


class clsRunnable(object):
    pass


class clsFlyable(object):
    pass


class clsDog(clsMammal, clsRunnable):
    pass


class clsBat(clsMammal, clsFlyable):
    pass

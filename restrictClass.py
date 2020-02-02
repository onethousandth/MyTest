# -*- coding:utf-8 -*-
# Copyright (C) AddyXiao <addyxiao@msn.cn>
#
#

"A restrict class test"


class clsMyFamily(object):
    __slots__ = ("name", "role")

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def print_role(self):
        print("I'm %s, and my role is %s" % (self.name, self.role))


myfamily = clsMyFamily("AddyXiao", "Father")
myfamily.print_role()
myfamily.name="EleaZhao"
myfamily.role="Mother"
myfamily.print_role()

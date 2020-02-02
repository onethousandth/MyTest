# -*- coding:utf-8 -*-
#
# Copyright (C) AddyXiao <addyxiao@msn.cn>
#

import unittest
from mydict import Dict

"An unit test sample"

__author__ = "AddyXiao"
__author_email__ = "addyxiao@msn.cn"


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, Dict))

    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == "__main__":
    unittest.main()

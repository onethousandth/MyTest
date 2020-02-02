# -*- coding -*-
# Copyriht (C)  2019-2028 AddyXiao <onethousandth@163.com>
#
#

# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/master/COPYING.LESSER


"""MyTest packing information"""

version = "1.0.0"
numversion = tuple(int(elem) for elem in version.split(".") if elem.isdigit())

extras_require = {}
install_requires = [
    "lazy_object_proxy==1.4.*",
    "six~=1.12",
    "wrapt==1.11.*",
    'typed-ast>=1.4.0,<1.5;implementation_name== "cpython" and python_version<"3.8"',
]

license = "LGPL"
author = "Python Code Quality Authority"
author_email = "onethousandth@163.com"
mailinglist = "mailto://%s" % author_email
web = "https://github.com/addyxiao"

description = "An abstract syntax tree for Python with inference support."

classifiers = [
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Quality Assurance",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
]
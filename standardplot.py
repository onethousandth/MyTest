# -*- coding:utf-8 -*-
#
# Copyright (C) AddyXiao <addyxiao@msn.cn>
#
#


"A test of plot"

__author__ = "AddyXiao"
__author_email__ = "addyxiao@msn.cn"

# import matplotlib.pyplot as plt
# import numpy as np

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

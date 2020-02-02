# -*- codingLutf-8 -*-
#
# Copyright (C) AddyXiao <addyxiao.msn.cn>
#
#

import os

print(dir(os.path))


def dir(Dir):
	print(Dir)
	for x in os.listdir(Dir):
		if os.path.isdir(x):
			nextDir = os.path.join(Dir, x)
			dir(nextDir)
		else:
			print(os.path.join(Dir, x))

def main():
	dir(os.path.abspath('.'))

if __name__ == '__main__':
	main()
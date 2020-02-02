# -*- coding:utf-8 -*-
#
# Copyright (C) AddyXiao <addyxiao@msn.cn>
#
#

from multiprocessing import Process
import os


def run_process(name):
    print("Run child process %s (%s)" % (name, os.getpid()))


if __name__ == "__main__":
    print("Parent process is %s" % os.getpid())
    p = Process(target=run_process, args=("Test",))
    print("Child process will start.")
    p.start()
    p.join()
    print("Child process end.")

# -*- conding:utf-8 -*-
#
# Copyright (C) AddyXiao <addyxiao@msn.cn>
#

from multiprocessing import Process
from multiprocessing import Pool
import time
import os
import random

"A pool process test!"


def long_time_task(name):
    print("Run task %s (%s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s run %.2f seconds." % (name, (end-start)))


def main():
    print("Parent process %s ." % os.getpid())
    p = Pool(4)
    for i in range(8):
        p.apply_async(long_time_task, args=(i,))
    print("Waiting for subprocess done.")
    p.close()
    p.join()
    print("All subprocess done.")


if __name__ == "__main__":
    main()

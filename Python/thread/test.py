#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time

from threading import Thread


def fun(i):
    while True:
        if i > 1000000:
            break

        i += 1


start_time = time.time()

fun(0)

end_time = time.time()
print(end_time - start_time)
start_time = time.time()

i = 0
ts = []

for i in range(10):
    t = Thread(target=fun, args=[i])
    t.start()
    ts.append(t)

for t in ts:
    t.join()

end_time = time.time()
print(end_time - start_time)

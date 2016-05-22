#!/usr/bin/python

# coding=UTF-8

import copy


def yield_test():
    num_list = range(1, 10);
    for x in num_list:
        yield x


newx = yield_test()

for num in newx:
    print num

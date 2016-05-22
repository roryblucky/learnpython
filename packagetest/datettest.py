#!/usr/bin/python

# coding=UTF-8

from random import *
from time import *

date1 = (2016, 5, 22, 18, 51, 22, -1, -1, -1)
time1 = mktime(date1)
date2 = (2017, 5, 22, 18, 51, 22, -1, -1, -1)
time2 = mktime(date2)

random_time = uniform(time1, time2)

print asctime(localtime(random_time))

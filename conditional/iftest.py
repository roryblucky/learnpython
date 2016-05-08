#!/usr/bin/python

# coding = UTF-8

"""为零或为空的字符串、数组、列表、字典都为False"""
if 0:
    print "hahah %s" % "wocao"
else:
    print "False"

x = [1, 2, 3]
y = [2, 4]

print x is not y  # True

del x[2]
print x  # [1,2]
y[1] = 1
print y  # [2,1]
y.reverse()
print y  # [1, 2]

#!/usr/bin/python
# coding=utf-8

d = {"x": 1, "y": 2, "z": 3}

for k, v in d.items():
    print k, v

list = range(1,5)
list1 = xrange(1, 1000000)

print "%s \n %s\n" % (list1, list)

result = zip(list, list1)

print result

for v1, v2 in result:
    print "%d --> %d" % (v1, v2)
print "\n"

str = "test hahahah"

for index, value in enumerate(str):
    print "%d --> %s" % (index, value)

l = ['1', '2', '3', '4']
print " ".join(reversed(l))

print sorted(l)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print sum(a)
print reduce(lambda x, y: x + y, a)

print filter(lambda x: x > 3, a)
print [x for x in a if x > 3]

print map(lambda x: x + 5, a)
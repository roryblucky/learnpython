#!/usr/bin/python

# coding=UTF-8

from os import path


def print_content(content):
    print content


rel_path = path.abspath("test.txt")

f = open(rel_path, "r", 1)

for l in f:
    print l

# create python file scrapy_env.py

from __future__ import print_function
import re, json , copy
import difflib

def compare(str1, str2):
    a = str1.splitlines()
    b = str2.splitlines()
    d = difflib.Differ()
    diff = d.compare(a, b)
    print('\n'.join(diff))
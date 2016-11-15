import sys
import numbers
from omput import *
from omparse import *
from openmath import *

#Sums all the numbers in a list
obj = ParseOMfile('tst/list.xml')
if type(obj) == list:
    acc = 0
    for x in obj:
        if isinstance(x, numbers.Number):
            acc += x
    OMprint(acc)
elif isinstance(obj, numbers.Number):
    OMprint(obj)

import math
from math import *
import operator

import OMTypes as T

import error
from error import *

import fractions
from fractions import gcd

################################################################
#
# Parsing OpenMath objects
#

################################################################
#
# OpenMath content dictionaries
#
omdicts = {}

# list1             http://www.openmath.org/cd/list1.xhtml
omdicts['list1'] = {}

# logic1            http://www.openmath.org/cd/logic1.xhtml
omdicts['logic1'] = {}

# nums1_rational    http://www.openmath.org/cd/nums1.xhtml
omdicts['nums1'] = {}

# complex1          http://www.openmath.org/cd/complex1.xhtml
omdicts['complex1'] = {}

# interval1         http://www.openmath.org/cd/interval1.xhtml
omdicts['interval1'] = {}

# linalg2           http://www.openmath.org/cd/linalg2.xhtml
omdicts['linalg2'] = {}

# ecc               http://www.openmath.org/cd/ecc.xhtml
omdicts['ecc'] = {}

# python            Private content dictionary for representing Python data types
omdicts['python'] = {}

# relation1         http://www.openmath.org/cd/relation1.xhtml
omdicts['relation1'] = {}

#integer1           http://www.openmath.org/cd/interval1.xhtml
omdicts['integer1'] = {}

# error             http://www.openmath.org/cd/error.xhtml
omdicts['error'] = {}

# arith1            http://www.openmath.org/cd/arith1.xhtml
omdicts['arith1'] = {}



# list1.list
def oms_list1_list(list):
    return list

# nums1.rational
def nums1_rational(values):
    return T.Rational(values[0], values[1])

# complex1.complex_cartesian
def complex1_complex_cartesian(values):
    return T.ComplexCartesian(values[0], values[1])

# integer1.integer_interval
def integer_interval(values):
    #return T.IntegerInterval(values[0],values[1])
    return range(values[0],values[1]+1)

# linalg2.matrixrow
def matrixrow(elements):
    return T.MatrixRow(elements)

# linalg2.matrix
def matrix(rows):
    return T.Matrix(rows)

# python.dict OpenMath representation of Python dictionary
def oms_python_dict(d):
    mergedDict = {}
    for t in d:
        mergedDict.update(t)
    return mergedDict

# keyval OpenMath representation of a key value pair in a Python dictionary
def oms_python_keyval(kv):
    if type(kv[0]) == list or type(kv[0]) == dict:
        raise NonHashableTypeError("Can't use unhashable type as key to dictionary")
    return {kv[0] : kv[1]}

# ecc.Pair
def oms_ecc_Pair(x):
    return (x[0], x[1])

# relation1.eq
def oms_relation1_eq(x):
    return T.Relation(operator.eq, x[0], x[1])

# relation1.lt
def oms_relation1_gt(x):
    return T.Relation(operator.lt, x[0], x[1])

# relation1.gt
def oms_relation1_lt(x):
    return T.Relation(operator.gt, x[0], x[1])

# relation1.neq
def oms_relation1_neq(x):
    return T.Relation(operator.ne, x[0], x[1])

# relation1.geq
def oms_relation1_geq(x):
    return T.Relation(operator.ge, x[0], x[1])

# relation1.leq
def oms_relation1_leq(x):
    return T.Relation(operator.le, x[0], x[1])

# integer1.factorial
def oms_integer1_factorial(x):
    if type(x[0]) != int:
        raise NonIntegerFactorialError("Non-integer input to factorial")
    if x[0] < 0:
        raise NegativeFactorialError("Negative input to factorial")
    return math.factorial(x[0])

# error.unhandled_symbol
def oms_error_unhandled_symbol(x):
    return "unhandled_symbol"

# error.unexpected_symbol
def oms_error_unexpected_symbol(x):
    return "unexpected_symbol"

# error.unsupported_CD
def oms_error_unsupported_CD(x):
    return "unsupported_CD"

# arith1.lcm
def oms_lcm(values):
    if values[1] == 0:
        return values[0]
    else:
        return (values[0]*values[1])/gcd(values[0],values[1])

#arith1.gcd
def oms_gcd(values):
    return gcd(values[0], values [1])

#arith1.plus
def oms_plus(values):
    return (values[0] + values[1])

#arith1.lcm
def oms_unary_minus(values):
    if(values[0]>0):
        return (-values[0])
    else:
        return (values[0])

#arith1.minus
def oms_minus(values):
    return(values[0] - values[1])

#arith1.times
def oms_times(values):
    return(values[0] * values[1])

#arith1.divide
def oms_divide(values):
    return(values[0]/values[1])

#arith1.power
def oms_power(values):
    return(values[0]**values[1])

#arith1.abs
def oms_abs(values):
    return abs(values[0])

#arith1.root
#https://en.wikipedia.org/wiki/Talk%3ANth_root_algorithm
def oms_root(values):
    x, xp = 1, -1
    while abs(x - xp) > 1:
        xp, x = x, x - x/values[1] + values[0]/(values[1] * x**(values[1]-1))
    while x**values[1] > values[0]:
        x -= 1
    return x

#arith1.sum
def oms_sum(values):
    [vals, arith] = values
    y = sum([arith([x])for x in vals])
    return y

#arith1.product
from functools import reduce 
def oms_product(values):
    [vals, arith] = values
    list = [arith([x])for x in vals]
    a = reduce(operator.mul, list, 1)
    return a



omdicts['list1']['list'] = oms_list1_list

omdicts['logic1']['true'] = True
omdicts['logic1']['false'] = False

omdicts['nums1']['rational'] = nums1_rational

omdicts['complex1']['complex_cartesian'] = complex1_complex_cartesian

omdicts['interval1']['integer_interval'] = integer_interval

omdicts['linalg2']['matrixrow'] = matrixrow
omdicts['linalg2']['matrix'] = matrix

omdicts['python']['dict'] = oms_python_dict
omdicts['python']['keyval'] = oms_python_keyval

omdicts['ecc']['Pair'] = oms_ecc_Pair

omdicts['relation1']['eq'] = oms_relation1_eq
omdicts['relation1']['lt'] = oms_relation1_lt
omdicts['relation1']['gt'] = oms_relation1_gt
omdicts['relation1']['neq'] = oms_relation1_neq
omdicts['relation1']['leq'] = oms_relation1_leq
omdicts['relation1']['geq'] = oms_relation1_geq

omdicts['integer1']['factorial'] = oms_integer1_factorial

omdicts['error']['unhandled_symbol'] = "unhandled_symbol"
omdicts['error']['unexpected_symbol'] = "unexpected_symbol"
omdicts['error']['unsupported_CD'] = "unsupported_CD"

omdicts['arith1']['lcm'] = oms_lcm
omdicts['arith1']['gcd'] = oms_gcd
omdicts['arith1']['plus'] = oms_plus
omdicts['arith1']['unary_minus'] = oms_unary_minus
omdicts['arith1']['minus'] = oms_minus
omdicts['arith1']['times'] = oms_times
omdicts['arith1']['divide'] = oms_divide
omdicts['arith1']['power'] = oms_power
omdicts['arith1']['abs'] = oms_abs
omdicts['arith1']['root'] = oms_root
omdicts['arith1']['sum'] = oms_sum
omdicts['arith1']['product'] = oms_product

# Flag indicating whether we are parsing an attribution or not.
attr = False


################################################################
#
# Basic OpenMath elements
#

# OpenMath integer
def ParseOMI(node):
    return int(node.text)

# OpenMath float
def ParseOMF(node):
    return float(node.get('dec'))

# OpenMath string
def ParseOMSTR(node):
    return str(node.text)

def ParseOMS(node):
    global attr
    # returns a function or an object
    if attr:
        return T.OMSymbol(node.get('cd'), node.get('name'))

    if not (node.get('cd') in omdicts.keys()):
        return T.OMError(T.OMSymbol("error", "unsupported_CD"), ParseOMS_E(node))
    
    if not (node.get("name") in omdicts[node.get("cd")].keys()):
        return T.OMError(T.OMSymbol("error", "unexpected_symbol"), ParseOMS_E(node))


    return omdicts[node.get('cd')][node.get('name')]

def ParseOMA(node):
    elts = []
    for child in node.findall("*"):
        elts.append(ParseOMelement(child))
    # now the first element of 'elts' is a function to be applied to the rest of the list
    return elts[0](elts[1:len(elts)])

def ParseOMS_E(node):
    return T.OMSymbol(node.get('cd'), node.get('name'))

def ParseOME(node):
    elts = []
    elts.append(ParseOMS_E(node[0]))
    elts.append(ParseOMS_E(node[1]))
    # First element is error type as a string and second is the symbol on which the error occured
    return T.OMError(elts[0], elts[1])

def ParseOMATP(node):
    elts = {}
    count = 0
    thisAttr = None
    for child in node.findall("*"):
        count = count + 1
        if count % 2 == 1:
            thisAttr = ParseOMS(child)
        else:
            elts[thisAttr] = ParseOMelement(child)        
    return elts

def ParseOMATTR(node):
    global attr
    attr = True
    omatp = ParseOMATP(node[0])
    attr = False
    sym = ParseOMelement(node[1])
    return T.OMAttr(omatp, sym)

ParseOMelementHandler = {'OMS' : ParseOMS, 'OMA' : ParseOMA ,  'OMI' : ParseOMI, 'OMF' : ParseOMF, 'OMSTR' : ParseOMSTR, 'OME' : ParseOME, 'OMATTR' : ParseOMATTR}

def ParseOMelement(obj):
    return ParseOMelementHandler[obj.tag](obj)

def ParseOMroot(root):
    try:
        return ParseOMelement(root[0])
    except NonIntegerFactorialError as error:
        print("Parse error: " + repr(error))
    except NonHashableTypeError as error:
        print("Parse error: " + repr(error))


################################################################

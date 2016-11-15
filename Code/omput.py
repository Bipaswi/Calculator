# Encoding Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html
import operator
import xml.etree.ElementTree as ET
import OMTypes as T
Element = ET.Element
SubElement = ET.SubElement


################################################################
#
# OpenMath integer (OMI)
#
def OMInt(x):
    omelt = Element("OMI")
    omelt.text = str(x)
    return omelt

################################################################
#
# List (list1.list)
#
def OMList(x):
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'list1', 'name' : 'list' }
    omelt.insert(1,oms)
    n = 1
    for t in x:
        n = n + 1
        omelt.insert(n, OMelement(t))
    return omelt

################################################################
#
# OpenMath float (OMF)
#
def OMFloat(x):
    omelt = Element("OMF")
    omelt.text = str(x)
    return omelt

################################################################
#
# OpenMath string (OMS)
#
def OMString(x):
    omelt = Element("OMSTR")
    omelt.text = str(x)
    return omelt

################################################################
#
# Attempt at Logic
#
def OMBool(x):
    oms = Element("OMS")
    if(x == True):
        oms.attrib = { 'cd' : 'logic1', 'name' : 'true' }
    else:
        oms.attrib = { 'cd' : 'logic1', 'name' : 'false' }
    return oms

################################################################
#
# Attempt at Complex
#
def OMComplex(x):
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'complex1', 'name' : 'complex_cartesian' }
    omelt.insert(1,oms)
    omelt.insert(2, OMelement(x.real))
    omelt.insert(3, OMelement(x.imag))
    return omelt

################################################################
#
# Python dictionary represented in OpenMath using private dictionary
#
def OMDict(x):
    omelt = Element("OMA")
    d = Element("OMS")
    d.attrib = { 'cd' : 'python', 'name' : 'dict' }
    omelt.insert(1, d)

    for t in x:
        oma = Element("OMA")
        kv = Element("OMS")
        kv.attrib = {'cd' : 'python', 'name' : 'keyval'}
        oma.insert(1, kv)
        oma.insert(1, OMelement(t))
        oma.insert(2, OMelement(x[t]))
        omelt.insert(1, oma)

    return omelt


################################################################
#
# Python dictionary represented in OpenMath using private dictionary
#
def OMRelation(x):
    omelt = Element("OMA")
    s = Element("OMS")
    s.attrib = {'cd' : 'relation1'}
    s.attrib['name'] = {operator.eq : 'eq',
                        operator.gt : 'gt',
                        operator.lt : 'lt',
                        operator.ge : 'geq',
                        operator.le : 'leq'}[x.op]

    arg1 = OMelement(x.arg1)
    arg2 = OMelement(x.arg2)

    omelt.insert(1, s)
    omelt.insert(2, arg1)
    omelt.insert(3, arg2)

    return omelt

################################################################

def OMmatrixrow(x):
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'linalg2', 'name' : 'matrixrow'}
    omelt.insert(1, oms)
    n = 1
    for element in x.elements:
        n += 1
        omelt.insert(n, OMelement(element))

    return omelt

################################################################

def OMmatrix(x):
    omelt = Element("OMA")
    oms = Element("OMS")
    oms.attrib = { 'cd' : 'linalg2', 'name' : 'matrix'}
    omelt.insert(1, oms)
    n = 1
    for row in x.rows:
        n += 1
        omelt.insert(n, OMmatrixrow(row))

    return omelt

################################################################
#
# OpenMath error generator
#
def OMError(x):
    omelt = Element("OME")
    err = Element("OMS")
    print(x.typ)
    err.attrib = {"cd" : "error", "name" : x.typ.name}
    s = OMSymbol(x.sym)
    omelt.insert(1, err)
    omelt.insert(2, s)
    return omelt

################################################################
#
# Unspecialised OMS used in combination with OMError
#
def OMSymbol(x):
    omelt = Element("OMS")
    omelt.attrib = {"cd" : x.cd, "name" : x.name}
    return omelt

################################################################
#
# Attempt at Logic
#
def OMBool(x):
    omobj = Element("OMS")
    if(x == True):
        omobj.attrib = { 'cd' : 'logic1', 'name' : 'true' }
    else:
        omobj.attrib = { 'cd' : 'logic1', 'name' : 'false' }
    return omobj

################################################################
#
# OMattribution
#
# Generates an OMATTR
#

def OMattribution(x):
    omelt = Element("OMATTR")
    omatp = Element("OMATP")

    for t in x.elements:
        omatp.append(OMelement(t))
        omatp.append(OMelement(x.elements[t]))

    sym = OMelement(x.sym)
    omelt.append(omatp)
    omelt.append(sym)
    return omelt

################################################################
#
# OMelement
#
# Dispatches OpenMath encoding method dependently on the type of x
#
def OMelement(x):
    t = type (x)
    if t == int:
        return OMInt(x)
    elif t == float:
        return OMFloat(x)
    elif t == list:
        return OMList(x)
    elif t == bool:
        return OMBool(x)
    elif t == complex:
        return OMComplex(x)
    elif t == str:
        return OMString(x)
    elif t == dict:
        return OMDict(x)
    elif t == T.Relation:
        return OMRelation(x)
    elif t == T.OMError:
        return OMError(x)
    elif t == T.OMSymbol:
        return OMSymbol(x)
    elif t == T.Matrix:
        return OMmatrix(x)
    elif t == T.MatrixRow:
        return OMmatrixrow(x)
    elif t == T.OMAttr:
        return OMattribution(x)

################################################################
#
# OMobject
#
# Wraps OpenMath encoding for x into OpenMath object
#
def OMobject(x):
    omobj = Element("OMOBJ")
    omobj.insert(1, OMelement(x))
    return omobj

import numbers

################################################################

# Is this the exception we want?
class MatrixError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Matrix(object):
    def __init__(self, rows):
        rowLen = rows[0].numElements()
        for row in rows:
            if(row.numElements() != rowLen):
                MatrixError("Lengths of matrix rows vary")
        self.rows = rows

    def __str__(self):
        string = ''
        for row in self.rows:
            string += (str(row) + ' ')
        return string


class MatrixRow(object):
    def __init__(self, elements):
        for element in elements:
            if not(isinstance(element, numbers.Number)):
                raise MatrixError(element, " is not an instance of number")

        self.elements = elements

    def numElements(self):
        return len(self.elements)

    def __str__(self):
        string = ''
        for element in self.elements:
            string += (str(element) + ' ')
        return string

class IntegerInterval(object):
    def __init__(self, LB, UB):
        self.LB = LB
        self.UB = UB

    def __str__(self):
        return str(self.LB) + ' ' + str(self.UB)


class ComplexCartesian(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return str(self.real) + ' ' + str(self.imag) + 'j'

class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

class Relation(object):
    def __init__(self, op, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.op = op

    def evaluate(self):
        return self.op(self.arg1, self.arg2)

    def __str__(self):
        return str(self.arg1) + " " + str(self.op) + " " + str(self.arg2)

# Used for any symbol which is unrecognised by the parser (particularly those after errors)
class OMSymbol(object):
    def __init__(self, cd, name):
        self.cd = cd
        self.name = name

    def __str__(self):
        return str(self.cd) + "." + str(self.name)

# Represents an OpenMath error
class OMError(object):
    def __init__(self, typ, sym):
        self.typ = typ
        self.sym = sym

    def __str__(self):
        return "Error(" + str(self.typ) + ", " + str(self.sym) + ")"


# Represents an OpenMath attribution
class OMAttr(object):
    def __init__(self, elements, sym):
        self.elements = elements
        self.sym = sym

    def __str__(self):
        return "Attribution(" + str(self.elements) + ", " + str(self.sym) + ")"
import openmath
from OMTypes import *
from openmath import *


print ("--Integer Print--")
s = '<OMOBJ> <OMI>42</OMI> </OMOBJ>'
num = ParseOMstring(s)
print(num)
print

print ("--List Print--")
s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>'
lst = ParseOMstring(s)
print(lst)
print

print ("--Nested List Print--")
s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMF dec="4.1"/> <OMI>42</OMI> <OMI>43</OMI> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMA> </OMOBJ>'
nstlst = ParseOMstring(s)
print(nstlst)
print

print ("--Integer File--")
print(ParseOMfile('tst/integer.xml'))
print
print ("--List File--")
print(ParseOMfile('tst/list.xml'))
print
print ("--Float File--")
print(ParseOMfile('tst/float.xml'))
print
print ("--Matrix File--")
print(ParseOMfile('tst/matrix.xml'))
print
print ("--Complex File--")
print(ParseOMfile('tst/complex.xml'))
print
print ("--Rational File--")
print(ParseOMfile('tst/rational.xml'))
print

print ("--unary_minus.xml File--")
print(ParseOMfile('tst/unary_minus.xml'))
print
print ("--lcm.xml File--")
print(ParseOMfile('tst/lcm.xml'))
print
print ("--plus.xml File--")
print(ParseOMfile('tst/plus.xml'))
print
print ("--minus.xml File--")
print(ParseOMfile('tst/minus.xml'))
print
print ("--gcd.xml File--")
print(ParseOMfile('tst/gcd.xml'))
print
print ("--times.xml File--")
print(ParseOMfile('tst/times.xml'))
print
print ("--divide.xml File--")
print(ParseOMfile('tst/divide.xml'))
print
print ("--power.xml File--")
print(ParseOMfile('tst/power.xml'))
print
print ("--abs.xml File--")
print(ParseOMfile('tst/abs.xml'))
print
print ("--root.xml File--")
print(ParseOMfile('tst/root.xml'))
print
print ("--plus.xml File--")
print(ParseOMfile('tst/plus.xml'))
print
print ("--sum.xml File--")
print(ParseOMfile('tst/sum.xml'))
print
print ("--product.xml File--")
print(ParseOMfile('tst/product.xml'))
print



print ("--String Creation And Parsing--")
print(ParseOMstring(OMstring("Hello world")))
print

print ("--OMPrint Integer--")
OMstring(42)
OMprint(42)
print

print ("--OMPrint List--")
OMstring([1,2,3])
OMprint([1,2,3])
print
print ("--OMPrint String--")
OMprint([1,2,[3,4,5]])
OMstring([1,2,[3,4,5]])
print

print ("--Equality True--")
a = 42
print (a == ParseOMstring(OMstring(a)))

a = [1,2,3]
print (a == ParseOMstring(OMstring(a)))

a = [1,2,[3,4,5]]
print (a == ParseOMstring(OMstring(a)))
print

print ("--Equality False")
print

print ("--Booleans--")
OMprint(True)
OMprint(False)
print

#Testing inputs
print("--complex--")
OMprint(5+5j)
print

print("--Output python dictionary")
OMprint({'Name': 'Zara', 'Age': 7, 'Class': 'First'})

#Testing dictionary in
#print(ParseOMstring(OMstring({'Name': 'Zara', 'Age': 7, 'Class': 'First'})))

print("--Dictionary with dupes--")
print(ParseOMfile("tst/dictionary.xml"))
print()

print("--Server Test--")
OMSend('<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>')
print()
OMSend('<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41 <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>')
print()
OMSend('<OMOBJ> <OMA> <OMS cd="arith1" name="power"/> <OMI> 5 </OMI> <OMI> 4 </OMI> </OMA> </OMOBJ>')
print()
OMSend('<OMOBJ> <OMA> <OMS cd="interval1" name="integer_interval"/> <OMI>-10</OMI> <OMI>10</OMI> </OMA> </OMOBJ>')
print()

print("--Testing Matrix--")
r1 = MatrixRow([2,3,4,5])
r2 = MatrixRow([4,5,6,7])
matrix = Matrix([r1,r2])
OMprint(r1)
OMprint(matrix)
print()

print("--lcm--")
OMprint(oms_lcm([20, 8]))
print

print("--gcd--")
OMprint(oms_gcd([20, 8]))
print

print("--plus--")
OMprint(oms_plus([5, 5]))
print

print("--unary minus--")
OMprint(oms_unary_minus([5]))
print

print("--minus--")
OMprint(oms_minus([10, 5]))
print

print("--times--")
OMprint(oms_times([5,5]))
print

print("--divide--")
OMprint(oms_divide([30,2]))
print

print("--power--")
OMprint(oms_power([5,5]))
print

print("--abs--")
OMprint(oms_abs([-1]))
print

print("--root--")
OMprint(oms_root([125, 3]))


print("--Input python dictionary")
print(ParseOMstring(OMstring({'Name': 'Zara', 'Age': 7, 'Class': 'First'})))

print("--Dictionary with unhashable keys")
print(ParseOMfile("tst/dictionary.xml"))

print("--Factorial input")
print(ParseOMfile("tst/factorial.xml"))

print("--Equality operator")
eq = ParseOMfile("tst/eq.xml")
print(eq)
print(eq.evaluate())
OMprint(T.Relation(operator.eq, 1, 2))

print("--LEQ operator")
le = ParseOMfile("tst/geq.xml")
print(le)
print(le.evaluate())
OMprint(T.Relation(operator.le, 1, 2))

print("--OM errors")
le = ParseOMfile("tst/error.xml")
print(le)
OMprint(le)

print("--OM error generation")
le = ParseOMfile("tst/unsupported_CD.xml")
print(le)
OMprint(le)

print("--OM attribution")
le = ParseOMfile("tst/attribution.xml")
print(le)
OMprint(le)

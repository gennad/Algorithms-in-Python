#Newbie programmer
def fact1(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
print fact1(6)

#First year programmer, studied Pascal
def fact2(x):
    result = 1
    i = 2
    while i <= x:
        result = result * i
        i = i + 1
    return result
print fact2(6)

#First year programmer, studied C
def fact3(x): #{
    result = i = 1;
    while (i <= x): #{
        result *= i;
        i += 1;
    #}
    return result;
#}
print(fact3(6))

#First year programmer, SICP
@tailcall
def fact4(x, acc=1):
    if (x > 1): return (fact((x - 1), (acc * x)))
    else: return acc
print(fact4(6))

#First year programmer, Python
def fact5(x):
    res = 1
    for i in xrange(2, x + 1):
        res *= i
    return res
print fact5(6)

#Lazy Python programmer
def fact6(x):
    return x > 1 and x * fact(x - 1) or 1
print fact6(6)

#Lazier Python programmer
f = lambda x: x and x * f(x - 1) or 1
print f(6)

#Python expert programmer
import operator as op
import functional as f
fact7 = lambda x: f.foldl(op.mul, 1, xrange(2, x + 1))
print fact7(6)

#Python hacker
import sys
@tailcall
def fact8(x, acc=1):
    if x: return fact(x.__sub__(1), acc.__mul__(x))
    return acc
sys.stdout.write(str(fact8(6)) + '\n')

#EXPERT PROGRAMMER
import c_math
fact9 = c_math.fact
print fact(6)

#ENGLISH EXPERT PROGRAMMER
import c_maths
fact10 = c_maths.fact
print fact(6)

#Unix programmer
import os
def fact11(x):
    os.system('factorial ' + str(x))
fact(6)

#Windows programmer
NULL = None
def CalculateAndPrintFactorialEx(dwNumber,
                                 hOutputDevice,
                                 lpLparam,
                                 lpWparam,
                                 lpsscSecurity,
                                 *dwReserved):
    if lpsscSecurity != NULL:
        return NULL #Not implemented
    dwResult = dwCounter = 1
    while dwCounter <= dwNumber:
        dwResult *= dwCounter
        dwCounter += 1
    hOutputDevice.write(str(dwResult))
    hOutputDevice.write('\n')
    return 1
import sys
CalculateAndPrintFactorialEx(6, sys.stdout, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)

#Enterprise programmer
def new(cls, *args, **kwargs):
    return cls(*args, **kwargs)

class Number(object):
    pass

class IntegralNumber(int, Number):
    def toInt(self):
        return new (int, self)

class InternalBase(object):
    def __init__(self, base):
        self.base = base.toInt()

    def getBase(self):
        return new (IntegralNumber, self.base)

class MathematicsSystem(object):
    def __init__(self, ibase):
        Abstract

    @classmethod
    def getInstance(cls, ibase):
        try:
            cls.__instance
        except AttributeError:
            cls.__instance = new (cls, ibase)
        return cls.__instance

class StandardMathematicsSystem(MathematicsSystem):
    def __init__(self, ibase):
        if ibase.getBase() != new (IntegralNumber, 2):
            raise NotImplementedError
        self.base = ibase.getBase()

    def calculateFactorial(self, target):
        result = new (IntegralNumber, 1)
        i = new (IntegralNumber, 2)
        while i <= target:
            result = result * i
            i = i + new (IntegralNumber, 1)
        return result

print StandardMathematicsSystem.getInstance(new (InternalBase, new (IntegralNumber, 2))).calculateFactorial(new (IntegralNumber, 6))

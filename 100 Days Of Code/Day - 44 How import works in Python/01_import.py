
import math


result = math.sqrt(9)
print(result)  # Output: 3.0

"""(SRH) ----------IMPORING SPECIFIC FUNCTION---------- (SRH)"""
from math import sqrt

result = sqrt(9)
print(result)  # Output: 3.0

"""(SRH) ----------IMPORING MULTIPLE SPECIFIC FUNCTIONS OR VARIABLE---------- (SRH)"""
from math import sqrt, pi

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793

"""(SRH) ----------IMPORT EVERYTHING---------- (SRH)"""

""" This is not recommended """
from math import *

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793

"""(SRH) ----------RENAMING AS SHORT NAME---------- (SRH)"""
#from math import pi, sqrt as s
#import math as math_built_in_python
import math as m
result = m.sqrt(9)
print(result)  # Output: 3.0

print(m.pi)  # Output: 3.141592653589793

"""(SRH) ----------VIEWING ALL FUNCTION AND VARIAVLES---------- (SRH)"""
import math

print(dir(math))
print(math.nan,type(math.nan))

"""(SRH) ----------IMPORTING FROM OTHER PROGRAM---------- (SRH)"""

#from hridoy import *
from hridoy import welcome, hri

welcome()
print(hri)


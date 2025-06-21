# sine, cosine and tangent
import math
from math import sin, cos, tan

x = 1
sine = sin(x)
cosine = cos(x)
tangent = tan(x)

print(f"sin({x}): {sine:.4f}")
print(f"cos({x}): {cosine:.4f}")
print(f"tan({x}): {tangent:.4f}")

print()
from math import asin, acos, atan, atan2

y = 0.5
arcsine = asin(x)
arccosine = acos(x)
arctangent = atan(x)
arctangent2 = atan2(y, x)

print(f"arcsin({x}): {arcsine:.4f}")
print(f"arccos({x}): {arccosine:.4f}")
print(f"arctan({x}): {arctangent:.4f}")
print(f"arctan({y}/{x}): {arctangent2:.4f}")

print()
from math import degrees, radians

a = math.pi / 3
b = 180
deg = degrees(a)
rad = radians(b)

print(f"{a:.2f} radians equals {deg:.2f} degrees")
print(f"{b} degrees equals {rad} radians")

print()
# hyperbolic
from math import sinh, cosh, tanh, asinh, acosh, atanh

h_sine = sinh(x)
h_cosine = cosh(x)
h_tangent = tanh(x)
h_arcsine = asinh(x)
h_arccosine = acosh(x)
h_arctangent = atanh(x - 0.1)

print(f"sinh({x}) = {h_sine}")
print(f"cosh({x}) = {h_cosine}")
print(f"tanh({x}) = {h_tangent}")
print(f"asinh({x}) = {h_arcsine}")
print(f"acosh({x}) = {h_arccosine}")
print(f"atanh({x - 0.1}) = {h_arctangent}")

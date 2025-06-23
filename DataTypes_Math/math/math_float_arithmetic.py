"""
These functions are with respect of floating precision numbers
"""

import math

# arithmetic

x = 2.67

ceil = math.ceil(x)                  # The smallest integer greater than or equal to x
floor = math.floor(x)                # The largest integer less than or equal to x
trunc = math.trunc(x)                # The integer part of x

print(
    f"The ceiling of {x} is {ceil}; the floor is {floor}; the truncation is {trunc}"
)

y = -83
z = 42

fabs = math.fabs(y)                  # Absolute value of float x
fma = math.fma(x, y, z)              # Fused multiply-add operation (x * y) + z
fmod = math.fmod(y, z)               # Remainder of division x / y
rem = math.remainder(y, z)           # Remainder of x with respect to y
modf = math.modf(x)                  # Fractional and integer parts of x

print(f"The absolute value of {y} is {fabs}")
print(f"The fused multiply-add operation of {x}, {y} and {z} is {fma:.2f}")
print(f"The remainder of division {y} and {z} is {fmod}; The remainder of {y} with respect to {z} is {rem}")
print(f"The fractional and integer parts of {x} is {modf}")


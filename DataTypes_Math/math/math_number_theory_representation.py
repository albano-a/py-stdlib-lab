import math

x = 8.0
mantissa, exponent = math.frexp(x)

m, e = 0.5, 4
ld = math.ldexp(m, e)

y = 8.495
modf_parts = math.modf(y)

print(
    math.ceil(2.3),         # round up
    math.floor(2.9),        # round down
    math.trunc(-2.7),       # truncate toward 0

    math.copysign(3, -2),   # copy sign
    math.fabs(-5),          # absolute (float)
    math.factorial(5),      # factorial

    math.fmod(5.5, 2.2),    # float modulo

    (mantissa, exponent),   # frexp decomposition
    mantissa * 2**exponent, # frexp reconstruction

    ld,                     # ldexp result
    modf_parts              # modf (fractional, integer)
)

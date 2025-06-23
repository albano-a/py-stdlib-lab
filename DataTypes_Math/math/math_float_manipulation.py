import math

# Manipulation

a = 10
b = -5

cp = math.copysign(10, -5)
ulp = math.ulp(a)  # The distance of a number to the next float
nextafter = math.nextafter(a, 5)  # The smallest float in direction of 5

print(f"Sign of {b} copied to {a}: {cp}")
print(f"ULP of {a}: {ulp}")
print(f"Next float {a} toward {5}: {nextafter}")

frexp = math.frexp(4.687)
ldexp = math.ldexp(frexp[0], frexp[1])

print(f"Mantissa and exponent of {frexp} and the ldexp is {ldexp}")

# checks

a = 24
b = 19

is_close = math.isclose(a, b, rel_tol=1e-1)
is_finite = math.isfinite(a)
is_inf = math.isinf(a)
is_nan = math.isnan(a)

print(f"Is {a} close to {b}?: {is_close}")
print(f"Is {a} finite?: {is_finite}")
print(f"Is {a} infinite?: {is_inf}")
print(f"Is {a} NaN?: {is_nan}")

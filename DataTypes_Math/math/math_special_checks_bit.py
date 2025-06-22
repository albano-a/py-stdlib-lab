import math

x = 4
a = x
b = 3
gamma = math.gamma(x)
lgamma = math.lgamma(x)
erf = math.erf(x)
erfc = math.erfc(x)
hypot = math.hypot(a, b)

print(f"Gamma function of {x} = {gamma}")
print(f"Log of abs(gamma({x})) = {lgamma}")
print(f"Error function at {x} = {erf}")
print(f"1 - Error function at {x} = {erfc}")
print(f"The hypotenus of {a} and {b} is {hypot}")

print()
is_finite = math.isfinite(x)
is_infinite = math.isinf(x)
is_nan = math.isnan(x)

print(f"Is {x} finite? {is_finite}")
print(f"Is {x} infinite? {is_infinite}")
print(f"Is {x} nan? {is_nan}")

print()

ulp = math.ulp(x)
nextafter = math.nextafter(x, 5)

print(f"The distance of {x} to the next float is {ulp}")
print(f"Smallest float > {x} in direction of {5}: {nextafter}")

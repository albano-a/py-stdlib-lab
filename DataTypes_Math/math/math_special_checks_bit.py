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